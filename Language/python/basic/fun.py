import math

def nop():
	pass
def myabs(x):
	if not isinstance(x,(int,float)):#参数类型检查
		raise TypeError("bad input")
	if x >= 0:
		return x
	elif x< 0:
		return -x
def quadratic(a,b,c):
	if not isinstance(a,(int,float)):
		raise TypeError("bad input a")
	if not isinstance(b,(int,float)):
		raise TypeError("bad input b")
	if not isinstance(c,(int,float)):
		raise TypeError("bad input c")
	delta = pow(b,2) - 4 * a * c
	absdelta = abs(delta)
	if(a==0):
		return "error"
	if(delta >= 0):
		x1 = (-b + math.sqrt(absdelta))/(2*a)
		x2 = (-b - math.sqrt(absdelta))/(2*a)
		return (x1,x2)
	else:
		x1 = -b/(2*a)
		x2 = math.sqrt(absdelta)/(2*a)
		x3 = -b/(2*a)
		x4 = -math.sqrt(absdelta)/(2*a)
		return (str(x1) +"+"+ str(x2) + "i",str(x3) + "+"+str(x4) + "i")
# 定义默认参数要牢记一点：默认参数必须指向不变对象！
# 否则第二次调用会出错，Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
def add_end(L=[]):
	L.append('End')
	return L
def add_end_modify(L=None):
	if L is None:
		L = []
	L.append('End')
	return L
def calc(numbers):
	sum = 0
	for x in numbers:
		sum = sum + x * x
	return sum
def calc_modify(*numbers):
	sum = 0
	for x in numbers:
		sum = sum + x * x
	return sum
nop()
print(myabs(-0.1))
print(quadratic(1,4,4))
print(quadratic(2,3,1))
print(quadratic(1,3,-4))
print(quadratic(1,1,100))

print(add_end([1,2]))
print(add_end([1,2]))
print(add_end())
print(add_end())
print(add_end_modify())
print(add_end_modify())
#可变参数
print(calc([1,2,3,4]))
print(calc_modify(1,2,3,4))
#Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去：
nums = [1,2,3]
print(calc_modify(*nums))


#关键字参数:可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}
print(type(extra))
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)

#命名关键字参数
#对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
#如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
#
def person1(name, age, *, city, job):
    print(name, age, city, job)
person1('Jack', 24, city='Beijing', job='Engineer')
person1('Jack', 24, city='Beijing', job='Engineer')
#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person2(name, age, *args, city, job):
    print(name, age, args, city, job)
person2('jack','2',2,3,'6',city = 'bb',job = 'computer')
#person2('jack','2',2,3,'6')

#由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数。
#命名关键字参数可以有缺省值，从而简化调用：
def person3(name, age, *, city='Beijing', job):
    print(name, age, city, job)
person3('jack','2',job = '6')

#使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
def person4(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass

#参数组合
#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
#
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

print("最后的测试")
f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

#作业，多个数的乘法改造，用到了可变参数
def product(x, y = 1,*args):
    if args =={}:
    	return x * y
    else:
    	result = x * y
    	for i in args:
    		result = result * i
    	return result

print(product(5))# = 5
print(product(5, 6))# = 30
print(product(5, 6, 7))# = 210
print(product(5, 6, 7, 9))# = 1890
