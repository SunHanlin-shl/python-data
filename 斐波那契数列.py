k = int(input())
if k == 1 or k == 2:
   print(1)
else:
   a1 = a2 = 1
   for x in range(k-2):
       a1,a2 = a2, a2 + a1
       print(a2)
   



    
    