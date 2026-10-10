
import sys

from time import sleep

# sys.setrecursionlimit(10000)

print(sys.getrecursionlimit())

# count = 1

def greet(count):
    # global count
    if count == 11:
        return
    print("Hello , ", count)
    count += 1
    # sleep(0.02)
    greet(count) 

greet(1)