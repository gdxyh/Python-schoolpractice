#上机课一 练习题一 新能源2001班 陆竟成
'''输入三个浮点数，求他们的平均值并保留一位小数，输出结果。'''
a = float(input("请输入第一个浮点数："))                      #输入浮点数一
b = float(input("请输入第二个浮点数："))                      #输入浮点数二
c = float(input("请输入第三个浮点数："))                      #输入浮点数三
d = (a + b +c)/3                                             #计算平均值
print("平均值为（保留一位小数）：{0:.1f}".format(d))           #输出结果（保留一位小数）