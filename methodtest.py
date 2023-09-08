import random

messages = ('test1', 'test2','test3', 'test4')
newlist = messages
newlist = list(newlist)
newlist[1] = 'cat'
print(messages)
print(newlist)