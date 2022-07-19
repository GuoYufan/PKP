import sys,os
sys.path.append(
    os.path.dirname(__file__)+"/common/module/"
    "PKP")
del sys,os
from PKP import *


if __name__=="__main__":
    class 在文件中模拟终端世界():
        def __init__(self):
            self.code=str()
            self.codeThisLine=str()
            self.codeAllLines=list()
            self.examples=(
            	"dir()",
             "dir(list)",
             "a='GuoYufan'",
             "b=list(range(10))",
             "from copy import copy",
             "a_,b_=map(copy,(a,b))",
'''
def cp():
    global a_,b_
    a_,b_=copy(a),copy(b)
''',
'''
def new():
    global a,b
    a,b=map(copy,(a_,b_))
''',
             "a",
             "b",
             )
    
        def execute(self,statement=None):          
            if statement:self.code=statement
            
            # eval执行是否发生异常
            eval_failed=False
                
            try:
                eval_return_value=eval(self.code,None,globals())
                #input("eval执行一次")
            except Exception as e:
                    # eval("b=1")
                    if isinstance(e,SyntaxError):pass
                    eval_failed=True
                    
            if not eval_failed:
                if not (eval_return_value==None):
                    print(repr(eval_return_value))        
                return True
            else:
                try:
                    exec(self.code,None,globals())
                    #input("exec执行一次")
                except Exception as e:
                    input("❌"+type(e).__name__+":"+str(e))
                    return False
                
            return True
        	
        	
        def automatic(self):
            for statement in self.examples:
                print(f">>> {statement}")
                self.execute(statement)
    
                
        def terminal(self):
            while True:
                self.codeThisLine=input(\
上色("Write some codes you will execute:\n"+\
">>> ","重点黑"))
                if not self.codeThisLine:continue
                
                if not [char for char in list(":\\")\
if self.codeThisLine.endswith(char)]:
                    self.codeAllLines.append(self.codeThisLine)
                else:
                    self.codeThisLine+="\n"
                    self.codeAllLines.append(self.codeThisLine)
                    while True:
                        self.codeThisLine=input("... ")
                        if not self.codeThisLine:break
                        self.codeThisLine+="\n"
                        self.codeAllLines.append(self.codeThisLine)
                self.code=str.join(str(),self.codeAllLines)
                self.codeAllLines.clear()
                if not self.execute():continue
    
            
        def do(self):
            self.automatic()
            self.terminal()
    
           
    def 主函数():
        在文件中模拟终端=在文件中模拟终端世界()
        在文件中模拟终端.do()

        
    主函数()


#updated:2021.7.7 0:55~
#该GYF中间模块专用于对GYF根模块的检测

#updated:2021.7.?
#解决sublime输出编码问题
#import io
#sys.stdout=io.TextIOWrapper(\
# sys.stdout.buffer,encoding="utf8")

#updated:2021.7.8 14:44~
#Windows下对于file读写
#为了避免'gbk' codec can't decode的问题
#必须加上参数encoding="utf-8"
#即要
#with open(name,mode,encoding="utf-8")

#updated:2021.7.9 21:48~
#eval的报错不值得一看
#eval只允许expression
#expression就是有返回值的语句
#不允许其他的statement 比如像赋值语句这样的
#总之从此取消对eval报错的print

#updated:2021.7.11 3:09~
#增加我的<手撕>函数英文名unpack的显示

#updated:2021.7.11 11:36~
#可能设置eval的locals参数值会好一点才不受限
#updated:2021.7.11 11:49~
#确实是把eval的locals参数值设为globals()就好了
#只是不能以常规的不按位置而指定参数名传值
#也就是不能eval(source,locals=globals())
#而必须eval(source,None,globals())

#updated:2021.7.11 11:58~
#出问题了
#在函数里用exec创建变量
#这变量只存留在函数这局部空间里
#updated:2021.7.11 12:02~
#可能是要合并globals()跟locals()这两个字典

#updated:2021.7.11 12:42~
#为什么不能在函数这局部空间里用exec创建变量？
#updated:2021.7.11 12:45~
#我明白了 exec也有locals参数 也是要设locals参数
#也是要exec(source,None,globals())

#updated:2021.7.11 12:50-
#所以只要在exec设置好locals参数
#赋值语句就正常了
#但像dir()这样的还是不正常
#再在eval设置好locals参数
#dir()也正常了
#再把eval的报错屏蔽掉就行了
#note:2021.7.11 13:02~
#完成了 没出问题

#updated:2021.7.11 12:59~
#对于要屏蔽的eval的报错
#其实那是允许expression即有返回值的语句
#而不允许像赋值语句这样的statement
#其实那是语法错误 SyntaxError
#所以先捕捉Exception全部异常
#再type判断该异常是否为SyntaxError
#如果是则屏蔽掉 否则可报错
#note:2021.7.11 13:18~
#完成了 没出问题

#updated:2021.7.11 13:20~
#如此 写成函数这局部空间也就没问题了
#note:2021.7.11 13:26~
#完成了 确实没问题

#updated:2021.10.6 16:14~
#GYF根模块由 GYF_using_v12 更新为 GYF_using_plus_v13


#updated:2022.11.7 23:56~
#try...except应该用input暂停它
