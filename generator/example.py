def k():
    print('hello')
    yield 23
    print('world')
    yield 'hai'
g=k()#here 
print(g)
print(next(g))