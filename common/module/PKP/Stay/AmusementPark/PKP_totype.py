from PKP_Using_Obliged_setBuiltInType import *

@sign(list,"totype")
def totype(seq):
    if not isinstance(seq,(list,tuple)):
        raise TypeError("must be list or tuple, not "+\
type(seq).__name__)

    return [type(element) for element in seq]


#updated:2021.10.6 1:40~2:14
#列表内元素转类型
