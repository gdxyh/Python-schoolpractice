#上级课二 练习题三 新能源2001班 陆竟成 20411080104
'''输入三个数，判断他们能否组成三角形，若能，则输出三角形是等腰三角形、等
边三角形、直角三角形还是普通三角形，若不行，则输出不能组成三角形。'''
a=float(input('请输入第一个数（第一边）：'))
b=float(input('请输入第二个数（第二边）：'))
c=float(input('请输入第三个数（第三边）：'))
if (a+b>c or a+c>b or b+c>a):
    if (a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2):
        print('直角三角形')
    elif (a==b or a==c or b==c) and (a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2) :
        print('等腰直角三角形')
    elif a==b or a==c or b==c :
        print('等腰三角形')
    elif a==b==c :
        print('等边三角形')
    else :
        print('普通三角形')
else:
    print('不能组成三角形')

