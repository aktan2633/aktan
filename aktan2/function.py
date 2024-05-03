# def  hello_world():
#     print('hello world')
#     hello_world()
# def add(a, b): int
#     return a - b
# result =add('25', '5')
# print=(result)

# original_list = ['aktan','17','1','19']
# def original(orginal_list):
#     half = len(original_list) // 2   
#     list1 = original_list[:half]     
#     list2 = original_list[half:]     
#     list5 = list1[::-1]
#     list6 = list2[::-1]
#     return list5 + list6
# result = original(original_list)
# print(result)

# a= min(12,44,45,4)
# b= max(12,min(93,50),abs(-12),max(12,34,4))
# print(b)

# def square(a):
#     return a ** 2
# so = square(2)
# print(so)

# def even(x):
#     return x % 2 == 0
#     #     return True
#     # else:
#     #     return False
# for i in range(1,11):
#     print(i,even(i))

# x=int(input('number:  '))
# def even(x):
#     return x +1
# print(even(x))
# def bolshe(num):
#     if num < 100:
#             return num
#     else:
#             return 'incorect num'
# print(bolshe(even(x))) 
# def pay(salary):
#     to_pay = salary * 1.12
#     if to_pay > salary:
#         print('ITOGO: ')
#         print('\t{0}'.format(to_pay))
#     else:
#         print('Vy uvolenny')

# pay(0)
# pay(21000)
# pay(120000)
# def const (salary, percent=12):
#     print(salary * percent)

# const(15000)
# const(17000,percent=15)
# *a,b,c= [2,3,4,5,6,78,9,2]
# print(a,b,c)
# def func1(*nums):
#     res = 0 
#     for num in nums:
#         res += num
#     return res
# print(func1(1,2,3,4,5,6,7,8,9,10))
# def func(a,b,c,d):
#     return a,b,c,d
#     print(func(1,2,3,4))
# a = ['hello' ,True,234,[1,2,3]]
# print(func(*a))

# def student(name,**lessons):
#     print(('hello,{name}'))
#     for names,times in lessons.items():
#         print(f'{names}:{times}')
# student('oomat',chemistry =7,math =6 )
# print()
#               3 часть функции