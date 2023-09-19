myCat = {'size': 'fat', 'color': 'gray', 'disposition':'loud'}
print('my cat is ' +myCat['size'])

print ([1,2,3] == [2,3,1])
tuplecat = tuple(myCat.keys())
print(tuplecat) 

for i,o in myCat.items():
    print(i, o)

print(myCat.get('size', 'none'))
myCat.setdefault()