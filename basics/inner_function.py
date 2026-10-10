
def outer():
    print("inside outer function")
    
    def inner(n):
        print("inside inner funtion", n)

    return inner

value = outer()

value(2)