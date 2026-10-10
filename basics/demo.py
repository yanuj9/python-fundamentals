
num = 7
salary = 6

if num % 2 == 0:
    print("Even")
    if salary > 5:
        print("Great Job")
    else:
        print("Better Luck next time")
else:
    print("Odd")

print("Bye")


# # in same package (folder) for calculator module
# # package is simply location / folder
# # and module is the file having functions but not being called in that file but to be used by somebody else

# # import calc
# from calculator.calc import add, sub

# # res = calc.add()
# res = add()
# print(res)


# # res1 = calc.sub()
# res1 = sub()
# print(res1)
