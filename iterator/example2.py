class Fibonacci:
    def __init__(self,a,b,c):
        self.start=a
        self.second=b
        self.count=c
    def __iter__(self):
        self.i=self.start
        return self
    def __next__(self):
        if self.i<=self.count:#count
            dummy=self.start
            self.second=self.start
            self.start=dummy+self.start
            self.i+=1
            return dummy
        raise StopIteration
vl=Fibonacci(1,2,30)
o=[]
for i in vl:
    o.append(i)
print(o)