# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2017/6/15 16:14'

sting1 = str(input())
i = 0
sum = 0

length1 = len(sting1)
while i < length1:
    sum = sum + int(sting1[i])
    i = i+1

string2 = str(sum)
a = 0
dir1 = {'1':'yi','2':'er','3':'san','4':'si','5':'wu','6':'liu','7':'qi','8':'ba','9':'jiu','0':'ling'}
length2 = len(string2)
result = ''
while a < length2:

    result = result+dir1[string2[a]]+" "
    a = a+1
print str(result[:-1])
