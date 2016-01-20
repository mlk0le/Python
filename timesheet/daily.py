__author__ = 'Mike'

import math
import sys
print("Use military time format eg: 21")


starthr = int(input ("\nWhat hour did you start: "))
startmin = int(input ("What minute did you start: "))
lunchmin = int(input ("How many minutes was your lunch: "))
endhour = int(input ("What hour did you end: "))
endmin = int(input ("What minute did you end: "))

# run sanity checks
if startmin>60 or endmin>60 or startmin<0 or endmin<0:
   print("\nYour minutes are out of range, exiting script")
   sys.exit()

if starthr>24 or starthr<0 or endhour>24 or endhour<0:
   print("\nYour hours are out of range, exiting script")
   sys.exit()

# round up minutes to nearest hour
fillmin = 60 - startmin
fillhour = starthr + 1

#convert whole hours to minutes 
blockmin = (endhour - fillhour) * 60

#compute and display
totalmin = fillmin + endmin + blockmin - lunchmin 
hours = int(totalmin/60)
minutes = totalmin%60
decimalminutes = minutes / 60

print("\nYou worked: " + str(hours) + "h " + str(minutes) + "m")
print("\nOr: " +  str(decimalminutes+hours))
