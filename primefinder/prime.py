#TODO enter a time stamp for time it took to generate


testnum = 10000

while True:
   testnum +=1   
   count = 0
   for x in range(1,testnum):
      if testnum%x == 0:
         count += 1
         if count>1:
            continue

   if count<2:
      print(str(testnum) +  " is prime!")
	
   
      
         
