s = str(input("Please enter a string: "))
ls = list(s)
substrings = []
noRepeatStrings = []
len(set(s)) == len(s)

# Generate all the substrings of the string
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        substrings.append(s[slice(i, j)])

# Identify the strings with no repeating characters
for i in range(len(substrings)):
   if len(set(substrings[i])) == len(substrings[i]):
       noRepeatStrings.append(substrings[i])
       
        
        
    
        
print(substrings)
print(noRepeatStrings)
print("Longest substring with no repeating characters: ", max(noRepeatStrings, key=len))