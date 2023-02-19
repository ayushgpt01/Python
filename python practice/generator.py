# def generator_func(num):
#     for i in range(num):
#         yield i

# for item in generator_func(1000):
#     print(item)

class MyRange():
    current = 0
    def __init__(self,first,last):
        self.first = first
        self.last = last
    
    def __iter__(self):
        return self
    

    def __next__(self):
        if MyRange.current < self.last :
            num = MyRange.current
            MyRange.current +=1
            return num
        raise StopIteration

ran = MyRange(0,100)
for i in ran:
    print(i)