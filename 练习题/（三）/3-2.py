#上级课三 练习题二
for x in range(100,1000):                                       #让x值为100到999并循环
    if x//9==(x//100)**2+((x-100*(x//100))//10)**2+(x%10)**2:   #比较x被九整除的数是否等于各位数字的平方和
        print(x)                                                #输出满足条件的数
