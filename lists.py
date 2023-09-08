def listtest(i):
    spam = list(range(i))
 
    for i in spam: 
        print(str(spam[i]))
        i += 1

    print(spam)
    print(type(spam)) 

def listtest2(i):
    item = range(1, i)
    return list(item)

print(listtest(75))


spam = [2,3,4,5,6,7]
spam[2] = 'hello'
spam.insert(3,'hello')
spam.append('hi')
tuple = (42,)
print(type(tuple))
print(spam)