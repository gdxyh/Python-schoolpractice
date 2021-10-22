#上级课二 练习题二 新能源2001班 陆竟成 20411080104
'''要求输入两个整型数据和一个算术运算符（+、-、* 、/、//或者% ），并对其进行指定的算术运算。
例如：输入10*3输出10*3=30；输入10#3输出# is not an operator。'''
a=int(input('请输入整数一：'))
b=int(input('请输入整数二：'))
x=input('请输入运算符号（+、-、* 、/、//或者% ）：')
if x=='+':
    c=a+b
    print(c)
elif x=='-':
    c=a-b
    print(c)
elif x=='*':
    c=a*b
    print(c)
elif x=='/':
    c=a/b
    print(c)
elif x=='//':
    c=a//b
    print(c)
elif x=='%':
    c=a%b
    print(c)
else:
    print(x,' is not an operator.')

'''
d=print('请输入计算式：')
print(eval(d))
'''