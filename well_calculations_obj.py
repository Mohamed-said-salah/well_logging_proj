


class WellCalculations:
	def __init__(self, name: str, CALI: dict, GR: dict):
		name = self.name
		CALI = self.CALI
		GR = self.GR
		## here you add the name of your new field as next (<field_name> = self.<field_name>)
		## ! and also Please!, don't forget to add it to the constructor function as next:-
			# def __init__ (self, <field_name>)



		def get_cali_results(self) -> dict:
			""" This method is to get the CALI result from object
			in like the next syntax {WellCalculations.get_cali_results()} """
			return self.CALI

		def get_mud_cake(self) -> list :
			""" This method is to get the mud_cake result from object
			in like the next syntax {WellCalculations.get_mud_cake()} """
			return self.CALI["mud_cake"]

		def get_wash_out(self) -> list:
			""" This method is to get the wash_out result from object
			in like the next syntax {WellCalculations.get_wash_out()} """
			return self.CALI["wash_out"]

		def get_gr_results(self) -> dict:
			""" This method is to get the GR result from object
			in like the next syntax {WellCalculations.get_gr_results()} """
			return self.GR




