
from functools import reduce

nums = [4,2,8,4,6,2,3,7,5]

# evens = []

# for i in nums:
#     if i % 2 == 0:
#         evens.append(i)

# def is_even(n):
#     return n % 2 == 0

# is_even = lambda n : n % 2 == 0

# evens = list(filter(is_even, nums))


# def double_it(n):
#     return n * 2

# evens = list(filter(lambda n : n % 2 == 0, nums))

# doubles = list(map(lambda n:n*2,evens))

# def sumit(a,b):
#     return a+b

evens = list(filter(lambda n : n % 2 == 0, nums))

doubles = list(map(lambda n:n*2,list(filter(lambda n : n % 2 == 0, nums))))

# sum = reduce(sumit, doubles)

sum = reduce(lambda a,b:a+b, doubles)

print(evens)
print(doubles)
print(sum)

cubes = [2,3,4]
print(reduce(lambda a,b:a+b, map(lambda a:a*a*a, cubes)))