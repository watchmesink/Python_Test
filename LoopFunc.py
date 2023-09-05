def loopFunc2(spam):
    def insidefunc():
        spam2 = 15
        return
    while True:
        print("Current value is "+ str(spam))
        spam = spam - 1
        if int(spam) < 0:
            break
 

for x in range(5):
    loopFunc2(15) 