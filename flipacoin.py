import random

list = []
def flipacoingame(i):
    while i < 10000:
        toss = random.randint(0,1)
        if toss == 0:
            list.append('head')
        else:
            list.append('tail')
        i += 1
    headStreak = 0
    totalheadStreaks = 0
    for i in list:
        if i == 'head':
            headStreak += 1
            if headStreak == 6:
                totalheadStreaks += 1
        else:
            headStreak = 0
    
    tailStreak = 0
    totaltailStreaks = 0
    for i in list:
        if i == 'head':
            tailStreak += 1
            if tailStreak == 6:
                totaltailStreaks += 1
        else:
            tailStreak = 0
    print(totalheadStreaks)
    print(totaltailStreaks)
    

flipacoingame(0)
print()
