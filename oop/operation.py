
# a = 5
# b = 6

# # c = a + b

# # c = int.__add__(a,b)
# # c = a.__add__(b)

# print(c)

# print(a.__str__())


class Account:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __str__(self):
        return f'{self.name} : {self.balance}'

    def __add__(self, other):
        return Account('combined', self.balance + other.balance)

    def __gt__(self, other):
        return self.balance > other.balance

user1 = Account("Anuj", 4000)
user2 = Account("stillMissing", 2000)

combined = user1 + user2

print(user1.__str__())
print(user2)
print(combined)

if user1 > user2:
    print("Anuj pays")
else:
    print("stillMissing pays")