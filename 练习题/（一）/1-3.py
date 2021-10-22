#练习题三
'''随机生成一个3位数，将它的十位数变成0。例如，生成234，输出则为204。'''
import random                              #导入random库
x = random.randint(100,999)                #随机生成三位数
a = int(x/100)                             #提取百位
b = int(x%10)                              #提取个位
c = 100*a + b                              #重组数据
print("随机生成的数为：{0:}".format(x))     #输出随机生成的树
print("提取的百位数为：{0:}".format(a))     #输出百位数
print("提取的个位数为：{0:}".format(b))     #输出个位数
print("结果为：{0:}\n".format(c))           #输出结果
