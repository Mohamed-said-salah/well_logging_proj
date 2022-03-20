

## *** https://www.pythonguis.com/tutorials/plotting-matplotlib/   *** this is a good link for you to include
## *** matplotlib window inside pyqt5

## Methods in this page
## A- caliber log
## B- GR log
## C- RESISTIVITY log
## D- All logs


## <Example for implementing pointer of caliber log> ##

## 1.
import matplotlib.pyplot as plt      ## import matplotlib
from saied_point_collector import collector  ## import the point collector

from objects.objects import WellCalculations, WellPlotterAndPointCollector, validate_caliber, validate_res ## import the well plotting Object and validation function

## 2.
fig, ax = plt.subplots(figsize=(4, 18), ncols = 1)  ## initialize the plotting window

## 3.
collector = collector(ax, ["mud-cake", "wash-out"], markers=["x", "+"], colors=['orange', 'red']) ## add Point Collector To the plotting window

## 4.
##  !!!  Next is important step focus on how we will use the object
my_plotting_well = WellPlotterAndPointCollector()   ### !! Focus here carefully (You Must!!! provide a well data in this subject)


## 5.
try:
    CALI = my_plotting_well.get_cali()
except:
    ## ? add here a ui that is representing to the non valid caliper log data
    pass


try:
    BS = my_plotting_well.get_bit_size()
except:
    ## ? add here a ui that is representing to the non found! caliper log data and bitsize data
    pass

## 6.
## then you add the plots to axis of matplotlib window
ax = CALI.plot(ax = ax, c='blue')
ax = BS.plot(ax= ax, c='black')

## 7.
## adding some information to the plot and show it 
ax.set_title(f"INTERPRATE CALIBER-LOG in Well: {my_plotting_well.WELL.header.name}")

plt.tight_layout()

plt.show()

## after this you must  make the fukcing UI that is showing all the above staff into it to user 
## !? not you fucking must include the above plotting in the ui Window
## ! links are above 
## may god help you and you start doing it  :::)(:::: 😔😔😔😔😔

## 8. 
## after finishing the staff you fucking validate data 

validate_caliber(collector_result=collector.get_points()) ## !! don't forget ##? this must be added into a submit button


## 10.
# add the well to WellCalculations Object
## ??!! the next will include the values from different picking pages (ex. cali, gr, RESISTIVITY) so we must get it in a more higher order page (route)

## here there is some needed result that will come from the picked result and other logs
calculated_well = WellCalculations(name=my_plotting_well.WELL.header.name, CALI=collector.get_points()) 

## 11.
# here the coming interpretation for the data
## Soon ......









## B- GR log
############################################################################################################
############################################################################################################
############################################################################################################


## <Example for implementing pointer of GR log> ##

## 1.
import matplotlib.pyplot as plt      ## import matplotlib
from saied_point_collector import collector  ## import the point collector
from objects.objects import WellCalculations, WellPlotterAndPointCollector, validate_gr ## import the well plotting Object and validation function

## 2.
fig, ax = plt.subplots(figsize=(4, 18), ncols = 1)  ## initialize the plotting window

## 3.
collector = collector(ax, ["GR"], markers=["x"], colors=['red']) ## add Point Collector To the plotting window

## 4.
##  !!!  Next is important step focus on how we will use the object
my_plotting_well = WellPlotterAndPointCollector()   ### !! Focus here carefully (You Must!!! provide a well data in this subject)


## 5.
try:
    GR = my_plotting_well.get_gr()
except:
    ## ? add here a ui that is representing to the non found! GR log data
    pass

## 6.
## then you add the plots to axis of matplotlib window
ax = GR.plot(ax = ax, c='blue')

## 7.
## adding some information to the plot and show it 
ax.set_title(f"INTERPRATE GR-LOG in Well: {my_plotting_well.WELL.header.name}")

plt.tight_layout()

plt.show()

## after this you must  make the fukcing UI that is showing all the above staff into it to user 
## !? not you fucking must include the above plotting in the ui Window
## ! links are above 
## may god help you and you start doing it  :::)(:::: 😔😔😔😔😔

## 8. 
## after finishing the staff you fucking validate data 

validate_gr(collector_result=collector.get_points()) ## !! don't forget ##? this must be added into a submit button


## 10.
# add the well to WellCalculations Object
## ??!! the next will include the values from different picking pages (ex. cali, gr, RESISTIVITY) so we must get it in a more higher order page (route)

## here there is some needed result that will come from the picked result and other logs
calculated_well = WellCalculations(name=my_plotting_well.WELL.header.name, GR=collector.get_points()) 

## 11.
# here the coming interpretation for the data
## Soon ......








## C- RESISTIVITY log
############################################################################################################
############################################################################################################
############################################################################################################


## <Example for implementing pointer of RESISTIVITY log> ##

## 1.
import matplotlib.pyplot as plt      ## import matplotlib
from saied_point_collector import collector  ## import the point collector
from objects.objects import WellCalculations, WellPlotterAndPointCollector, validate_res ## import the well plotting Object and validation function

## 2.
fig, ax = plt.subplots(figsize=(4, 18), ncols = 1)  ## initialize the plotting window

## 3.
collector = collector(ax, ["RESISTIVITY"], markers=["x"], colors=['red']) ## add Point Collector To the plotting window

## 4.
##  !!!  Next is important step focus on how we will use the object
my_plotting_well = WellPlotterAndPointCollector()   ### !! Focus here carefully (You Must!!! provide a well data in this subject)


## 5.
try:
    RESISTIVITY = my_plotting_well.get_resistivity()
except:
    ## ? add here a ui that is representing to the non found! RESISTIVITY log data
    pass

## 6.
## then you add the plots to axis of matplotlib window
ax = RESISTIVITY.plot(ax = ax, c='blue')

## 7.
## adding some information to the plot and show it 
ax.set_title(f"INTERPRATE RESISTIVITY-LOG in Well: {my_plotting_well.WELL.header.name}")

plt.tight_layout()

plt.show()

## after this you must  make the fukcing UI that is showing all the above staff into it to user 
## !? not you fucking must include the above plotting in the ui Window
## ! links are above 
## may god help you and you start doing it  :::)(:::: 😔😔😔😔😔

## 8. 
## after finishing the staff you fucking validate data 

validate_res(collector_result=collector.get_points()) ## !! don't forget ##? this must be added into a submit button


## 10.
# add the well to WellCalculations Object
## ??!! the next will include the values from different picking pages (ex. cali, gr, RESISTIVITY) so we must get it in a more higher order page (route)

## here there is some needed result that will come from the picked result and other logs
calculated_well = WellCalculations(name=my_plotting_well.WELL.header.name, RESISTIVITY=collector.get_points()) 

## 11.
# here the coming interpretation for the data
## Soon ......

