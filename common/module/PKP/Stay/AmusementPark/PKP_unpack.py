from PKP_Using_Obliged_setBuiltInType import *

@sign(list,"unpack")
def unpack_v14(source):
    if not isinstance(source,(list,tuple)):
        raise TypeError("must be list or tuple, "+\
f"not {type(source).__name__}")

    from copy import copy
    
    result=list()
    last=copy(source)
    
    while True:
        for element in last:
            try:result.extend(element)
            except TypeError:result.append(element)
        if result == last:break
        last=copy(result)
        result.clear()
        
    return result
    

#created:2021.10.5 23:42~
#一个空列表 extend i for i in 多重列表
#如此反复 直到没有list
#能否与之前的手撕方法同样实现多重列表unpack？

#extend法解多重列表

#updated:2021.10.6 1:13~
#《try_v10_211006_extend法解多重列表.py》
#完成
#updated:2021.10.6 1:32~
#《try_v11_211006_extend法解多重列表.py》
#小修整
#updated:2021.10.6 2:19~
#《try_v12_211006_extend法解多重列表.py》
#用检测列表里有无此类型的方法 替代 与last比较是否相同的方法
#来减少一次冗余 也就是用list.nothistype方法


@sign(list,"unpack_v10")
def 手撕(汉堡包蜜汁鸡):
    if not isinstance(汉堡包蜜汁鸡,(list,tuple)):
        raise TypeError("must be list or tuple,"+\
f"not {type(汉堡包蜜汁鸡).__name__}")
    from copy import copy
    同款=copy(汉堡包蜜汁鸡)
    合上=int()
    开吃啦=list()
    def 撕到底(汉堡包蜜汁鸡,合上):
        for 芝士火腿鸡肉 in 汉堡包蜜汁鸡:
            if 汉堡包蜜汁鸡==同款:合上=0
            if isinstance(芝士火腿鸡肉,(list,tuple)):
                合上=撕到底(芝士火腿鸡肉,合上)
            else:
                开吃啦.append(芝士火腿鸡肉)
        合上+=1
        return 合上
    撕到底(汉堡包蜜汁鸡,合上)
    return 开吃啦


#created:2021.7.4 14:55
#test_210704_解表中表.py
#我写《解表中表》函数是由于
#我的DL_TITLE函数的参数值关卡之需要
#我的DL_TITLE函数的delay参数值范围是
#in above or in below or in between
#above=[ "前", 0 ]
#below=[ "后", 2 ]
#between=[ "中", 1 ]
#我本来是写成
#if str(delay) in "前中后012"
#但是这样的写法太受限了 我不满意 我不想写成这样

#updated:2021.7.8 12:24~
#直至第一个元素不是列表
#实现了取出第一个二层列表的元素
#可以实现最深对二层列表的解表中表
#updated:2021.7.9 1:24~
#updated:2021.7.9 1:47~2:32
#回头取+末层+展开最终章
#updated:2021.7.9 3:03~

#updated:2021.7.9 16:29~
#每次进去是拿着什么进去的？
#这个最终章是进去几次得到的？
#第一次出来是最后一次进去的出来
#第一次出来是带着time为1出来
#继续往下走
#最后一次是拿着[0]进去
#[0]是怎么遍历得到的？
#是由["左",[0]]遍历得到的
#所以第一次出来是出到
#for 当前层 in ["左",[0]]
#直到最终章([0],time)
#遍历完了就要开始出来
#传进去的<当前层>就是正在接收的<汉堡盒>
#updated:2021.7.9 17:02~
#完成
#updated:2021.7.9 17:23~
#只要是遍历完了 都会自增1
#而到“出来2次”就没有“出来3次”了
#是因为还没遍历完
#updated:2021.7.9 18:03~18:39
#再次测试 没出问题
#updated:2021.7.9 19:20~19:40
#函数名：手撕(汉堡包蜜汁鸡)
#内函数名：撕到底(汉堡包蜜汁鸡,合上)
#内变量名：同款 合上 开吃啦 芝士火腿鸡肉
#updated:2021.7.9 19:40~20:17
#已测试一次 无问题
