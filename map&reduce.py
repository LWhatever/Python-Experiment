# -*- coding: utf-8 -*-
#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。
#输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']
def normalize(name):
    return name[0].upper()+name[1:].lower()

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#编写一个prod()函数，可以接受一个list并利用reduce()求积
from functools import reduce

def prod(L):
    return reduce(lambda x,y: x*y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
def str2float(s):
    s1 = s.replace('.', '')
    def fn(x, y):
        return x * 10 + y
    def char2num(s1):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s1]
    if '.' in s:
        n = s.index('.')
    else:
        pass
    return reduce(fn, map(char2num, s1))/10**n

print('str2float(\'123.456\') =', str2float('123.456'))
