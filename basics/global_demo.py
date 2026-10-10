
a = 10

def something():
    print(globals())

    # print(globals()['a'])
    # a = 15

    globals()['a'] = 20

    print("inside a : ", a)

something()

print("outside a : ", a)