# numbers = [1, 2, 3, 4]
# result = (x * x for x in numbers)
# print(result)

# # for num in result:
#     # print(num)

# print(next(result))
# print(next(result))


# f = open('test.txt')
# lines = (t.strip() for t in f) 
# comments = (t for t in lines if t[0] == '#')
# for c in comments:
#     print(c)

# def func(num):
#     while num > 0:
#         yield num
#         num -= 1

# # # for num in func(5):
# # #     print(num)

# res = func(5)
# # print(next(res))
# # print(next(res))
# # print(next(res))
        
# print(res.__next__())
# print(res.__next__())
# print(next(res))

# for num in func(5):
#     print(num)

# # else: 
# a = sum(func(5))

# def func():
#    yield 37
#    return 42

# result = func()
# print(result)
# print(next(result))
# print(next(result))

# def func(num):
#    while num > 0:
#        yield num
#        num -= 1

# for num in func(5):
#    if num == 2:
#        break
#    print(num)

# def fib(n):
#     fubi = 1
#     yield fubi
#     fubo = 1
#     yield fubo
#     for i in range(n - 2):
#         fubi, fubo = fubo, fubi + fubo
#         yield fubo
 
#  # yeld eto generator

# for num in fib(12):
# 	pass
# print(num)

# DZ
emails = {'mgu.edu': ['andrei_serov', 'alexander_pushkin', 'elena_belova', 'kirill_stepanov'],
      	'gmail.com': ['alena.semyonova', 'ivan.polekhin', 'marina_abrabova'],
      	'msu.edu': ['sergei.zharkov', 'julia_lyubimova', 'vitaliy.smirnoff'],
      	'yandex.ru': ['ekaterina_ivanova', 'glebova_nastya'],
      	'harvard.edu': ['john.doe', 'mark.zuckerberg', 'helen_hunt'],
      	'mail.ru': ['roman.kolosov', 'ilya_gromov', 'masha.yashkina']}

print(*sorted({i + '@' + k for k, v in emails.items() for i in v}), sep = '\n')