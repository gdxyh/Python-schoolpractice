#上级课二 练习题一
'''输入年份，判别该年是否为闰年。①能够被4整除，但不能被100整除的年份；②能够被400整除的年份。
列如：输入1900年，输出1900年不是闰年，输入2000年，输出2000年是闰年。'''
year=int(input('请输入年份：'))                     #输入年份
if (year%4==0 and year%100!=0) or year%400==0:     #判断是否为闰年
    print('该年是闰年。')                           #输出是闰年
else:                                              #否则
    print('该年不是闰年。')                         #输出不是闰年
