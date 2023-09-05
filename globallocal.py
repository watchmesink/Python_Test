# Global / Local vars

def globalvar():
    def localvar():
        def local2var():
            spam = str(input())
            return spam
        return local2var()
    return localvar()

print(globalvar())
