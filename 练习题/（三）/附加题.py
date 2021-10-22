##上级课三 练习题（附加题）
'''求1+2+3+……+x的值'''
x=int(input())             #输入x
#方法一
if x%2==0:                 #x为偶数
    y=(x/2)*(x+1)          #计算和
else:                      #x为奇数
    y=((x-1)/2)*x+x        #计算和y
print('{:.0f}'.format(y))  #输出和y
#方法二
s=0                        #定义和s为0
for i in range(1,x+1):     #将数从1到X循环
    s+=i                   #将每一个数加到和s
print(s)                   #输出和s
