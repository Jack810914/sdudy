#列表生成式即List Comprehensions
#生成[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list(range(1,11)))
#生成[1x1, 2x2, 3x3, ..., 10x10],如果用循环
L = []
for x in range(1,11):
	L.append(x*x)
print(L)
#使用列表生成式可以很方便的替代上面的表达
L = [x * x for x in range(1,11)]
print(L)

#进一步的，可以加上条件判断
L = [x * x for x in range(1,11) if x%2 == 0]
print(L)

#双重循环
L = [m+n for m in "ABC" for n in "XYZ"]
print(L)

#运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os # 导入os模块，模块的概念后面讲到
L= [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
print(L)

#处理dict
d = {'x': 'A', 'y': 'B', 'z': 'C' }
L =  [k + '=' + v for k, v in d.items()]
print(L)

L = ['Hello',None, 'World', 18,'IBM', 'Apple']
L = [s.lower() for s in L if isinstance(s, str)]
print(L)