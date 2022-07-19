from SearchPath import *
from try_Using_最大公约数 import *


def 获取最小公倍数(a,b):
    c=获取最大公约数(a,b)
    
    #return a/c*b/c*c
    return int(a*b/c)


#分数在字符串形式与列表形式之间的转换
def 分数形式转换(分数,转换为=list):
    if type(分数)==转换为:return 分数
    
    if isinstance(分数,list) and 转换为==str:
        return "/".join(map(str,分数))
    elif isinstance(分数,str) and 转换为==list:
        return list(map(int,分数.split("/")))
    
    raise TypeError("❌无法转换")
    

def 分数相加减(分数一,分数二,运算法="+",是否化简=True):
    分数一,分数二=map(分数形式转换,(分数一,分数二))
    
    分子一,分母一=分数一[0],分数一[1]
    分子二,分母二=分数二[0],分数二[1]
    
    共同分母=获取最小公倍数(分母一,分母二)

    分子一变化为=int(分子一*共同分母/分母一)
    分子二变化为=分子二*共同分母//分母二
    
    分子和或差=分子一变化为+分子二变化为 if 运算法=="+" else 分子一变化为-分子二变化为
    
    result=f"{分子和或差}/{共同分母}"
    
    return 获取最简分数(result) if 是否化简 else result


def 分数显示形式(分数):
    分子,分母=分数
    return f"{分子}/{分母}"
    
    
def 试用():
    while True:
        try:
            分数一=list(map(int,input("\n分数一:").split("/")))
            if len(分数一)==1:分数一.append(1)
        except:continue
        try:
            分数二=list(map(int,input("分数二:").split("/")))
            if len(分数二)==1:分数二.append(1)
        except:continue
        try:运算法=input("相加还是相减(+/-):")
        except:continue
        break
        
    分数一显示,分数二显示=map(分数显示形式,(分数一,分数二))
    print("\n%s%s%s=%s"%(分数一显示,运算法,分数二显示,分数相加减(分数一,分数二,运算法)))


def main():
    while True:试用()


if __name__=="__main__":main()
