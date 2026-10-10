
# # in same package (folder) for calculator module
# # package is simply location / folder
# # and module is the file having functions but not being called in that file but to be used by somebody else

# # import calc
from calc import add, sub

# res = calc.add()
res = add()
print(res)


# # res1 = calc.sub()
# res1 = sub()
# print(res1)

# print(globals())
# print(__name__)

# import calc

# print("in demo : ", __name__)
