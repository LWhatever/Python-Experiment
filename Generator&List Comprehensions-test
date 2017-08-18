# -*- coding: utf-8 -*-
def move(n,a,b,c):                 #汉诺塔
    if(n==1):
        print(a,'-->',c);
    else:
        move(n-1, a, c, b);
        move(1, a, b, c);
        move(n-1, b, a, c)

move(3, 'A', 'B', 'C')


#将所有大写字母小写
L1 = ['Hello', 'World', 18, 'Apple', None]
L3 = [s.lower() if isinstance(s, str) else s for s in L1]


#杨辉三角
def triangles():
    L = [1];
    while True:
        yield L;
        L = [1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break
