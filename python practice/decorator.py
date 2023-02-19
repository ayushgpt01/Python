# def my_decorator(func):
#     def wrap_func(*args,**kwargs):
#         func(*args,**kwargs)
#     return wrap_func

# @my_decorator
# def function(x):
#     print(x)

# function(2)
from time import time
def performance(func):
    def wrap_func(*args,**kwargs):
        t1 = time()
        result = func(*args,**kwargs)
        t2 = time()
        print(f'Took {float(t2 - t1)}s')
        return result
    return wrap_func

@performance
def long_time():
    for i in range(100000000000):
        i*5

long_time()