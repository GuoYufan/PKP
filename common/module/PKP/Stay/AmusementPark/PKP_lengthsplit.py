from PKP_Using_Obliged_setBuiltInType import *

@sign(str,"lengthsplit_COM")
def lengthsplit_COM(word,length):
    if not (isinstance(length,int) and length>0):return [word]
    if length>=len(word):return [word]
    
    result=list()
    last=word
    while True:
        result.append(last[:length])
        last=last[length:]
        if not last:break
    
    return result


@sign(str,"lengthsplit")
def lengthsplit(word,length):
    if not (isinstance(length,int) and length>0):return [word]
    if length>=len(word):return [word]
    return [word[length*i:length*i+length] for i in range(len(word)//length+1)]


#created:2021.6.30 2:01
#updated:2021.6.30 2:48~
#《以长而分》 
#updated:2021.6.30 13:13~
#增加对于拆分长度大于总长度时的检测
#这个版本 也就是我的原版 修改至此
#目前只有一种情况会出问题
#当整除时 即当余数为0时
#由于我+号连接的是余数有多少个就有多少个
#那么在余数>0时是没有问题的
#当余数==0 端点重叠 取出来的是空字符串
#可是又把之前最后一组端点删了
#比如本来[5,6] [6,7]就好了 却删了[6,7]
#自己又弄不成[6,7]
#因为在此算法下当余数=0自己去弄是弄不成的
#已经是弄好了不该自己去弄了
#可是仍然要append进去 于是就多了个空字符串
#《lengthsplit_v10》


#updated:2021.6.30 12:58~
#网上找的思路
#找每一组的start
#先把最后一组之前的全部获取
#已经获取的全部连起来
#与原字符串相差部分
#就是最后一批
#至于怎么连 就看你的了
#可以看已经获取多少组
#那么把组的数量乘以每组长度就是了
#《lengthsplit_web》


#updated:2021.6.30 15:41~
#就是个看倍数的游戏 所以可以反推总长度
#你3个3个地为一组 那我当然除以3 剩下的就是最后一组
#也就是说 余数就是最后一组 这就是个商与余数的游戏
#取余可以在任何拆分开始之前确定最后一组
#是否在第一轮就已经拆分好而不用进入第二轮
#反推总长度 我想多长的就多长 比如如果我想3个为一组
#我想余2个 ok 3x+2呗
#总长度可以为 5 8 11 14 15 20 等等
#updated:2021.6.30 17:10~
#最后一组长度就是轮次逻辑标号
#updated:2021.6.30 17:13~
#终于 我的lengthsplit跟网上找的一样不出问题了
#《lengthsplit_v15》


#updated:2021.6.30 17:41~
#以往为lengthsplit_old
#至此创建一个新的lengthsplit
#更新我的lengthsplit
#我是往多了算的
#网上的算法是往少了算的 看int()转整就知道了
#我这次更新是 对最后一组不删去了 而是替换掉
#即想要原位赋值[-1] 但发现不行 目前办法只有pop
#以[:-1]切片删去再+=连接 不行
#以[:-1]切片赋值再append 不行
#可以用负数start
#因为负数start只在整除时 即余数为0时出问题
#比如当负0的时候 就把全部弄出来了
#而len(word)-len(word)%length
#总长度减去余下作为为最后一组的 这样正数计算就不会出问题
#余数为0进入下一轮就会有问题 也就是会接上一个空
#余数为0不该进入下一轮 因为这一轮已经拆分好了最后一组
#不需要进入下一轮了
#而余数为0时即最后一组长度为0时
#我现在已经有<最后一组长度>这个变量作为控制
#当余数为0时根本不会进入第二轮
#所以不用担心这个问题了
#而只要解决了余数为0的问题 负数start就不会出问题了
#所以现在可以放心用负数start了
#余数就是最后一组的长度
#负号接余数就是最后一组的起始位置
#即最后一组的负数start（起始位置）
#就是负号接最后一组的长度 就是负号接余数
#就是负号接len(word)%length
#就是-len(word)%length
#像我这样早早建好变量并赋值好的
#则是负号接<最后一组长度>变量
#即 -<最后一组长度>
#比如-1就是最后一组长度为1时的起始位置 以此类推
#updated:2021.6.30 19:30~
#我的最新版本lengthsplit终于没问题了
#updated:2021.7.2 5:22~
#彻底修复我的lengthsplit问题
#负数start是有问题的 已弃用

#最后一组长度=len(word)%length
#《lengthsplit_v20》


#updated:2021.10.12 1:37~
#切片根本不用担心超出尾部问题 不用担心IndexError
#之前的lengthsplit版本都是多此一举
