import math

from SearchPath import *
from try_Using_最大公约数 import *
from try_Using_分数相加减 import *


def 有限小数转分数(小数):
    整数部分=int(小数)
    小数位数=len(str(小数))-len(str(整数部分))-1
    if 小数位数<1 or 小数==整数部分:raise ValueError("❌你这不是小数")


    分数分部之分母=10**小数位数
    
#a=3.36
#b=str(a).split["."]
#b[1]
    小数部分=小数*分数分部之分母-整数部分*分数分部之分母
    分数分部之分子=int(小数部分)
    	
  
    约分后的分子,最终分母=分数约分((分数分部之分子,分数分部之分母))
    #根据分数整部分子变化
    最终分子=整数部分*最终分母+约分后的分子
    最终分数=f"{最终分子}/{最终分母}"
    
    return 最终分数


def 无限循环小数转分数_拆解(无限循环小数,循环体长度=1):
    循环体=str(无限循环小数)[-循环体长度:]
    
    a=无限循环小数
        
    #取出a的整数部分存进
    b=int(a)
    input(f"\n取出a的整数部分存进b:{b}")
    print(f"【整数部分:{b}】")
    
    #a从小数点后到首次循环体结束位共n位
    #即a的使用小数部分共n位
    n=len(str(a))-len(str(b))-1
    #n=len(str(a).split(".")[-1])
    input(f"a从小数点后到首次循环体结束位共n位: {n}")
    
    #取出a的使用小数部分的整数形式存进c
    #（或字符串形式）
    
    #c整数形式之数值计算法（默认）
    c=math.ceil(a*10**n-b*10**n)
    
    #c整数形式之字符串切片法
    #c=int(str(a).split(".")[-1])
    
    input(f"取出a的使用小数部分的整数形式存进c: {c}")
    
    #循环体的字符串形式为d（循环体应当是字符串形式 因为存在头位为0的情况）
    #而且万物本质在于字符串
    d=循环体
    input(f"循环体的字符串形式为d: {repr(d)}")
    
    #首次循环体与小数点之间的空即距离即空位为e
    e=int(n-循环体长度)
    是否有空位=True if e else False
    input(f"首次循环体与小数点之间的空即距离即空位为e: {e}")
   
    # 由空位得出的需要缩小的倍数为f（根据空位e）
    # 空部不被填时循环部分需要缩小的倍数（从而不填空）
    f=10**e
    input(f"需要缩小的倍数为f（根据e）: {f}")
    
    
    # 空部不被填时循环部分需要减小的数值的分数形式（从而不填空）
    # 这时可能增加空（故不推荐用）
    f_substract="%s/%s"%(int(循环体),f) if 是否有空位 else "0"
    input("空部不被填时循环部分需要减小的数值的分数形式为f_substract:"
    	f"{repr(f_substract)}")
    
    # f_substract的最简分数形式
    f_substract=获取最简分数(f_substract) if 是否有空位 else "0"
    input(f"f_substract的最简分数形式: {repr(f_substract)}")
    
    
    #由循环体得到的分数部分的字符串形式为g
    g=f"{循环体}/{str(9)*循环体长度}"
    input(f"由循环体得到的分数部分的字符串形式为g: {repr(g)}")
   	
    g=获取最简分数(g)
    input(f"g的最简分数形式为g: {repr(g)}")
    print(f"【循环部分:{g}】")
    
    #首次循环体与小数点之间的空部拆解出来的有限整数的整数形式为h
    #（或字符串形式）    
    #h整数形式之相减法之全位（默认）
    h_整数形式之相减法_全位=int(c-int(循环体))
    input("首次循环体与小数点之间的空部拆解出来的有限整数的整数形式为h\n"
    f"h整数形式之相减法之全位: {h_整数形式之相减法_全位}")
    print("【%s-%s】"%(c,循环体)) 
    
    #h整数形式之相减法    
    h=h_整数形式之相减法=(c-int(d))//(10**循环体长度)
    input(f"h整数形式之相减法（默认）: {h}")
    print("【(%s-%s)//%s】"%(c,循环体,10**循环体长度)) 
     
    #h整数形式之数值截取法（与之不同 字符串截取法是切片）
    #循环体长度等于n-e
    h_整数形式之数值截取法=c//(10**(n-e))
    input(f"h整数形式之数值截取法: {h_整数形式之数值截取法}")
    print("【%s从头向尾只留%s位】"%(c,e))
    
    #h整数形式之字符串切片法
    #h=int(str(c)[:-e])
    
    #空部拆解出来的整数形式h进行还原
    #方法是以h作为分子 分母为10的n次方 得到这样的分数形式
    #然后得到这分数的最简分数形式的字符串形式
    #从而还原为i
    
    #当使用h整数形式之相减法之全位来进行还原为i
    i_相减法_全位=f"{h_整数形式之相减法_全位}/{10**n}" if h!=0 else "0"
    input(f"空部拆解出来的整数形式h进行还原为i\n"
    f"i字符串形式之当h使用相减法之全位: {repr(i_相减法_全位)}")

    #当使用h整数形式之相减法来进行还原为i（默认）
    i=i_相减法=f"{h}/{f}" if h!=0 else "0"
    input(f"i字符串形式之当h使用相减法（默认）: {repr(i)}")
        
    #当使用h整数形式之数值截取法来进行还原为i
    i_数值截取法="%s/%s"%(h_整数形式之数值截取法,f)\
