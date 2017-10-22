# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2017/6/15 16:49'

#times = raw_input()

#主循环
def judge(str):
        char = list(str[::])
        a = 0
        b = 0
        c = 0
        for j in range(len(char)):
            if char[j] == 'A':
                a = a+1
            elif char[j] == 'P':
                b = b+1
            elif char [j] == 'T':
                c = c+1
            else:
                return False
            j = j + 1
        if a == 0 or b ==0 or c ==0 or b>1 or c>1:
            return False

        count = [0, 0, 0]  # 设置一个3重计数器
        pos = 0
        i = 0
        while i <= len(char)-1:
            if char[i] == 'A':
                count[pos] = count[pos] + 1
            elif char[i] == 'P' and pos == 0:
                pos = 1
            elif char[i] == 'T' and pos == 1:
                pos = 2
            else:
                return False
            i = i+1
        #判断计数结果是否符合预期

        if (count[2]) != (count[1])*count[0] and count[0]!=0 :
            return False
        else:
            return True


times = int(raw_input("")) # 获取字符串数量
while times > 0:
    str = raw_input("")  # 获取字符串
    result = judge(str)
    if result == True:
        print "YES"
    else:
        print "NO"
    times = times - 1
