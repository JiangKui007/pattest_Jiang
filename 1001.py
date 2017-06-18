# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2017/6/15 16:10'

n = input()
i = 0
while n != 1:
    if n%2 == 0:
        n = n/2
        i = i+1
    else:
        n = (3*n+1)/2
        i = i+1
print i