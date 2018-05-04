#list study
#list特点：有序
#例子
classmates = ['mike','bob','tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[len(classmates)-1])

print(classmates[-1])
print(classmates[-2])

#追加元素，加入到尾部或者加入到指定位置
classmates.append('adam')
classmates.insert(1,'lucy')
print(classmates)
#删除元素，删除尾部用pop()，删除指定位置pop(i)
classmates.pop()
classmates.pop(1)
print(classmates)
#替换
classmates[1] = 222
print(classmates)

#list 可以嵌套，可以理解为C++的多维数组
classmates1 = classmates
classmates2 = classmates
school = [classmates1,classmates2]
print(school)
print(school[1][1])

#list 可以为空
L = []
print(len(L))