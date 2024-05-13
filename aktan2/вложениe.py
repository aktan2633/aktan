# def main(name):
#     print('hello')
#     def inner():
#         print('hello',name)
#     inner()
# main('oomat')
# def me(a):
#     def inner(z):
#         return a + z
#     res = inner(100)
#     print(res)
# me(100)

# def total_callory():
#     p=products
#     def count_callory(p):
#         res = 0
#         for i in p.values():
#             res+=i
#         return res
#     print(count_callory(p))

# products = {
#     'apple': 200,
#     'bread' :300,
#     'egg' : 500     
# }
# total_callory()
# #   замыкание

# def summa(x):
#     def inner(a):
#         return x/a
#     return inner

# inner = summa(32)
# print(inner(2))
# print(inner(4))
# print(inner(8))

# def decorator (func):
#     def inner():
#         print('hello')
#         func()
#         print('finish')
#     return inner

# @decorator
def func():
    print('oomat')
func()
import random
def unical(random_100):
    def individual():
        result = list(set(random_100()))
        res = (random.choices(result,k=506))
        res = set(res)
        print(list((res)))
    return individual

@unical
def random_100():
    lst = []
    for i in range(100):
        result =random.randint(10,50)
        lst.append(result)
    return lst

random_100()
