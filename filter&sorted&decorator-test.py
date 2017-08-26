# -*- coding: utf-8 -*-
#筛选素数
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列
        
for n in primes():
    if n < 1000:
        print(n)
    else:
        break

#筛选回文数
def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

output = filter(is_palindrome, range(1, 1000))
print(list(output))

#排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
def by_score(t):
    return t[1]
L2 = sorted(L, key = by_name)
print(L2)
L2 = sorted(L, key = by_score, reverse = True)
print(L2)

#decorator装饰器
import functools

def log(text='call'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('begin call...')
            print('%s %s():' % (text, func.__name__))
            f = func(*args, **kw)
            print('end call')
            return f
        return wrapper
    return decorator

@log('execute')
def now():
    print('2015-3-25')

now()
