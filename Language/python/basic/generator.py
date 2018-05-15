import numpy as np
#generator
#杨辉三角的例子开发的有问题，通过循环和迭代都能实现，但是加上generator结果有问题，后续需要再研究，可能和结果是累计的有关
#不必创建完整的list，从而节省大量的空间。在Python中，这种一边循环一边计算的机制，称为生成器：generator。
#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
L = [x * x for x in range(10)]
G = (x * x for x in range(10))
print(L)
print(G)
#print(next(G))
#print(next(G))
print("  ")
for n in G:
	print(n)

#yield 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield(b)
        a, b = b, a + b
        n = n + 1
    return 'done'
#最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
#但是用for循环调用generator时，发现拿不到generator的return语句的返回值。如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中
#for或者while来处理
for n in fib(6):
	print(n," ",end = "")
print("  ")
g = fib(6)
while True:
	try:
		x = next(g)
		print('g:', x)
	except StopIteration as e:
		print('Generator return value:', e.value)
		break

# 杨辉三角
def trianglesGenerator(num):
	result = [1]
	#yield(result)
	reusltTemp = [1]
	m = 2
	while m <= num:
		res = reusltTemp
		last = [0] + res + [0]
		length = len(last)
		reusltTempLeft = last[:length-1]
		reusltTempRight = last[1:length]
		reusltTemp = reusltTempLeft
		loop = 0
		while loop < len(reusltTempLeft):
			reusltTemp[loop] = reusltTempLeft[loop] + reusltTempRight[loop]
			loop = loop + 1	
		result.append(reusltTemp)
		#yield(result)
		m = m+1
	result[0] = [1]
	#yield(result)
	return result
#递归
def triangles(num):
	#m = 0
	#while m < num:
	#yield(result)
	if num == 1:
		result = [1]
	else:
		#print(num)
		res = triangles(num-1)
		last = [0] + res + [0]
		length = len(last)
		result = last[:length-1]
		b = last[1:length]
		loop = 0
		while loop < len(result):
			result[loop] = result[loop] + b[loop]
			loop = loop + 1
	print(result)
	return result
	#m = m + 1

# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]

n = 0
results = []

ret = trianglesGenerator(10)
print(ret)
print('测试开始......')
for t in ret:
    print(t)
    #results = t
    results.append(t)
    n = n + 1
    if n == 10:
        break
print('测试开始......')
print(type(results[0]))
print(results)
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
