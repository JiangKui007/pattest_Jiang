# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2017/6/14 22:02'

i = input("测试用例个数")

while i >0:
    y=input("测试数据")
    a,b,c = y.replace(' ',',')
    z = a + b > c
    i = i - 1
    print "Case #",i,z

8
PT
if count[0] == 0 or count[1] == 0 or count[2] == 0 or pos != 2:
    return False