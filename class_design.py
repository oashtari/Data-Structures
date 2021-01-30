class Vec2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vec2: ({self.x}, {self.y})"

    # def __str__(self):
    #     return self.__repr__()

    def add(self, other):
        self.x += other.x
        self.y += other.y
        return Vec2(self.x, self.y)
    
    def __add__(self, other):
        ret = Vec2(0,0)
        ret.x = self.x + other.x
        ret.y = self.y + other.y
        return self.add(other)

    def sub(self, other):
        self.x -= other.x
        self.y -= other.y

#you can overwrite pre-existing methods, which you can find with 'dir' on CLI
# specifically for this class, not for all things in python
    def __sub__(self, other):
        print('fishy')

    def mul(self, other):
        self.x *= other.x
        self.y *= other.y

    def div(self, other):
        self.x /= other.x
        self.y /= other.y

    def idiv(self, other):
        self.x //= other.x
        self.y //= other.y

v1 = Vec2(20,10)
v2 = Vec2(10,20)

print(v1)
print(v2)

v1.add(v2)

print(v1)
print(v2)

v1.sub(v2)

print(v1)
print(v2)

v3 = v1 + v2
print("V3", v3)
v1-v2

v1.mul(v2)

print(v1)
print(v2)

v1.div(v2)

print(v1)
print(v2)

v1.idiv(v2)

print(v1)
print(v2)