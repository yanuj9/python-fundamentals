def fact(num):
    if num == 1:
        return 1

    # for i in range(1,num+1):
    #     result *= i

    # return result
    return num * fact(num-1)

    

result = fact(5)
print(result)