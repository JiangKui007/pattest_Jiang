# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2017/6/15 15:29'



a=input()
b = a / 100
c = a / 10 % 10
d = a % 10
result1 = "B"*b
result2 = "S"*c
e = 1
result3 = ''
while d > 0:
    result3 = result3+str(e)
    e = e+1
    d = d-1
print result1+result2+str(result3)