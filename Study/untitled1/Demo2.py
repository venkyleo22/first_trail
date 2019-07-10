__author__ = 'konangiv'
l=[0,1,2,3,4,5,6]

def f1(x):
    return x*2

def f2(x):
    if x%2==0:
        return True

print([f1(x) for x in l if f2(x)])

print(list(map(f1,filter(f2,l))))
import functools
list(map(f1,functools.reduce(f2,l)))