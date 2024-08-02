#There are two types of iterators
'''builin iterator and User defined iterator'''
sequence=[1,2,3,4,5,6,7,8]
k=iter(sequence)
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
print(next(k))
try:
    print(next(k))#StopIteration
except Exception as v:
    print('you are extracted all the elements in the given CDT',v)  
finally:
    pass