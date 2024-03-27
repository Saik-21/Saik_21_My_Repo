class calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def mul(self):
        return self.x*self.y
    def div(self):
        if self.x or self.y>0:
            return round(self.x/self.y,2)
        else:
            return "Not valid input"
    def sub(self):
        if self.x>self.y:
            return self.x - self.y
        elif self.y>self.x:
            return self.y - self.x
        else:
            return 0

c1 = calculator(13,3)
print(c1.add())
print(c1.mul())
print(c1.sub())
print(c1.div())