#sorted排序算法
s = sorted([36, 5, -12, 9, -21])
print(s)
#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
s = sorted([36, 5, -12, 9, -21], key=abs)
print(s)
#默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
s = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(s)
#忽略大小写
s = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(s)
#要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True：
s = sorted(['bob', 'about', 'Zoo', 'Credit'],key = str.upper,reverse = True)
print(s)

print("作业")
L = [('Bob', 75), ('Adam', 92), ('bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0].lower()
def by_score(t):
	return t[1]
L2 = sorted(L, key=by_name)
print(L2)
L2 = sorted(L, key=by_score)
print(L2)