from PKP_Using_Obliged_setBuiltInType import *

@sign(list,"draw")
def draw(prize,minpool=1,maxpool=None):
    if not hasattr(prize,"__len__") or isinstance(prize,set):
        raise TypeError("must be a container and must support indexing like str or list.Check its type please")
    if not isinstance(minpool,int):
        raise TypeError("arg 2 'minpool' must be int")
    #if not minpool<len(prize):
        #raise ValueError("arg 2 'minpool' is too large")

    if maxpool==None:maxpool=len(prize)
    elif not isinstance(maxpool,int):
        raise TypeError("arg 3 'maxpool' must be int or None")
    #elif maxpool<minpool:
        #raise ValueError("arg 3 'maxpool' cannot be less than arg 2 'minpool")
    #elif maxpool<0:
        #raise ValueError("arg 3 'maxpool' cannot be less than 0")
    
    import random
    quantity=random.randint(minpool,maxpool)
    return random.choices(prize,k=quantity)
    
'''
print(list(range(100)).draw(10))
'''


#updated:2021.10.6 4:47~4:57
#《try_211006_随机生成列表.py》
#完成

#created:2021.10.6 20:29
#随机生成列表 用Python自带的方法
#即电脑的方法 即com

#updated:2021.10.8 3:33~
