#set
r'''
和dict类似，也是一组key的集合，但不存储value。
由于key不能重复，所以，在set中，没有重复的key。
要创建一个set，需要提供一个list作为输入集合：
重复元素会被过滤
通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
通过remove(key)方法可以删除元素
两个set可以做数学意义上的交集、并集等操作： & |
set和dict的唯一区别仅在于没有存储对应的value，但是，
set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
>>> s = set([1, 1, 2, 2, 3, 3])
>>> s
{1, 2, 3}
'''
s1 = set([1, 1, 2, 2, 3, 3])
s2 = set([4, 5, 2, 2, 3, 3])
s3 = s1 & s2
print(s3)
s4 = s1 | s2
print(s4)
s3.add(8)
print(s3)
s4.remove(3)
print(s4)