#mathmoudle
def prime(x):                #定义函数prime
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
