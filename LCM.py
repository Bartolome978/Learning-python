x = int(input("Please enter a number: "))
y = int(input("Please enter a number: "))
fx = []
fy = []
prime = False

for i in range(1, x+1):
    if x%i == 0:
       fx.append(i)
      


        
for i in range(1, y+1):
    if y%i == 0:
        fy.append(i)

common_factors = [i for i in fx if i in fy]
hcf = max(common_factors)

print(fx)
print(fy)

lcm = int((x * y)/hcf)

print("The lowest common multiple of", x, "and", y, "is", lcm)

        