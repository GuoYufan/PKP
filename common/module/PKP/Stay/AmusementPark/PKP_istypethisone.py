from PKP_Using_Obliged_setBuiltInType import *

@sign(list,"istypethisone")
def istypethisone(sequence,typeNames,mode="all"):
    if not isinstance(sequence,(list,tuple)):
        raise TypeError("arg 1 must be list or tuple")
    if not sequence:return None   
       
    result=None
        
    try:typeNames=tuple(typeNames)
    except TypeError:pass
    
    specify_someone=typeNames
    compare_to_specify_someone=\
    [i for i in sequence if isinstance(i,specify_someone)]
        
    if mode=="all":
        result=len(compare_to_specify_someone)==len(sequence)
    elif mode=="any":
        result=bool(compare_to_specify_someone)
    
    return result


@sign(list,"O")
def O(sequence,typeNames,mode="all"):
    return sequence.istypethisone(typeNames,mode)

@sign(list,"_O")
def _O(L,T):return not L.O(T)

@sign(list,"O_")
def O_(L,T):return L.O(T,"any")
    
@sign(list,"_O_")
def _O_(L,T):return not L.O(T,"any")


'''        
    specify_someone=typeNames
    compare_to_specify_someone=\
    [isinstance(i,specify_someone) for i in sequence]
        
    if mode=="all":
        result=all(compare_to_specify_someone)
    elif mode=="any":L
        result=any(compare_to_specify_someone)~
    
    return result
'''

#updated:2021.7.1 8:31~
#列表元素类型是否全部为指定类型
#又一个我的函数
#我要把它命名为isalltypethisone
#这样 继内置类型str有了我的lengthsplit之后
#内置类型list也有了一个我的方法

#updated:2021.7.6 22:32~
#之前调用为istypeoo
#是istypeonlyone的缩写
#如此含义与istypeallsame（缩短为istypesame）重复
#还是要改回isalltypethisone
#缩短为istypethisone

#updated:2021.7.11 14:25~
#小修整

#updated:2022.7.11 23:40~
#specify_someone
#compare_to_specify_someone
