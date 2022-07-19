def 获取最大公约数(a,b):
    if 0 in (a,b):
        raise TypeError("❌计算最大公约数的两个数中任何一个不能是0")
    #这里要加括号形成元组 不然被逗号分隔了
    #如此 右操作数有三个 左边只有两个 就对不上了  
    smaller,bigger=(a,b) if a<=b else (b,a)
    
    while True:
        remainder=bigger%smaller
        if remainder==0:break
        bigger,smaller=smaller,remainder

    return abs(smaller)


#单参数版（常用）——接收分数的字符串形式版——返回同形式
def 获取最简分数(原分数的字符串形式):
    原分子,原分母=map(int,原分数的字符串形式.split("/"))
    
    最大公约数=获取最大公约数(原分子,原分母)
    
    分子约分后=原分子//最大公约数
    分母约分后=原分母//最大公约数
    
    return f"{分子约分后}/{分母约分后}"

    
def 获取最简分数_多参版(原分子,原分母):
    原分数的字符串形式="/".join(map(str,(原分子,原分母)))
    
    return 获取最简分数(原分数的字符串形式)
    

#单参数版——接收分数的列表形式版——返回同形式
def 分数约分(原分数的列表形式):
    最简分数的字符串形式=获取最简分数("/".join(map(str,原分数的列表形式)))
    分数约分后的字符串列表形式=最简分数的字符串形式.split("/")
    
    return 分数约分后的字符串列表形式


def 试用():
    while True:
        try:
            a=int(input("\nnum1:"))
            b=int(input("num2:"))
        except:
            print("❌暂不支持非整数")
            continue
        if 0 in (a,b):
            print("❌计算最大公约数的两个数中任何一个不能是0")
            continue
        break
    print("\n%s和%s的最大公约数是%s"%(a,b,获取最大公约数(a,b)))
    #print("最简分数是%s"%获取最简分数(f"{a}/{b}"))
    print("最简分数是%s"%获取最简分数_多参版(a,b))
    #print("最简分数是%s"%分数约分((a,b)))



def main():
    while True:试用()
    
    
if __name__=="__main__":main()
