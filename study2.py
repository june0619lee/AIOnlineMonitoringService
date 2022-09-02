class SomeClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self) -> int:
        return 100

    def __repr__(self) -> str:
        return self.__class__.__name__ + ' ' + str(self.x) + ',' + str(self.y)

    def __add__(self, other):
        return SomeClass(self.x+other.x, self.y+other.y)


p1 = SomeClass(1, 1)
p2 = SomeClass(1, 3)

p3 = p1 + p2

print(p3)