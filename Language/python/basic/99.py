shuzhi = list(range(1,10))
print(shuzhi)
for i in shuzhi:
	 for j in range(1,i+1):
	 	print(" %d * %d = %2d"%(j,i,i*j),end='')
	 print("")
