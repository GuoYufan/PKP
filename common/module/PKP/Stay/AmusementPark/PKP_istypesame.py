from PKP_Using_Obliged_setBuiltInType import *

@sign(list,"istypesame")
def istypesame(sequence,mode="all"):
    if not isinstance(sequence,(list,tuple)):
        raise TypeError("arg 1 must be list or tuple")
    if not sequence:return None

    first_one=type(sequence[0])
    compare_to_first_one=[i for i in sequence if type(i)==first_one]
    
    if mode=="all":
        return len(compare_to_first_one)==len(sequence)    
    elif mode=="any":
        return bool(compare_to_first_one)
        
    return None



#完全一样
@sign(list,"S")
def S(sequence,mode="all"):
    return sequence.istypesame(mode)

#不完全一样
@sign(list,"_S")
def _S(L):
    return not L.S()

#有些一样
@sign(list,"S_")
def S_(L):
    return L.S("any")
    
#完全不一样
@sign(list,"_S_")
def _S_(L):
    return not L.S("any")

    
'''    
    first_one=type(sequence[0])
    compare_to_first_one=[i==first_one for i in sequence.totype()]
    
    if mode in ("all","any"):
        return eval(f"{eval(f'{mode}')(compare_to_first_one)}")
    return None
'''


#updated:2021.6.29 16:50~17:13
#updated:2021.6.29 17:49~
#《列表元素类型是否相同》
#updated:2021.7.1 7:01~
#增加进场函数 装global部分

#updated:2021.7.7 15:15~

#updated:2021.7.11 14:25~
#小修整
