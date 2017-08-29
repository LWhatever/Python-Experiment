#https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014319098638265527beb24f7840aa97de564ccc7f20f6000
#定制类(__str__/__iter__/__getitem__/__getattr__/__call__)
# -*- coding: utf-8 -*-
class Chain(object):
    def __init__(self, path=''):
        self._path = path
    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))
    
    def __call__(self, attr):
        return Chain('%s/%s' % (self._path, attr))
    
    def __str__(self):
        return self._path
    
    __repr__ = __str__
    
print(Chain().users('michael').group('student').repos)
print(Chain().status.user.timeline.list)
print(Chain().users('Kzc').repos)
