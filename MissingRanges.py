user_input = input("Enter numbers separated by spaces: ")
l = list(map(int, user_input.split()))
l.sort()
j = 0
rang = ()
tuples = []

while j < len(l)-1:
    if l[j]+1 != l[j+1]:
        rang = (l[j]+1, l[j+1]-1)
        tuples.append(rang)
            
    j += 1
    
  
print(tuples)
