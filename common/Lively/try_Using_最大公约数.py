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
	"try_220624_最大公约数",
	)
))
del os,sys,here

from try_220624_最大公约数 import (
	获取最大公约数,
	获取最简分数,
	获取最简分数_多参版,
	分数约分,
	)
	
if __name__=="__main__":
    print(dir())