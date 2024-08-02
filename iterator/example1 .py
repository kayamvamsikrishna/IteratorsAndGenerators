class PowerOfNumber:
    def __init__(self,a,b,u=1):
        self.start=a
        self.end=b
        self.update=u
    def __iter__(self):
        self.i=self.start
        return self
    def __next__(self):
        if self.i<=self.end:
            dummy=self.i**self.i
            self.i+=self.update
            return dummy
        raise StopIteration
vl=PowerOfNumber(1,20)
o=[]
for i in vl:
    o.append(i)
print(o)