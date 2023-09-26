import re
beginswithHello = re.compile(r'^Hello')
print(beginswithHello.search('Hello there'))
alldigitsRegex = re.compile(r'^\d+$')
print(alldigitsRegex.search(('12341324123412341234' )))