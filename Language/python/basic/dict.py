#dict 类似于map，key-value存储，快速查找，类似于查字典
#一个key只能对应一个value，后存储的会覆盖前面的
#list是无序的
#list占用内存大，空间换时间
#key值不能变，通过key来计算value的方法称为哈希算法Hash
#list是可变的，因此不能作为dict的key
#如果访问不存在的元素，会报错
r'''
d['Thomas']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Thomas'
'''
#判断是否存在可以使用in方法来判断
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
print('ss' in d)
print(d.get('ss')) #不存在返回None
print(d.get('Bob'))
print(d.get('ss',-1)) #不存在返回-1
print(d.get('Bob',-1))

#pop  删除字典的某一项,删除key的同时也删除了value
d.pop('Bob')
print(d)