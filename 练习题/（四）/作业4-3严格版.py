#4-3 严格版（未完成）
'''输入5×5矩阵A，完整下列操作：
(1)输出矩阵A。
(2)将第二行和第五行元素对调后，输出新的矩阵A1。
(3)用对角线上的各元素分别去除各元素所在行，输出新的矩阵A2。'''
a,b,c,d,e=[],[],[],[],[]                                                       #定义矩阵A的五行列表
x=[a,b,c,d,e]                                                                  #定义矩阵A(命名为x)
h=''                                                                           #定义空字符串h
for i in range(len(x)):                                                        #每个列表循环一次（对应每行）
    for j in range(5):                                                         #每行循环5次（对应每列）
        #'''调试数据
        h=float(i+j)
        x[i].append(float(format(h,'.2f')))
        #'''
        #'''正式数据
        h=input('请输入第{}行第{}列数字：'.format(i+1,j+1))                     #输入数据
        if h.isdigit():                                                        #判断是否为数字
            pass                                                               #不执行（本次判断结束）
        else :                                                                 #不是数字
            while h.isdigit() is False:                                        #直到h为数字停止循环
                h=input('请输入第{}行第{}列数字！\n重新输入：'.format(i+1,j+1))  #重新输入数据
        x[i].append(float(h))                                                  #将元素添加进列表（矩阵）
        #'''

        '''简化输入                                                             #（失败）
        while h.isdigit() is False:                                            #
            h=input('请输入数字！\n重新输入：')                                  #
        x[i].append(float(h))                                                  #将元素添加进列表（矩阵）
        #'''

for i in x:                                                                    #输出矩阵A
    print(i)                                                                   #输出矩阵A
print()                                                                        #换行

s=[a,e,c,d,b]                                                                  #定义矩阵A1为矩阵A第二行和第五行元素对调
for i in s:                                                                    #输出矩阵A1
    print(i)                                                                   #输出矩阵A1
print()                                                                        #换行

f=[a,b,c,d,e]                                                                  #定义新矩阵A2
for i in range(len(f)):                                                        #处理原矩阵A的数据
    f[i][i]=float(format((f[i][i])/(i+1),'.1f'))                                                    #斜率为负的对角线上的数除以行数
    if i != 2:                                                                 #跳过两条对角线的相交处，防止重复作除
        f[i][len(f)-1-i]=float(format((f[i][len(f)-1-i])/(i+1),'.1f'))                              #斜率为正的对角线上的数除以行数
    print(f[i])                                                                #输出矩阵A2
