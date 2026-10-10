
# # # ways to create threads in python

# # # threads using classes
# # # threads using functions

# # from threading import Thread
# # from time import sleep

# # class Hello(Thread):
# #     def run(self):
# #         for i in range(5):
# #             print("Hello", i+1)
# #             sleep(0.1)

# # class Hi(Thread):
# #     def run(self):
# #         for i in range(5):
# #             print("Hi", i+1)

# # if __name__ == '__main__':
# #     # t1 = Hello()
# #     # t2 = Hi()

# #     # t1 = Thread(target=Hello.do()) # Default way, other is inheritence -> run method is mandatory here to execute the thread here else thread will not start
# #     t1 = Hello()
# #     sleep(0.2)
# #     t2 = Hi()

# #     t1.start()
# #     t2.start()

# #     # threads analogy ->

# #     # call 
# #     # WhatsApp
# #     # Cricket

# #     # all 3 run simulaneously

# #     # Another analogy -> 

# #     # In games -> it's You Moving, Enemy1 Moving, Enemy2 Moving, Sound playing, Score being updated

# #     # so here -> execute Hello and Hi simulaneously

# from threading import Thread
# from time import sleep, time

# def Hello():
#     for i in range(5):
#         print("Hello", i+1)
#         sleep(0.1)

# def Hi():
#     for i in range(5):
#         print("Hi", i+1)

# def download(fileanme):
#     print("Downloading file...", fileanme)
#     sleep(0.5)
#     print("Download complete")


# if __name__ == '__main__':
#     # t1 = Thread(target=Hello)
#     # sleep(0.2)
#     # t2 = Thread(target=Hi)

#     # t1.start()
#     # t2.start()

#     # t1.join() # wait for threads to finish
#     # t2.join() # wait for threads to finish

#     files = ['video.mp4', 'image.png', 'data.csv']
#     start = time()
#     for f in files:
#         download(f)
#     end = time()
#     print(f" serial time {end - start:.2f} seconds")


#     threads = []

#     for f in files:
#         t = Thread(target=download, args=(f,))
#         threads.append(t)

#     start = time()

#     for t in threads:
#         t.start()

#     for t in threads:
#         t.join()

#     end = time()

#     print(f"Parallel with threads time {end - start:.2f} seconds")

#     print("Bye")

# from time import time
# from threading import Thread

# def calculate(n1, n2):
#     sum = 0
#     for n in range(n1, n2):
#         sum += n*n

# num = 50_000_000

# start = time()

# calculate(0, num)

# end = time()

# print(f"serial time {end - start:.2f} seconds")

# mid = num // 2

# t1 = Thread(target=calculate, args = (0,mid))
# t2 = Thread(target=calculate, args = (mid, num))

# start = time()

# t1.start()
# t2.start()

# t1.join()
# t2.join()

# end = time()

# print(f"parallel time is {end - start:.2f} seconds")

# To run mutiple threads, in python, we have GIL - Global Interpreter lock
# So one thread gets the lock, is executed and other waits and they keep switching in between

# This switching takes time, hence time taken is more

# Solution for this is -> Multiprocessing

# Unlike threads sharing memory, Processes have their own memory and GIL for each, so no GIL sharing


from time import time
from threading import Thread
from multiprocessing import Process

def calculate(n1, n2):
    sum = 0
    for n in range(n1, n2):
        sum += n*n

if __name__ == '__main__':
    num = 50_000_000

    start = time()

    calculate(0, num)

    end = time()

    print(f"serial time {end - start:.2f} seconds")

    mid = num // 2

    t1 = Thread(target=calculate, args = (0,mid))
    t2 = Thread(target=calculate, args = (mid, num))

    start = time()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time()

    print(f"parallel time with threads is {end - start:.2f} seconds")



    t1 = Process(target=calculate, args = (0,mid))
    t2 = Process(target=calculate, args = (mid, num))

    start = time()

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    end = time()

    print(f"parallel time with proecss is {end - start:.2f} seconds")


# for IO bound, something to happen parallel, speed does not matter -> use Thread
# for having it's own memory and GIL, use Process