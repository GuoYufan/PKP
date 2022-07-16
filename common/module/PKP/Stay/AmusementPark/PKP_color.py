from  PKP_istypethisone import *

class 颜色世界():
    def __init__(self):
        from types import MappingProxyType
        self.五颜六色={"蓝":"\033[1;34m","红":"\x1b[31m",
        "反":"\x1b[7m","绿黑":"\033[32;40m",
        "重点黑":"\x1b[1;30m",
        "重置":"\033[0m"}
        self.提示色=self.五颜六色['蓝']
        self.代码色=self.五颜六色['反']
        self.重置色=self.五颜六色['重置']
        self._预备色号={"提示色":0,"代码色":1}
        self.预备色号=MappingProxyType(self._预备色号)
    
    def 色名关卡(self,色名=None):
        if isinstance(色名,(list,set,dict)):return False
        try:dict()[色名]=None
        except:return False
        return True
        
    def 看色(self,色名=None):
        if not self.色名关卡(色名):return self.五颜六色
        if 色名 in self.五颜六色:
            return repr(self.五颜六色[色名])
        if 色名==0:return repr(self.提示色)
        if 色名==1:return repr(self.代码色)
        return self.五颜六色        

    def 取色(self,色名='重置'):
        if not self.色名关卡(色名):return self.重置色
        if 色名 in self.五颜六色:
            return self.五颜六色[色名]
        if 色名==0:return self.提示色
        if 色名==1:return self.代码色
        return self.重置色

    def 改色(self,色名='蓝',颜色代码表=[1,34],模式="add"):
        if not self.色名关卡(色名):return self.五颜六色
        if 模式=="add" and type(颜色代码表) in [list,int]:
            if isinstance(颜色代码表,int) or\
(颜色代码表 and 颜色代码表.O(int)):
                self.五颜六色[色名]=\
"\033["+";".join(str(颜色代码表).strip("[]").replace(" ",str()).split(","))+"m"
        if 模式=="del" and 色名 in self.五颜六色:del self.五颜六色[色名]
        return self.五颜六色

    def 上色(self,语=str(),语型色名="提示语",自动重置=True,反转=False):
        try:语=语.__str__()
        except:
            raise TypeError(上色("语","重点黑")+"的类型无法转换成字符串")
        if not self.色名关卡(语型色名):return 语
        变语=语
        if 语型色名 in ["提示语",0]:
            变语=语.join([self.提示色,self.重置色])
        elif 语型色名 in ["代码语",1]:
            变语=语.join([self.代码色,self.重置色])
        elif 语型色名 in self.五颜六色:
            变语=语.join([self.取色(语型色名),self.重置色])
        else:pass
        if not 自动重置:变语=变语[:-len(self.重置色)]
        if 反转:
            变语表=list()
            if 语:变语表=变语.split(语)
            else:
                import re
                变语表=re.findall(r"\x1b\[.*?m",变语)
            变语表.reverse()
            变语=语.join(变语表)
        return 变语


颜色=颜色世界()
上色,看色,取色,改色=(
	颜色.上色, 颜色.看色, 
	颜色.取色,
	颜色.改色
	)


#updated:2021.6.29 10:25~
#增加类：颜色世界
#updated:2021.6.29 18:55~19:24
#updated:2021.6.29 20:38~
#自己实现Python3.9版本才有的str,removeprefix
#import os
#removeprefix=lambda word,prefix:word[len(prefix)+1:]
#print(removeprefix(__file__,os.path.dirname(__file__)))
#updated:2021.6.30 5:34~
#加强了上色函数
#updated:2021.7.2 11:59~
#增加字典键只读
#updated:2021.7.2 12:35~
#isinstance也可以同时测多类型 接收的是tuple对象
#updated:2021.7.5 5:07~
#增加上色参数<是否重置>
#updated:2021.7.6 13:57~
#考虑重置色置前置后的选项
#比如目前实现的是 取色("红")+语+取色()
#那么如何有个选项可以直接反转为
#取色()+语+取色("红")
#updated:2021.7.6 17:03~
#上色第四个参数改为<自动重置>
#增加第五个参数<反转>
#updated:2021.7.6 23:21~
#修复颜色代码表不能为0的问题
#因为当为0时 就为False
#不能先行以 if <颜色代码表> 这样的判断
#updated:2021.7.8 19:30~19:51
#解决split不能以空字符串进行拆分的问题
#是用re解决的
#代码管理
#原版本：语+本语
#更新为：语+变语
#updated:2021.7.9 13:20~13:41
#之前遗漏的小修整

#updated:2021.7.15 22:25~
#重点黑不是1 1只是加粗
#重点黑是加粗以及黑色 是1以及30
#即"\033[1;30m"

#updated:2021.7.15 22:25~
#修复函数上色()中对语的类型要求过高问题
