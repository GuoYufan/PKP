import os,re
中间路径=os.sep.join("/common/module/PKP".split("/"))
顶层路径=re.match("(.+)"+中间路径+".*",os.path.dirname(__file__)).group(1)
del os,re,中间路径

if __name__=="__main__":
    print("\n顶层路径:",顶层路径)


'''
import os

顶层路径=os.sep.join(\
	os.path.dirname(__file__).split(os.sep)\
	[:-len(os.sep.join("/common/module/PKP".split("/")).split(os.sep))])
'''
