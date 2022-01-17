a = 23
prime = True

for i in range (2,a):
    if (a%i==0):
       prime = False
       break
if (prime==True):
    print("This number is prime")
elif (prime==False):
    print("This number is not prime")