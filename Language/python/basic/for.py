#for in
#break continue的作用同C++
names = ['bob','alice','david']
for name in names:
	print(name)

print(list(range(101)))
print(range(10))
sum = 0
datalist = list(range(101))
for x in datalist:
	sum = sum + x
print(sum)

str1 = 'Hello,'
str2 = '!'
L = ['Bart', 'Lisa', 'Adam']
for x in L:
	print(str1,x+str2)