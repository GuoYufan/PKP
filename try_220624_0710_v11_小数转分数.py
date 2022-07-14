import math

def 获取最大公约数(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError("must be int")
    
#这里要加括号形成元组 不然被逗号分隔了
#如此 右操作数有三个 左边只有两个 就对不上了      
    smaller,bigger=(a,b) if a<=b else (b,a)
    
    while True:
        now=bigger%smaller
        if now==0:break
        bigger,smaller=smaller,now
    
    return smaller


def 小数转分数(小数):
    取出整数部分=int(小数)
    小数位数=len(str(小数))-len(str(取出整数部分))-1
    if 小数位数<1 or 小数==取出整数部分:raise ValueError("❌你这不是小数")


    分数分部之分母=10**小数位数
    
#a=3.36
#b=str(a).split["."]
#b[1]
    取出小数部分=小数*分数分部之分母-取出整数部分*分数分部之分母
    分数分部之分子=int(取出小数部分)
    	
    分子分母最大公约数=获取最大公约数(分数分部之分子,分数分部之分母)
  
    约分后的分子=分数分部之分子//分子分母最大公约数
    
    最终分母=约分后的分母=分数分部之分母//分子分母最大公约数
    最终分子=根据分数整部分子要变化成=取出整数部分*最终分母+约分后的分子
    最终分数字符串=f"{最终分子}/{最终分母}"
    
    return 最终分数字符串


#单参数版——接收分数的字符串形式版——返回同形式
def 获取最简分数(原分数的字符串形式):
    原分子,原分母=tuple(map(int,原分数的字符串形式.split("/")))
    最大公约数=获取最大公约数(原分子,原分母)
    分子约分后=原分子//最大公约数
    分母约分后=原分母//最大公约数
    
    return f"{分子约分后}/{分母约分后}"

#单参数版——接收分数的列表形式版——返回同形式
def 分数约分(分数):
    分数=list(map(int,分数))
    a=获取最大公约数(分数[0],分数[1])
    最终约分后字符串列表=[str(int(i/a)) for i in 分数]
    
    return 最终约分后字符串列表


def 获取最小公倍数(a,b):
    c=获取最大公约数(a,b)
    
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
    
    return f"{分子和或差}/{共同分母}"


def 无限循环小数转分数_拆解(无限循环小数,循环体长度=1):
    循环体=str(无限循环小数)[-循环体长度:]
    
    a=无限循环小数
        
    #取出a的整数部分存进b
    b=int(a)
    #input(b)
    
    #a从小数点后到首次循环体结束位共n位
    #即a的使用小数部分共n位
    n=len(str(a))-len(str(b))-1
    #n=len(str(a).split(".")[-1])
    input(f"\na从小数点后到首次循环体结束位共n位: {n}")
    
    #取出a的使用小数部分的整数形式存进c
    #（或字符串形式）
    
    #c整数形式之数值计算法（默认）
    c=math.ceil(a*10**n-b*10**n)
    
    #c整数形式之字符串切片法
    #c=int(str(a).split(".")[-1])
    
    input(f"取出a的使用小数部分的整数形式存进c: {c}")
    
    #循环体的字符串形式为d（循环体应当是字符串形式 因为存在头位为0的情况）
    #而且万物本质在于字符串
    d=str(a)[-循环体长度:]
    input(f"循环体的字符串形式为d: {d}")
    
    #首次循环体与小数点的之间的空即距离为e
    e=n-循环体长度
    input(f"首次循环体与小数点的之间的空即距离为e: {e}")
    
    #需要缩小的倍数为f
    f=10**e
    input(f"需要缩小的倍数为f: {f}")
    
    #由循环体得到的分数部分的字符串形式为g
    g=f"{循环体}/{str(9)*循环体长度}"
    input(f"由循环体得到的分数部分的字符串形式为g: {g}")
   	
    g=获取最简分数(g)+\
    (f"/{f}" if f!=1 else str())
    input(f"g的最简分数形式为g: {g}")
    
    
    #首次循环体与小数点之间的空部拆解出来的有限整数的整数形式为h
    #（或字符串形式）    
    #h整数形式之相减法（默认）
    h=h_整数形式之相减法=int(c-int(d))    
    input("首次循环体与小数点之间的空部拆解出来的有限整数的整数形式为h\n"
    f"h整数形式之相减法（默认）: {h}")        
    #h整数形式之数值截取法（与之不同 字符串截取法是切片）
    print("【%s-%s】"%(c,d))
    h_整数形式之数值截取法=c//(10**(n-e))
    input(f"h整数形式之数值截取法: {h_整数形式之数值截取法}")
    print("【%s从头向尾只留%s位】"%(c,e))
    
    #h整数形式之字符串切片法
    #h=int(str(c)[:-e])
    
    #空部拆解出来的整数形式h进行还原
    #方法是以h作为分子 分母为10的n次方 得到这样的分数形式
    #然后得到这分数的最简分数形式的字符串形式
    #从而还原为i
    
    #当使用h整数形式之相减法（默认）
    i=i_相减法=分数约分([h,10**n]) if h!=0 else 0
    input(f"空部拆解出来的整数形式h进行还原为i\n"
    f"i字符串列表形式之当h使用相减法（默认）: {i}")
    
    #当使用h整数形式之数值截取法
    i_数值截取法=分数约分([h_整数形式之数值截取法,10**e]) if h_整数形式之数值截取法!=0 else 0
    input(f"i字符串列表形式之当h使用数值截取法: {i_数值截取法}")
    
    
    i="/".join(i) if h!=0 else 0
    input(f"空部h还原成的分数的最简分数形式的字符串形式为i: {i}")
    
    return b,i,g
    
    
def 无限循环小数转分数(无限循环小数,循环体长度=1):
    #0.8333...=0.5+0.333...    
    
    整数部分,空部,循环部分=无限循环小数转分数_拆解(无限循环小数,循环体长度)
    0
    return "%s+%s+%s"%(整数部分,空部,循环部分)


def 设置你的循环体长度界面():
    循环体长度=1
    while True:
        回答=input("\n设置你的循环体长度(Enter:默认值)(默认值:1):")
        if not 回答:break       
        try:循环体长度=int(回答)
        except:continue
        if 循环体长度<0:
            print("❌循环体长度不能小于0")
            continue
        break
        
    return 循环体长度


def 问你的小数界面():
    while True:
        try:你的小数=float(input("\n你的小数是？\n答:"))
        except:continue
        break
        
    return 你的小数

def 给出解答界面(你的小数,循环体长度):        
    try:print("\n%s的分数形式是%s"%(你的小数,小数转分数(你的小数)))
    except Exception as e:
        print(e)
        return
        
    if 循环体长度:
        print("\n%s%s...的分数形式是%s"%(你的小数,str(你的小数)[-循环体长度:]*2,无限循环小数转分数(你的小数,循环体长度)))
    

def 是否退出当前界面():
    if input("\n#Q/q to quit: ").lower()=="q":
        return True
    return False

def 试用():
    #print(分数相加减([1,5],[1,108],"-"))
    #input()
    
    循环体长度=设置你的循环体长度界面()
    while True:   
        while True:
            你的小数=问你的小数界面()
            给出解答界面(你的小数,循环体长度)
            if 是否退出当前界面():break
            
        循环体长度=设置你的循环体长度界面()
        if 是否退出当前界面():break


def 初始界面():
    while True:
        input("\n😋\n这里是初始界面")
        if 是否退出当前界面():break
        试用()

        
def main():
    初始界面()



if __name__=="__main__":main()


#625/3276=1/5+1/108+...

#updated: 2022.7.10 18:46~
#《try_220624_0710_v11_小数转分数.py》
