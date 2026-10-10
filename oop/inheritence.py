
class A:
    def f1(self):
        print("f1 works")

    def f2(self):
            print("f2 works")

    def show(self):
        print("in A show")

# class B(A): # Single level Inheritence

class B:
    def f3(self):
        print("f3 works")

    def f4(self):
            print("f4 works")

    def show(self):
            print("in B show")


# class C(B): # multi level inheritence
class C(A,B):
    def f5(self):
        print("f5 works")

    # def show(self):
    #     print("in C show")


obj1 = C()
obj1.show()

# MRO -> Method Resolution order -> check first class -> Parameter of Inheritence classes in order 