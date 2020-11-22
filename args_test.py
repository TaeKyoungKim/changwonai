def myFunc(*args, **kwargs):
    for arg in args:
        print(arg)
    for item in kwargs.items():
        print(item)    

myFunc(10, 20, 'a',x=100, y=200, z='b')