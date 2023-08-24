def loopFunc2(spam):
    while True:
        print("Current value is "+ str(spam))
        spam = spam - 1
        if int(spam) < 0:
            break
 


loopFunc2(15)
