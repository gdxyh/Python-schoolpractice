#新能源2001班 陆竟成 20411080104 5-2
'''
求100以内的全部素数，每行输出10个。要求定义和调用函数prime(m)判断m是否为素数.
'''

from mathmoudle import *            #导入mathmoudle
j=0                                 #使j（控制长度）为零
for i in range(1,101):              #循环，使i从1到100
    if prime(i)==True:              #调用函数，比较素数
        print(f'{i}为素数',end=' ') #输出素数
        j+=1                        #记录次数加一
    if j==10:                       #当j=10时
        print()                     #换行
        j=0                         #j再次归零
