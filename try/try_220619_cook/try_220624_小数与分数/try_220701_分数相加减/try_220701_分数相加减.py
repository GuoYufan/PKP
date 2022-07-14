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


def 获取最小公倍数(a,b):
    c=获取最大公约数(a,b)
    
    #return a/c*b/c*c
    return int(a*b/c)

   
def 分数相加减(分数一,分数二,运算法):
    分子一,分母一=分数一[0],分数一[1]
    分子二,分母二=分数二[0],分数二[1]
    
    共同分母=获取最小公倍数(分母一,分母二)
    
    分子一变化=int(分子一*共同分母/分母一)
    分子二变化=int(分子二*共同分母/分母二)
    
    if 运算法=="+":
        分子和或差=分子一变化+分子二变化
    else:分子和或差=分子一变化-分子二变化
   
    return 获取最简分数(分子和或差,共同分母)


def 分数显示形式(分数):
    分子,分母=分数
    return f"{分子}/{分母}"
    
    
def 试用():
    while True:
        try:
            分数一=list(map(int,input("\n分数一:").split("/")))
            if len(分数一)==1:分数一.append(1)
            分数二=list(map(int,input("分数二:").split("/")))
            if len(分数二)==1:分数二.append(1)
            运算法=input("相加还是相减(+/-):")
        except:continue
        break
        
    分数一显示,分数二显示=list(map(分数显示形式,[分数一,分数二]))
    print("\n%s%s%s=%s"%(分数一显示,运算法,分数二显示,分数相加减(分数一,分数二,运算法)))


def main():
    while True:试用()


if __name__=="__main__":main()