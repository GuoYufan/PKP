from PKP_Using_Obliged_setBuiltInType import *

@sign(list,"substract_COM")
def substract_COM(substracted,substractor):
    if not isinstance(substractor,(list,tuple)):
        raise TypeError("arg 2 'substractor' must be list or tuple, not "+\
type(classroom).__name__)

    from copy import copy
    substracted,substractor=map(copy,(substracted,substractor))
    
    for element in substractor:
        if element in substracted:
            substracted.pop(substracted.index(element))
            
    return substracted

    
#updated:2022.7.14 13:51~
#《try_v15_211006_220714_列表相减尝试.py》


@sign(list,"substract")
def flux(concert,classroom):
    if not isinstance(classroom,(list,tuple)):
        raise TypeError("arg 2 'classroom' must be list or tuple, not "+\
type(classroom).__name__)

    from copy import copy
    classroom=list(classroom)
   
    concert=copy(concert)
    classroom=copy(classroom)
    
    def nextone():
        nonlocal ticket
        ticket+=1

    def stayhere():pass
    
    def completely():pass
    
    def cleared():
        nonlocal classroom,concert
        return not (classroom and concert)
        
    ticket=0
    while True:
        try:audience=concert[ticket]
        except IndexError:
            completely()
            break
        student=audience
        if student in classroom:
            seat=classroom.index(student)
        else:
            nextone()
            continue
        classroom.pop(seat)
        concert.pop(ticket)
        if cleared():
            completely()
            break
        stayhere()
        
    return concert
    
'''
lst1=[1,3,3,2,1,2]
lst2=[1,2,3]

input(lst1.sub([]))
input([].sub(lst1))
input(lst1.sub(lst2))
#input(lst2.sub(lst1))
'''


#updated:2021.10.6 3:49~4:08
#《try_v11_211006_列表相减尝试.py》
#完成

#updated:2021.10.6 4:17~
#《try_v12_211006_列表相减尝试.py》
#不在里面你还找什么？你不找不就没事了？
#你又不是不能知道不在里面
#list.index要抛出异常还不是因为你不在里面还找？
#用in替代list.index抛出的ValueError

#updated:2021.10.6 5:23~
#《try_v13_211006_列表相减尝试.py》
#增加随机生成列表

#updated:2021.10.6 11:45~
#《try_v14_211006_列表相减尝试.py》
#修改为只返回相减的其中一者 而不是两者
#也就是只返回被减数 而不是被减数与减数都返回
#这样更符合减法运算的本义
#减法运算是被减数-减数=差 这个差是被减数的剩余
#当然 在这里 减数的剩余与被减数的剩余 仍然都被保留
#也就是我仍然计算出来这部分 但是我不使用这部分
