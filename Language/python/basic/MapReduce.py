#HighOrder
#结论：函数本身也可以赋值给变量，即：变量可以指向函数。
#可以认为是函数指针，函数别名
#把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
#我们先看map。map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

def f(x):
	return x * x

L = list(range(1,9))
print(L)
r = map(f,L)
print(list(r))
print((r))

#再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#比方说对一个序列求和，就可以用reduce实现：

from functools import reduce
def add(x, y):
		return x + y

print(reduce(add, [1, 3, 5, 7, 9]))

#整理成一个str2int的函数就是：
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
print(str2int("123456"))

#还可以用lambda函数进一步简化成：
from functools import reduce

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2num(s):
    return DIGITS[s]

def str2int1(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print(str2int1("123456"))

#利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：
from functools import reduce
def normalize(name):	
    name0 = name[0:1]
    name1 = name[1:]
    name0 = name0.upper()
    name1 = name1.lower()
    return name0 + name1
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

#Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

def prod(L): 
	def mul(x, y):
		return x * y  
	return (reduce(mul, L))

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

#利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：
def str2float(name):
    location = -1
    for i,value in enumerate(name):
    	if value is '.':
        	location = i
    if(location == -1):
    	return None
    nameleft = name[0:location]
    nameright = name[location+1:]
    nameright = list(reversed(nameright))  
    print(nameleft)
    print("--%d"%location)
    print(nameright)
    DIGITS={'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    def char2num(s):
        return DIGITS[s]
    def fn(x, y):
        return x * 10 + y
    def fn1(x, y):
        return (x * 0.1 + y)
    return reduce(fn, map(char2num, nameleft)) + reduce(fn1, map(char2num, nameright))/10

print(str2float('123.456'))
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')