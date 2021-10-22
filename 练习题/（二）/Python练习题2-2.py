#上级课二 练习题二
'''要求输入两个整型数据和一个算术运算符（+、-、* 、/、//或者% ），并对其进行指定的算术运算。
例如：输入10*3输出10*3=30；输入10#3输出# is not an operator。'''
a=int(input('请输入整数一：'))                           #输入整数一
b=int(input('请输入整数二：'))                           #输入整数二
x=input('请输入运算符号（+、-、* 、/、//或者% ）：')     #输入运算符号
#解法一                                                  #解法一
if x in ['+','-','*','/','//','%']:                      #如果运算符号是+,-,*,/,//,%
    c=eval('{}{}{}'.format(a,x,b))                       #运算
    print('{0}{1}{2}={3}'.format(a,x,b,c))               #输出结果
else:                                                    #否则
    print(x,' is not an operator.')                      #输出不是运算符号
#解法二                                                  #解法二
if x=='+':                                               #判断运算符号
    c=a+b                                                #运算
    print('{0}{1}{2}={3}'.format(a,x,b,c))               #输出结果
elif x=='-':                                             #判断运算符号
    c=a-b                                                #运算
    print('{0}{1}{2}={3}'.format(a,x,b,c))               #输出结果
elif x=='*':                                             #判断运算符号
    c=a*b                                                #运算
    print('{0}{1}{2}={3}'.format(a,x,b,c))               #输出结果
elif x=='/':                                             #判断运算符号
    c=a/b                                                #运算
    print('{0}{1}{2}={3}'.format(a,x,b,c))               #输出结果
elif x=='//':                                            #判断运算符号
    c=a//b                                               #运算
    print('{0}{1}{2}={3}'.format(a,x,b,c))               #输出结果
elif x=='%':                                             #判断运算符号
    c=a%b                                                #运算
    print('{0}{1}{2}={3}'.format(a,x,b,c))               #输出结果
else:                                                    #否则
    print(x,' is not an operator.')                      #输出不是运算符号
