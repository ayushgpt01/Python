my_list = [5,4,3]

my_dict = {num:num*2 for num in [1,2,3]}
print(my_dict)

print(list(map(lambda item: item ** 2,my_list)))

a =[(0,2), (4,3), (9,9), (10,-1)]
a.sort(key=lambda item:item[1])
print(a)