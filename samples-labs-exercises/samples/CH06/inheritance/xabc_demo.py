from xabc import Ordering

class Ball(Ordering):
    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return hasattr(other, 'radius') and self.radius == other.radius

    def __gt__(self, other):
        return hasattr(other, 'radius') and self.radius > other.radius

b1 = Ball(10)
b2 = Ball(20)
b3 = Ball(10)

print(b1 > b2)
print(b1 <= b2)
print(b1 == b2)
