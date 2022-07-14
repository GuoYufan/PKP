import sys
sys.path.append(
	"/sdcard/[PKP]/common/module/"
	"PKP/Stay/AmusementPark")
del sys
from PKP_color import 颜色,上色,取色
#input(颜色.五颜六色)
#input(dir(颜色))
#help(上色)


调色板={True:"红",
False:"蓝"}


import decimal as dcm
from copy import copy

    
def 找出下一个与末位数字相同的数字的位置(对它找):
    当前搜索位置=末位-2
    while True:
        if abs(当前搜索位置)>小数部分位数:
            print("❗️搜索已到尽头")
            break              
        if 对它找[当前搜索位置]==末位上的数字:
            yield 当前搜索位置
        当前搜索位置-=1


def 判断当前抓取片段是否为循环体(对它找,当前抓取片段,当前抓取片段首位):
    无法容纳下一个想象片段=Exception("❗️无法容纳下一个想象片段")        	

   	
    下一个想象片段末位=当前抓取片段首位-1
    print("◾️下一个想象片段末位:",下一个想象片段末位)
    #input()
    
    下一个想象片段长度=len(当前抓取片段)
    print("◾️下一个想象片段长度:",下一个想象片段长度)
    #input()
    
    下一个想象片段首位=下一个想象片段末位-下一个想象片段长度+1
    print("◾️下一个想象片段首位:",下一个想象片段首位)
    #input()

    下一个想象片段=对它找[下一个想象片段首位:下一个想象片段末位+1]
    if len(下一个想象片段)!=下一个想象片段长度:
        raise 无法容纳下一个想象片段
    else:
        print("◾️下一个想象片段:",上色(下一个想象片段,"蓝"))
        #input()
    
    if 下一个想象片段==当前抓取片段:return True
    
    return False
    

def 找出最终循环体():
    还需要填几个空=abs(小数点后第一位-(当前抓取片段首位-首次循环体长度))
    print("\n⭐️原本还需要填几个空:",还需要填几个空)
    if 还需要填几个空>首次循环体长度:
        还需要填几个空=小数部分位数%首次循环体长度
        print("⭐️（但自身可没那么长 所以）实际还需要填几个空:",还需要填几个空)
    #input()
    
    头部填空部分=首次循环体[-还需要填几个空:None]
    尾部保留部分=首次循环体[None:-还需要填几个空]
    print("⭐️头部填空部分:",头部填空部分)
    #input()
    print("⭐️尾部保留部分:",尾部保留部分)
    #input()
    
    最终循环体=头部填空部分+尾部保留部分
    return 最终循环体


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



def 非默认给出模式之进行一():
    分子=6
    
    残存者=[11]
    
    while True:
        回答=input("\n❓"+上色("你的分子是？(Enter:默认值)\n答:","重点黑"))
        if not 回答:break
        try:分子=dcm.Decimal(回答)
        except:continue
        break
    
    while True:
        回答=input("\n❓"+上色("你的残存者是？(Enter:默认值)\n答:","重点黑"))
        if not 回答:break
        try:残存者=list(map(dcm.Decimal,回答.split()))
        except:continue
        break
    
    未找到循环体组队=copy(残存者)
    已找到循环体组队=list()
    残存者.insert(0,None)
    
    
    return 分子,残存者,未找到循环体组队,已找到循环体组队
    
    
def 非默认给出模式之进行二():
    残存者.pop(0)
    try:残存者[0]
    except IndexError:
        raise Exception("\n✅已将残存者收拾完毕")

def 非默认给出模式之进行三():
    print("◾️"+上色(f"该数的分数形式:{分子}/{当前残存者}"
    	"（最简分数形式:"+获取最简分数(分子,当前残存者)+"）","反"))


def 非默认给出模式之进行四():
    global 未找到循环体组队

    已找到循环体组队.append(当前残存者)
    未找到循环体组队=sorted(list(set(未找到循环体组队)-set(已找到循环体组队)))
    
    return 未找到循环体组队


def 非默认给出模式之进行五():    
    if not 已找到循环体组队:
        print("\n😓\n全都没有找到循环体")
    else:
        print(上色("\n👀\n⭐️已找到循环体的","反"))
        for item in 已找到循环体组队:print(上色(item,"反"),end=" ")
        print()
        
    print("\n👀\n◾️仍未找到循环体的")
    for item in 未找到循环体组队:print(item,end=" ")
    print("\n◾️未找到循环体的有%s个\n"%len(未找到循环体组队))
    


while True:
    print(取色("重置色"))
    回答=input("⚙️"+上色("\n⭐️设置你的位数(Enter:默认值)(默认值:20):","绿黑",False))
    if not 回答:
        dcm.getcontext().prec=20
        break
    try:dcm.getcontext().prec=int(回答)
    except:continue
    break
print(取色("重置色"))



while True:
    print("⚙️\n⭐️设置你的给出模式",
    	"1:给出分子与分母",
    	"默认:给出小数本身（此模式与位数设置无关）",
    	"请选择:",sep="\n"*2,end=str())
    	
    回答=input()
    if 回答=="1":是否默认给出模式=False
    else:是否默认给出模式=True
    break
    

