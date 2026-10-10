
# class computer:

#     def config(self):
#         print("M4, 24GB, 512 GB")

#     def details(self, brand, ram):
#         print("brand is : ", brand, " and ram is : ", ram)

# computer1 = computer()
# computer2 = computer()

# # computer.config(computer1)
# # computer.config(computer2)

# computer1.config()
# computer1.details("Apple", "24GB")


class computer:

    # class variable
    # instance variable

    cpuClassVariable = "M4" # class variable

    # init is not constructor, just a method to initialize the value
    def __init__(self, cpu, ram, ssd): # Dender(__Method__ way : (double underscores before and after)) method
        print("init called")
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd

    def config(self):
        print("config : ", self.cpu, self.ram, self.ssd)

    def details(self, brand, ram):
        print("brand is : ", brand, " and ram is : ", ram)

    @classmethod
    def info(cls):
        return cls.cpuClassVariable

    @staticmethod
    def gb_to_bytes(gb):
        return gb * (1024 ** 3)

computer1 = computer("M4", "24GB", "512 GB")
computer2 = computer("M5", "96GB", "2 TB")

# computer.config(computer1)
# computer.config(computer2)

# print(computer2.cpu)

computer1.config()
computer2.config()

res = computer1.info()
print(res)

print(computer.gb_to_bytes(16))

# computer1.details("Apple", "24GB")


# print(type(computer1))

# a = 18

# def abc():
#     pass

# xyz = abc