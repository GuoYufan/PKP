def 获取最大公约数(a,b):
    #这里要加括号形成元组 不然被逗号分隔了
    #如此 右操作数有三个 左边只有两个 就对不上了  
    smaller,bigger=(a,b) if a<=b else (b,a)
    
    while True:
        now=bigger%smaller
        if now==0:break
        bigger,smaller=smaller,now

    return smaller

def 获取最简分数(a,b):
    最大公约数=获取最大公约数(a,b)
    分子约分后=a//最大公约数
    分母约分后=b//最大公约数
    
    return f"{分子约分后}/{分母约分后}"


def 试用():
    while True:
        try:
            a=int(input("\nnum1:"))
            b=int(input("num2:"))
        except:continue
        break
    print("\n%s和%s的最大公约数是%s"%(a,b,获取最大公约数(a,b)))
    print("最简分数是%s"%获取最简分数(a,b))

def main():
    while True:试用()
    
    
if __name__=="__main__":main()