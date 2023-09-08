

spam = ['apples', 'bananas', 'tofu', 'cats']

def andfunction(func):
    if len(func) < 1:
        return print('error')
    else:
        func[-1] = 'and ' + func[-1] 
        return func

emptylist = []

print(andfunction((spam)))