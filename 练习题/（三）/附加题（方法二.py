##上级课三 练习题（附加题） 新能源2001班 陆竟成 20411080104
'''求1+2+3+……+x的值'''
x=int(input())             #输入x
s=0                        #定义和s为0
for i in range(1,x+1):     #将数从1到X循环
    s+=i                   #将每一个数加到和s
print(s)                   #输出和s
