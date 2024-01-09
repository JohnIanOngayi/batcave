#!/usr/bin/python3

class quadrilateral:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    @property
    def area(self):
        return (self.a + self.b + self.c + self.d) / 2
    
    @property
    def perimeter(self):
        return self.a + self.b + self.c + self.d
    
class square(quadrilateral):
    def __init__(self, a):
        super().__init__(a, a, a, a)
        
class rectangle(quadrilateral):
    def __init__(self, a, b):
        super().__init__(a, b, a, b)
        

qd1 = quadrilateral(3, 4, 7, 8)
print(qd1.perimeter)
print(qd1.area)

sq1 = square(3)
print(sq1.perimeter)
print(sq1.area)

rc1 = rectangle(3, 4)
print(rc1.perimeter)
print(rc1.area)