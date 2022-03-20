
class WellPlotterAndPointCollector:
	
	RES_LOG_NAME = "RS"
	CALI_LOG_NAME = "CALI"
	GR_LOG_NAME = "GR"
	BS_NAME = "BS"
	
	def __init__(self, WELL):
		self.WELL = WELL

	def get_cali(self) -> list|Exception:
		if cali := self.get_curve(self.CALI_LOG_NAME) is not None:
			return cali
		
		raise ValueError("Well Has No CAlIPER LOGS")

	def get_bit_size(self) -> list|Exception:
		if bs := self.get_curve(self.BS_NAME) is not None:
			return bs
		
		raise ValueError("Well Has No CAlIPER LOGS or BS data")


	def get_resistivity(self) -> list|Exception:
		if RESISTIVITY := self.get_curve(self.RES_LOG_NAME) is not None:
			return RESISTIVITY
		
		raise ValueError("Well Has No Resistivity data")

	def get_gr(self) -> list|Exception:
		if gr := self.get_curve(self.GR_LOG_NAME) is not None:
			return gr
		
		raise ValueError("Well Has No GR data")







class WellCalculations:
	def __init__(self, name: str, CALI: dict=None, GR: dict=None, RESISTIVITY: dict =None):
		self.name = name
		self.CALI = CALI
		self.GR = GR
		self.RESISTIVITY = RESISTIVITY

		## here you add the name of your new field as next (<field_name> = self.<field_name>)
		# ! and also Please!, don't forget to add it to the constructor function as next:-
		# def __init__ (self, <field_name>)
		
	def get_cali_results(self) -> dict:
		""" This method is to get the CALI result from object
		in like the next syntax {WellCalculations.get_cali_results()} """
		return self.CALI

	def get_mud_cake(self) -> list :
		""" This method is to get the mud_cake result from object
		in like the next syntax {WellCalculations.get_mud_cake()} """
		return self.CALI["mud-cake"]

	def get_wash_out(self) -> list:
		""" This method is to get the wash_out result from object
		in like the next syntax {WellCalculations.get_wash_out()} """
		return self.CALI["wash-out"]

	def get_gr_results(self) -> dict:
		""" This method is to get the GR result from object
		in like the next syntax {WellCalculations.get_gr_results()} """
		return self.GR







########################################### validation functions ##############################################################

def validate_caliber(collector_result: dict) -> str|Exception|bool:
	""" Make Sure! The Data Entered Here is the Data of Caliper Log
		and name of values on the collecter! is literally 'mud-cake' & 'wash-out'
	"""
	mud_cake = sorted(collector_result['mud-cake'], key=lambda x: x[1])
	wash_out = sorted(collector_result['wash-out'], key=lambda x: x[1])
	if not (len(mud_cake)%2 == 0):
		raise ValueError("Mud Cake Events dosen't completely Picked!!")
	
	if not (len(wash_out)%2 == 0):
		raise ValueError("Wash Out Events dosen't completely Picked!!")

	mud_cake_depths = [i[1] for i in mud_cake]
	wash_out_depths = [i[1] for i in wash_out]
	ml1=[]
	for i in mud_cake_depths:
		if i not in ml1:
			ml1.append(i)
		else:
			raise ValueError(f"Error!, Depth {i} in mud-cake values is repeated, detail: Can't pick point at the same depth twice!")
	wl1 = []
	for i in wash_out_depths:
		if i not in wl1:
			wl1.append(i)
		else:
			raise ValueError(f"Error!, Depth {i} in wash-out values is repeated, detail: Can't pick point at the same depth twice!")
	

	mud_cacke_zones = [(mud_cake[i][1],mud_cake[i+1][1]) for i in range(0,len(mud_cake),2)]
	wash_out_zones = [(wash_out[i][1],wash_out[i+1][1]) for i in range(0,len(wash_out),2)]

	for zone in mud_cacke_zones:
		if zone in wash_out_zones:
			raise ValueError(f"Error! at Zone from depth {zone[0]} to dpeth {zone[1]}, details: Can't have the same zone as wash-out and mud-cake.")

	error_text = ""

	for zone in mud_cacke_zones:
		for val in wash_out:
			if zone[0] < val[1] < zone[1]:
				error_text = error_text + f"Wash out Value at depth {val[1]} Conflicts with Mud-Cake Zone from depth {zone[0]} To {zone[1]},\n"
			


	return error_text if not error_text == "" else True




def validate_res(collector_result: dict) -> Exception|bool:
	"Make Sure! the data Entered here is data of resistivity and name on collector! is literally 'RESISTIVITY'"
	res = sorted(collector_result['RESISTIVITY'], key=lambda x: x[1])
	if not (len(res)%2 == 0):
		raise ValueError("RESISTIVITY Events dosen't completely Picked!!")
	
	depths = [i[1] for i in res]
	l1=[]
	for i in depths:
		if i not in l1:
			l1.append(i)
		else:
			raise ValueError(f"Error!, Depth {i} is repeated, detail: Can't pick point at the same depth twice!")

	return True


def validate_gr(collector_result: dict) -> Exception|bool:
	"Make Sure! the data Entered here is data of GR and name on collector! is literally 'GR'"
	gr = sorted(collector_result['GR'], key=lambda x: x[1])
	if not (len(gr)%2 == 0):
		raise ValueError("GR Events dosen't completely Picked!!")

	depths = [i[1] for i in gr]
	l1=[]
	for i in depths:
		if i not in l1:
			l1.append(i)
		else:
			raise ValueError(f"Error!, Depth {i} is repeated, detail: Can't pick point at the same depth twice!")

	return True






