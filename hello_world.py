class Addition:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

if __name__ == "__main__":
    obj = Addition(10, 20)
    print(obj.addition())