if h_整数形式之数值截取法!=0 else "0"
    input(f"i字符串形式之当h使用数值截取法: {repr(i_数值截取法)}")
        
    i=获取最简分数(i) if h!=0 else "0"
    input(f"空部h还原成的分数的最简分数形式的字符串形式为i: {repr(i)}")
    print(f"【空部:{i}】")
    
    # 空部被填为j
    # 使用额外函数的方法
    j=分数相加减(i,f_substract,"-") if 是否有空位 else "0"
    input(f"空部被填为j（已化简）（非我哲学法）: {repr(j)}")
    
    # 符合我哲学的 不使用额外函数的方法
    j="%s/%s"%(h-int(循环体),f) if 是否有空位 else "0"
    input(f"空部被填为j（未化简）（是我哲学法）: {repr(j)}")
    
    # j的最简分数形式
    j=获取最简分数(j) if 是否有空位 else "0"
    input(f"j的最简分数形式（是我哲学法）: {repr(j)}")
    
    return (b,i,g),(f,f_substract,j)
    
    
def 无限循环小数转分数(无限循环小数,循环体长度=1):
    #0.8333...=0.5+0.333...
    
    基础,附加=无限循环小数转分数_拆解(无限循环小数,循环体长度)
    
    整数部分,空部,循环部分=基础
    空部不填_倍数缩小,空部不填_数值减小,空部被填=附加
    
    result_空部不填_数值减小=result_空部不填_倍数缩小=\
    result_空部不填_模板="%s+%s+%s"%(整数部分,空部,循环部分)
    
    result_空部不填_倍数缩小+="/%s"%(空部不填_倍数缩小)
    result_空部不填_数值减小+="-%s"%(空部不填_数值减小)
    result_空部被填="%s+%s+%s"%(整数部分,空部被填,循环部分)
    
    description=(
    	"方法一（空部不填之倍数缩小法）:",
    	"方法二（空部不填之数值减小法）:",
    	"方法三（空部被填法）（推荐）:",
    	)
    
    整合=zip(description,(
    	           result_空部不填_倍数缩小,
    		          result_空部不填_数值减小,
    		          result_空部被填,
    		          ))
    		
    return 整合


def 设置你的循环体长度界面():
    循环体长度=1
    while True:
        答=input("\n设置你的循环体长度(Enter:默认值)(默认值:1):")
        if not 答:break       
        try:循环体长度=int(答)
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
    try:print("\n%s的分数形式是%s"%(你的小数,有限小数转分数(你的小数)))
    except Exception as e:
        print(e)
        return
        
    if 循环体长度:
        print("\n%s%s...的分数形式是"%(你的小数,str(你的小数)[-循环体长度:]*2))
        for k,v in 无限循环小数转分数(你的小数,循环体长度):
            print(k,v)


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

#updated: 2022.7.17 0:36~1:52
#《try_220624_0717_v12_小数转分数.py》
