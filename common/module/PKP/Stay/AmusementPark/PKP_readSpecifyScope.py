from PKP_color import *
from PKP_istypethisone import *

def readSpecifyScope(here=__file__,only_s=[],only_m=[],after=1,before=None,empty_s=[],empty_m=[],color=1):    
    if not isinstance(here,str):
        raise TypeError("arg 1 'here' must be str")
    #if [i for i in [only_s,only_m,empty_s,empty_m] if not isinstance(i,list)]
    if [only_s,only_m,empty_s,empty_m]._O(list):
        raise TypeError("arg 2/3/6/7 must be list")
    
    ask=str()
    if only_m:
        [only_s.extend(i) for i in [range(s,e+1) for s,e in zip(only_m[::2],only_m[1::2])]]
    if empty_m:
        [empty_s.extend(i) for i in [range(s,e+1) for s,e in zip(empty_m[::2],empty_m[1::2])]]
    mode=dict(zip(['only','em'],[bool(i) for i in [only_s,empty_s]]))
    with open(here,"r") as py:
        print()
        for i,line in enumerate(py.readlines()[after-1:before]):
            only=lambda:i+after in only_s
            em=lambda:i+after in empty_s
            #mode:1.empty&only_read 2.only_read
            if mode["only"]:
                if only() and not em():
                    ask=input(上色(f"📜line {i+after} {line}",color))
            #mode:empty
            else:
                if not em():
                    ask=input(上色(f"📜line {i+after} {line}",color))
            if ask.lower()=="q":return
    only_s.clear()
    empty_s.clear()


#updated: 2021.5.10 18:14~
#我最近写的GYF_readSpecifyScope读取指定行部分
#用的是readline
#其实用Python自带的readlines就能实现了
#updated: 2021.5.10 20:46~
#添加只读取指定部分行功能
#之前是只有跳过指定部分行功能
#updated: 2021.5.10 21:14~
#可跳过指定单行或多行
#可只读取指定单行或多行
#updated: 2021.5.10 21:50~
#updated: 2021.5.10 22:00~
#updated: 2021.5.11 20:32~
#增加图案📜
#updated: 2021.5.12 20:12~
#可以不设置after跟before这两个参数
#updated: 2021.5.13 0:36~
#调整参数位置 使only置前 after在中 empty置后
#updated: 2021.5.13 4:00~
#添加一次换行在之前
#updated: 2021.5.13 4:12~4:41
#修复在同一文件内调用该函数设置only_m两次以上出现的冲突问题
#only_m冲突问题是由于每一次设置only_m都会添加进only_s
#并且每次设置only_m并不会清空only_s
#而且only_s保持之前被only_m添加的继续把only_m的添加进来
#解决办法：在最后清空only_s
#要清空 可以用clear
#注意：=list()并不能清空 具体是为什么我不清楚
#del也不能清空

#updated: 2021.5.13 6:07~
#切片置空从而走到最后一个元素可以用None
#[0:None]
#end=None [0:end]
#所以 此前before参数的默认值-1 现更改为None
