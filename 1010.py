# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2017/6/15 18:38'
str1=raw_input()
list1 = str1.split(' ')


x = 0
y = 0
e = int(len(list1))-1
list2 = []
length = len(list1)

while x < length:
    a = int(list1[x])
    b = int(list1[x+1])
    c = a*b
    list2.append(c)
    list2.append(b-1)
    x = x + 2
    y = y + 2

d = 0
str2 = ''
while d < len(list2):
    str2 = str2 + str(list2[d]) + " "
    d = d + 1
f = len(list2)-1
if list2[f] == -1:
    print str(str2[:-6])
else:
    print str(str2[:-1])

