n = int(input("Please enter an integer: "))
coprimes = [1]
def hcf(a, b):
    while b != 0:
        a, b = b, a % b

    return a
    
        
for i in range(2, n):
      if hcf(i, n) == 1:
          coprimes.append(i) 
           
          
length = len(coprimes)   

print(coprimes)

print("Number of comprimes ", length)
            

        
    
        
        
        