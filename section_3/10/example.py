spam = 42 # global variable

def eggs():
    spam = 24 # local variable

#assignment statement = local variable
#no assignment statement = global variable
print(spam)
print(eggs())

