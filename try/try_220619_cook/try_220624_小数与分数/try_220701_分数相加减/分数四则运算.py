from SearchPath import *
from try_Using_最大公约数 import *
from functools import reduce

def 获取最小公倍数(a,b):
    try:c=获取最大公约数(a,b)
    except Exception as e:
        print(e)
        return
    
    #return a/c*b/c*c
    return int(a*b/c)


def 是否形如分数(分数):
    if not 分数:return False
    if isinstance(分数,str):
        分数的字符串列表形式=分数.split("/")
    elif isinstance(分数,list):
        分数的字符串列表形式=[ str(_) for _ in 分数]
    else:return False
    
    input(分数的字符串列表形式)
     
    if len(分数的字符串列表形式)<=1 or str() in 分数的字符串列表形式:
        return False
    try:list(map(int,分数的字符串列表形式))
    except:return False
    
    return True
    
    

def 分数转列表形式(原分数的字符串形式):
    if isinstance(原分数的字符串形式,(list,tuple)):return 原分数的字符串形式
    if not isinstance(原分数的字符串形式,str):
        raise TypeError("must be str,not",\
type(原分数的列表形式).__name__)
    try:return list(map(int,原分数的字符串形式.split("/")))
    except:
        raise ValueError("❌不支持非整数分子分母\n")


def 分数转字符串形式(原分数的列表形式):
    if isinstance(原分数的列表形式,str):return 原分数的列表形式
    if not isinstance(原分数的列表形式,(list,tuple)):
        raise TypeError("must be list or tuple,not",\
type(原分数的列表形式).__name__)
    try:return "/".join(map(str,原分数的列表形式))
    except:
        raise ValueError("❌不支持非整数分子分母\n")

        
#分数在字符串形式与列表形式之间的转换
def 分数形式转换(分数):
    if isinstance(分数,list):
        try:return 分数转字符串形式(分数)
        except Exception as e:print(e)
    elif isinstance(分数,str):
        try:return 分数转列表形式(分数)
        except Exception as e:print(e)
    
    raise TypeError("❌无法转换\n")


def multiply(x,y):
    x,y=map(int,(x,y))
    return x*y


# 支持任意形式输入，限定输出字符串形式
def 连分数转换(连分数):
    if isinstance(连分数,str):
        连分数_列表形式=连分数.split("/")
    else:连分数_列表形式=连分数
        
    分子=连分数_列表形式[0]
    分母=reduce(multiply,连分数_列表形式[1:])
    return f"{分子}/{分母}"

                
def 使分数以标准显示(原分数的任意形式):
    try:原分数的列表形式=分数形式转换(原分数的任意形式) if\
not isinstance(原分数的任意形式,list) else 原分数的任意形式    
    except Exception as e:
        print(e)
        raise Exception("❌分数有误 请检查\n")
        
    if len(原分数的列表形式)==1:
        原分数的列表形式.append(1)
    if len(原分数的列表形式)>2:
        原分数的列表形式=连分数转换(原分数的列表形式).split("/")
    
    return 分数形式转换(原分数的列表形式)

    
def 分数四则运算(分数一,分数二,运算法="+",是否化简=True):
    if 运算法 not in ("+","-","*","/"):
        raise Exception("❌arg '运算法' is not be surpported.\n")
    
    分数一,分数二=map(使分数以标准显示,(分数一,分数二))
    
    分子一,分母一=分数形式转换(分数一)
    分子二,分母二=分数形式转换(分数二)
    
    if 0 in (分母一,分母二):
        raise ValueError("❌分母不能为0\n")
    
    if 运算法 in ("+","-"):
        共同分母=获取最小公倍数(分母一,分母二)

        分子一变化为=int(分子一*共同分母/分母一)
        分子二变化为=分子二*共同分母//分母二
    
        分子和或差=eval(str(分子一变化为)+运算法+str(分子二变化为))
    
        result=f"{分子和或差}/{共同分母}"
        
    elif 运算法 == "*":
        最终分母=分母一*分母二
        最终分子=分子一*分子二
        result=f"{最终分子}/{最终分母}"
    
    elif 运算法 == "/":
        最终分母=分母一*分子二
        最终分子=分子一*分母二
        result=f"{最终分子}/{最终分母}"
    
    return 获取最简分数(result) if 是否化简 else result



def 分数显示形式(分数):
    分子,分母=分数
    return f"{分子}/{分母}"
    
    
def 试用():
    while True:
        try:
            分数一=list(map(int,input("◾️分数一:").split("/")))
        except:
            print("❌分数有误 请检查\n")
            continue
        分数一=使分数以标准显示(分数一)
        分数一=分数形式转换(分数一)
        if 分数一[1]==0:
            print("❌分母不能为0\n")
            continue
        
        try:
            分数二=list(map(int,input("◾️分数二:").split("/")))
        except:
            print("❌分数有误 请检查\n")
            continue
        分数二=使分数以标准显示(分数二)
        分数二=分数形式转换(分数二)
        if 分数二[1]==0:
            print("❌分母不能为0\n")
            continue
        
        运算法=input("◾️四则运算(+/-/*//):")
        break
        
    分数一显示,分数二显示=map(分数显示形式,(分数一,分数二))
    try:分数四则运算结果=分数四则运算(分数一,分数二,运算法)
    except Exception as e:
        print(e)
        return
        
    if 运算法=="/":分数二显示=分数二显示.join("()")
    print("\n%s%s%s=%s\n"%(分数一显示,运算法,分数二显示,分数四则运算结果))
    

def main():
    while True:试用()


if __name__=="__main__":main()

# updated:2025.1.22 15:21
# 《分数相加减》修复了一些问题，加强了功能，优化了使用体验