if 是否默认给出模式:
    while True:
        回答=input("\n❓"+上色("你的小数是？(Enter:默认值)\n答:","重点黑"))
        if not 回答:
            你的小数="0.54"+"54"*10
            break
        try:你的小数=dcm.Decimal(回答)
        except:continue
        break
else:分子,残存者,未找到循环体组队,已找到循环体组队=非默认给出模式之进行一()

                
已完成=False       
while True:
    #对它找="0.011764705882352941176470588235294117647"
    #对它找="0.011764"
    if 已完成:break
    if 是否默认给出模式:
        对它找_decimal形式=dcm.Decimal(你的小数)
        已完成=True
    else:
        try:非默认给出模式之进行二()
        except Exception as e:
            print(e)
            已完成=True
        if 已完成:break
        当前残存者=残存者[0]
        对它找_decimal形式=dcm.Decimal(分子)/dcm.Decimal(当前残存者)
             
        
    对它找_完整部=对它找_str形式=对它找_decimal形式.__str__()
    if not 是否默认给出模式:
        对它找_完整部=对它找_丢弃最后一位=对它找_str形式[:-1]
    小数部分位数=对它找_完整部.split(".")[-1].__len__()
    print("\n✏️")
    
    if not 是否默认给出模式:非默认给出模式之进行三()
    #print("\n◾️该数的小数形式（来自于手机自带的科学计算器）\n",对它找,sep=str())
    print("\n◾️该数的小数形式\n（暂不使用手机自带的科学计算器",
    	"因为位数无限制",
    	"用手往后一拉就看答案了我不想那么早看答案）"
    	"\n（来自于decimal.Decimal 将prec（默认值28）设置为"
    	f"{dcm.getcontext().prec})"
    	"\n（由于decimal有最后一位四舍五入的毛病 而这不是我要的"
    	"我要的是截取 所以我把最后一位丢弃了",
    	"而模式二不存在此情况所以不必）")
    print(对它找_完整部)
    print("\n◾️小数部分位数:",小数部分位数)
       
    
    #只取用小数部分
    对它找=对它找_完整部.split(".")[-1]
    末位=-1
    小数点后第一位=-小数部分位数
    print("\n◾️小数点后第一位:",小数点后第一位)
    
    末位上的数字=对它找[末位]
    print("\n◾️末位上的数字:",末位上的数字)
    
    下一个位置生成器=找出下一个与末位数字相同的数字的位置(对它找)
    while True:
        print("\n✏️")
        try:下一个与末位数字相同的数字的位置=下一个位置生成器.__next__()
        except StopIteration:
            print("\n😓\n未找到循环体")
            break
            
        if 下一个与末位数字相同的数字的位置==末位:
            当前抓取片段首位=下一个与末位数字相同的数字的位置
        else:当前抓取片段首位=下一个与末位数字相同的数字的位置+1
        print("◾️当前抓取片段首位:",当前抓取片段首位)
        #input()
        
        当前抓取片段=对它找[当前抓取片段首位:None]
        print("◾️当前抓取片段:",上色(当前抓取片段,"红"))
        #input()
    
        try:当前抓取片段是否为循环体=判断当前抓取片段是否为循环体(对它找,当前抓取片段,当前抓取片段首位)
        except Exception as e:
            if e.__str__()=="❗️无法容纳下一个想象片段":
                print(e)
                print("\n😓\n未找到循环体")
            break
        print("◾️当前抓取片段是否为循环体:",上色(当前抓取片段是否为循环体,调色板[当前抓取片段是否为循环体]))
        #input()
        
        if 当前抓取片段是否为循环体:
            if not 是否默认给出模式:
                未找到循环体组队=非默认给出模式之进行四()
            
            首次循环体=当前抓取片段
            首次循环体长度=len(首次循环体)
            print("😋\n首次找到循环体:",上色(首次循环体,"反"))
            print("\n首次循环体长度:",上色(首次循环体长度,"重点黑"))
            
            最终循环体=找出最终循环体()
            最终循环体长度=len(最终循环体)
            print("😋\n已找到最终循环体:",上色(最终循环体,"反"))
            print("\n最终循环体长度:",上色(最终循环体长度,"重点黑"))
            break
    else:print("\n😓\n未找到循环体")


if not 是否默认给出模式:非默认给出模式之进行五()



#《try_220708_判断其中是否存在循环体.py》 
#1/85 = 0.0117647058823529411764705882352941176470

#updated:2022.7.8 17:13~23:06
#之前残存的
#弄得够好了

#updated:2022.7.10 17:14~
#《try_220708_0710_v12_判断其中是否存在循环体.py》
#增加支持的给出模式 原只支持给出分子与分母 现增加支持给出小数本身


#《try_220708_0710_v12_判断其中是否存在循环体.py》
#增加支持的给出模式 原只支持给出分子与分母（这样根本没有发挥出这代码真正的作用
#因为我是想把小数转分数 遇到了无限小数 所以才要找其循环体
#结果你告诉我要先把小数转成分数才能找其循环体 就像人是没钱才上班
#结果你要求上班必须要先有钱（理发/鞋子裤子穿得好/有手机） 那肯定不对劲了）
#（之前是因为最开始要测1/n的循环体 看看不同分母对循环情况的造成如何
#才首先支持该模式） 现增加支持给出小数本身

