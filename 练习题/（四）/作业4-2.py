# 新能源2001班 陆竟成 20411080104 4-2
'''输入一个随机长度为n的整数列表，n的值由用户输入。
(1)将列表中的偶数变成它的平方数，奇数保持不变，并分别统计奇数和偶数的个数。
(2)将奇数组成一个列表并按升序排序，将偶数组成一个列表并按降序排序。'''
n=int(input('请输入列表长度：'))              #输入列表长度
x,js,os=[],[],[]                             #定义空列表
a,b=0,0                                      #定义奇数偶数个数变量
for i in range(n):                           #循环n（列表长度）次
    x.append(int(input('请输入第{}个整数：'.format(i+1))))#输入列表内容
for i in range(n):                           #循环n（列表长度）次
    if x[i]%2==0:                            #判断是否为偶数
        x[i]=(x[i])**2                       #将偶数变为平方
        b+=1                                 #偶数计数加一
        os.append(x[i])                      #加入偶数列表
    else:                                    #其它情况（为奇数）
        a+=1                                 #奇数计数加一
        js.append(x[i])                      #加入奇数列表
js.sort()                                    #奇数列表升序排序
os.sort(reverse=True)                        #偶数列表降序排序
'''                                         #方法二：
for i in range(n):                           #循环n（列表长度）次
    if x[i]%2==0:                            #判断是否为偶数
        x[i]=(x[i])**2                       #将偶数变为平方
        b+=1                                 #偶数计数加一
        os.append(x[i])                      #加入偶数列表
    else:                                    #其它情况（为奇数）
        a+=1                                 #奇数计数加一
        js.append(x[i])                      #加入奇数列表
for i in range(len(js)-1):                   #奇数列表升序排序，控制比较轮数
    for j in range(i+1,len(js)):             #控制每轮比较的次数
        if js[i]>js[j]:                      #比较大小
            js[i],js[j]=js[j],js[i]          #排序
for i in range(len(os)-1):                   #偶数列表降序排序，控制比较轮数
    for j in range(i+1,len(os)):             #控制每轮比较的次数
        if os[i]<os[j]:                      #比较大小
            os[i],os[j]=os[j],os[i]          #排序
#'''                                         
print('处理后列表为{:}\n奇数个数为{:}\n偶数个数为{:}'.format(x,a,b))#输出
if a!=0:                                     #判断是否有奇数
    print('奇数列表为{:}'.format(js))         #输出奇数列表
if b!=0:                                     #判断是否有偶数
    print('偶数列表为{:}'.format(os))         #输出偶数列表
