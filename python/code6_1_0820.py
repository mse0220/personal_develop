# a = 10
# def foo(x=a):
#     return x
# a = 5
# print(foo())

#<--------------- start
###: case 1
# def foo(x, itmes=[]):
#     itmes.append(x)
#     return itmes

# print(foo(1)) # [1]
# print(foo(2)) # [1][2]
# print(foo(3)) # [1][2][3]

###: case 2
# def foo(x, items=None):
#     if items is None:
#         itmes = []
#     itmes.append(x)
#     return itmes

# print(foo(1)) # [1]
# print(foo(2)) # [2]
# print(foo(3)) # [3]

#end --------------->
