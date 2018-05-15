#切片
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
#取前3个元素
#L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
#如果第一个索引是0，还可以省略：
print( L[0:3])
print( L[:3])
#也可以从索引1开始，取出2个元素出来：
print( L[1:3])
#类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：
#记住倒数第一个元素的索引是-1
print( L[-2:-1])
print( L[-2:])

#tuple也是一种list，唯一区别是tuple不可变。因此，tuple也可以用切片操作，只是操作的结果仍是tuple：
#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：
def trim(s):
	print("xhc0")

	while s[:1] == ' ':   #如果字符串第一个是空格，删除第一个
	    s = s[1:]
	if s[-1] == ' ':
		print("xhc")
	while s[-1:] == ' ':  #如果字符串最后一个是空格，删除最后一个
	    s = s[:-1]
	return s

print(trim(" sdf gad "))

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
