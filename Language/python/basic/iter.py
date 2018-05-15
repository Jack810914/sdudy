#迭代
#如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
#for ... in,Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
#list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：

#因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。

#默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value，可以用for k, v in d.items()。

#由于字符串也是可迭代对象，因此，也可以作用于for循环for ch in 'ABC':
#当我们使用for循环时，只要作用于一个可迭代对象，for循环就可以正常运行，而我们不太关心该对象究竟是list还是其他数据类型
#判断一个对象是可迭代对象
from collections import Iterable
print(isinstance('abc',Iterable))
print(isinstance(123,Iterable))

for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)

def findMinAndMax(L):
	if not isinstance(L, Iterable):
		return (None,None)
	if L == []:
		return (None,None)
	minvalue = L[0]
	maxvalue = L[0]
	for x in L:
		if not isinstance(x, (int, float)):
			continue
		if x >maxvalue:
			maxvalue = x
		if x <minvalue:
			minvalue = x
	return (minvalue, maxvalue)

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')