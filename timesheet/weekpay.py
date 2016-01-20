__author__ = 'Mike'

import sys

hours = float(input("\nEnter hours worked: "))
rate = int(input("Enter rate of pay: "))

if hours<0:
   print("\n1.21 JIGGAWATTS?!?!")
   sys.exit()

if hours>=40:
   reghours = 40
   othours = hours%40
elif hours<40:
   reghours = hours
   othours = 0

# compute
regpretax = reghours * rate
otpretax = othours * (rate*1.5)
totalpretax = regpretax + otpretax
pay = ((reghours * rate) + (othours * (rate*1.5))) * .79 

# display
print("\nreg hours: " + str(reghours))
print("OT hours: " + str(othours))

print("\nreg pay pretax: " + str(regpretax))
print("ot pay pretax: " + str(otpretax))
print("total pretax pay: " + str(regpretax + otpretax))
print("\ntotal posttax pay: " + str(pay))

