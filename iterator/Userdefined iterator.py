#user_defined_iterator
class Series:
    def __init__(self,fv,lv,up=1):
        self.fv=fv
        self.lv=lv
        self.updation=up
    def __iter__(self):
        print('__iter__ is called')
        self.i=self.fv
        return self
    def __next__(self):
        print('__next__ is called')
        if self.i<=self.lv:
            dummy=self.i
            self.i+=self.updation
            return dummy
        raise StopIteration
s=Series(1,5)
for k in s:
    print(k)