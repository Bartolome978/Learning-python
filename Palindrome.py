n = int(input("Please enter a number: "))
m = str(n)
x = []
y = []

x = list(map(int, str(m)))
          
y = x[::-1]

print(x)
print(y)
    
if x == y:
    print(n, "is a palindrome")
 
else:
    print(n, "is not a palindrome")
