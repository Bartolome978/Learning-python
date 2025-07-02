user_input = input("Enter numbers separated by spaces: ")
l = list(map(int, user_input.split()))
l.sort()

missingIntegers = []

for i in range(l[0] + 1, l[-1]):
        if i not in l:
            missingIntegers.append(i)
            
print("Missing integers are: ", missingIntegers)
            

            
                