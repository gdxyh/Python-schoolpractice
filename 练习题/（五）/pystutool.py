#判断x是否为素数
def prime(x):
    """判断x是否为素数"""
    if x<2:                  #当x<2时，无素数
        return False         #返回（False）
    elif x==2:               #当x=2时
        return True          #返回真（True）
    else:                    #其它
        for i in range(2,x): #循环相除比较
            if x%i==0:       #验证算法是否有误
                return False #返回假（False）
                break        #打破循环
        else:                #其它情况
            return True      #返回真（True）
#判断x是否为完数
def perfectnum(x):
    """判断x是否为完数"""
    s=0                      #声明变量s
    for i in range(1,x):     #生成数字i（除数）（x为被除数）
        if x%i==0:           #如果x能被i整除，i就是因子
            s=s+i            #和s为s加i，回循环
    if x==s:                 #如果和s=原数x
        return True          #返回真（True）
    else:                    #其它情况
        return False         #返回假（False）
#求x的所有因子
def factor(x):
    factor=[]
    """求x的所有因子"""
    for i in range(1,x):     #生成数字i（除数）（x为被除数）
        if x%i==0:           #如果x能被i整除，i就是因子
            factor.append(i) #将因子加入到因子列表中
    return factor            #返回因子列表

