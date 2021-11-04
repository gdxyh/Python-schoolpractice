#新能源2001班 陆竟成 20411080104 5-3
'''斐波那契数列
若Fibonacci数列的第n项记为fib(a,b,n)，则有下列递归定义。
fib(a,b,1)=a
fib(a,b,2)=b
#已修改#fib(a,b,n)=fib(b,a+b,n+1)
用递归方法求值在5000之内的中，最大的一项。
'''
def fib(a,b,n):                                            #定义函数求斐波那契数列的值
    if n==1:                                               #当n为1时
        return a                                           #返回值为1
    elif n==2:                                             #当n为2时
        return b                                           #返回值为1
    else:                                                  #其它项
        return fib(a,b,n-1)+fib(a,b,n-2)                   #返回值为前一项加上前前项

n=1                                                        #n值默认为1（第一项）
while True:                                                #永远循环
    if fib(1,1,n)<=5000:                                   #判断值是否小于5000
        print(f'第{n}项为：{fib(1,1,n)}')                   #输出值
        n+=1                                               #数列项数加一
    else:                                                  #准备结束
        print(f'5000以内最大项为第{n-1}项：{fib(1,1,n-1)}') #输出结果
        break                                              #跳出循环
    