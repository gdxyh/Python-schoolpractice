#上级课三 练习题一 新能源2001班 陆竟成 20411080104
#求素数
import math                    #导入math函数
n=0                            #定义n的值为0
for m in range(101,201,2):     #取m为从201到200的奇数并循环
    k=int(math.sqrt(m))        #求m的平方根取整k
    for i in range(2,k+2):     #取i为从2到k+1
        if m%i==0:break        #当m除以i为整数时停止并跳出循环
    if i==k+1:                 #如果i=k+1时接着运行
        if n%10==0:print()     #如果n能被10整除则换行
        print(m,end='')        #输出素数
        n+=1                   #n的值加1
