'''
从键盘输入若干个数据建立一个字典，然后读取其键和值，并分别存入两个列表中。
'''
d,key,value,k={},[],[],''                      #预先定义所需的对象
def inkv():                                    #定义输入键值对函数
    """输入键值对"""
    global k,v                                 #使k,v变为全局变量（外部可调用）
    k=input('请输入关键字：')                   #输入k
    v=input('请输入值：')                       #输入v
    d.update({k:v})                            #将k,v添加到字典d中
while True:                                    #无停止的循环
    if k!='#=#':                               #设置停止字符
        inkv()                                 #调用函数
    else:                                      #其它情况下
        del d['#=#']                           #删除多余项
        break                                  #跳出循环
'''其它方法（需要预知数据个数，不适用）
n=int(input('请输入数据个数：'))                #输入数据个数
for i in range(n):                             #循环输入
    inkv()                                     #调用函数
#'''
for i in d.keys():                             #循环所有关键字
    key.append(i)                              #将所有关键字加入到列表key中
    value.append(d[i])                         #将所有值添加到列表value中
    '''
for j in d.values():                           #循环所有值
    value.append(j)                            #将所有值添加到列表value中
    '''
print(f'字典为{d}\n关键字为{key}\n值为{value}') #输出结果
