import os
here=__file__
#当设置为1 为回退到最底层目录
回退到上几级目录=3
for i in range(回退到上几级目录):
    here=os.path.dirname(here)
del 回退到上几级目录,i


import sys
sys.path.append(
	here+os.sep.join(
	(
	str(),"try",
	"try_220619_cook",
	"try_220624_小数与分数",
	"try_220701_分数四则运算",
	)
))
del os,sys,here

from 分数四则运算 import (
	获取最小公倍数,
	分数形式转换,
	连分数转换,
	分数四则运算,
	)
	
if __name__=="__main__":
    print(dir())