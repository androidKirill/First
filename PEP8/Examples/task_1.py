def example_function(arg1, arg2, arg3):
    print("A function with no spaces in the arguments and a too long construction that goes beyond the limits.        ")


x = 5
y = 10

if x > y:
    print("x is greater than y")
else:
    print("y is greater than x")

for i in range(5):
    print(i)


class E:
    def __init__(self, name):
        self.name = name

        def display_info(self):
            print(f"Name: {self.name}   ")


obj = E("example")
obj.display_info()
