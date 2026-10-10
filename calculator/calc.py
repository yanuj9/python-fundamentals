
# module -> creating a function and not caling it
# so somebody else can use it

def add():
    return "addition"

def sub():
    return "sub"

if __name__ == "__main__":
    print(add())
    print(sub())

# print("in calc : ",__name__)