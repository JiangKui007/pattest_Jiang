# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2017/6/15 18:22'


str1 = raw_input()
list1 = str1.split(' ')
list2 = list1[::-1]
str2 = ''
i = 0
for i in range(len(list2)):
    str2 = str2+list2[i]+' '
    i = i - 1
print str(str2[:-1])