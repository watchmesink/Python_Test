spam = [15,2,3,4,5,6,7,'cat',['cat','bat']]
variable = input()
spam[0] = variable

for i in range(len(spam)): 
    print(str(spam[-i]))
    i = i+1

print(spam)