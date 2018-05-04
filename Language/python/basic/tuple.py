#tuple 圆括号，一旦初始化不能修改，没有pop insert等方法，可以使用，不能修改
classmates = ('mike','bob','tracy')
print(classmates)
print(classmates[1])
#如果要定义只有一个元素的tuple，必须使用（x,）,逗号不可缺少，是为了和数学运算符的圆括号区分开
t = (1,)
print(t)

#可变的tuple
t = ('a','b',['aa','bb'])
print(t)
t[2][0] = 'cc'
print(t)