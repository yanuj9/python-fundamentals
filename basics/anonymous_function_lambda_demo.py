# assigning a function like variable

# def fun(num):
#     return num * num

# def add(num1, num2):
#     return num1 + num2

# square = fun

# # result = fun(5)
# result = square(5)

# print(result)

fun = lambda num : num * num

add = lambda a,b : a + b

result = fun(5)
print(result)


result2 = add(4,5)
print(result2)

evenOdd = lambda n : print("odd") if n % 2 == 1 else print("even")
print(evenOdd(7))
