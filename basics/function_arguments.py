
# def add(num1 = 9, num2 = 9): # default argument
#     return num1 + num2

# def add(num1, *num2): # variable length argument

#     sum = num1

#     for n in num2:
#         sum += n

#     return sum

# a = add(1,2,3,4)

# print(a)


# def person(name, age = 18):
#     print('name : ', name)
#     print('age : ', age)

# print(name = 'anuj', age = 30) # keyword arguments


def person(name, **kwlength): # keyword length argument
    print('name : ', name)
    for k,v in kwlength.items():
        print(k," : ", v)
    # print(kwlength)

person(age = 23, name = 'anuj', location = "Pune", tech = 'python') 





