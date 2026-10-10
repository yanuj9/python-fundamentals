# decorators get function -> modify it -> return the function
# inner function would have same parameters as the function called
# inner function returns parameter function and outer function returns inner function

def log_deco(fun):
    def wrap(*args, **kwargs):
        print("values ", args)
        res = fun(*args)
        print("wrap res : ",res)
        return res

    return wrap

def greaterFirst(fun):
    def wrap(a,b):
        if(a < b):
            a,b = b,a
        return fun(a,b)
    return wrap

@log_deco
def add(a,b,c):
    return a + b + c

# @greaterFirst
@log_deco
def divide(a,b):
    # if(a < b): 
    #     a,b = b,a
    return a / b

divide = greaterFirst(divide)

res = divide(2,4)
print(res)

# @greaterFirst
def sub(a,b):
    # if(a < b): 
    #         a,b = b,a
    return a - b

sub = greaterFirst(sub)

res2 = sub(2,4)
print(res2)

res3 = add(5,7,6)
print(res3)



def logger(fun):
    def wrap():
        print("log message 1")
        res = fun()
        print("log message 2")
        return res
    return wrap

@logger
def greet():
    print("Hello, python!")

greet()