print ("Hello Python")
a = 20
b = 20
if a > b:
	#print (str(a) + " is greater " +str(b))
	print("{a} is greater than {b}".format(**{'a': a, 'b': b}))
elif b>a:
	print(str(b) + " is greater "+str(a))
else:
	print ("equal")


n=1
while n<=10:
	print (n)
	n += 1

for n in range(1,11):
	
	print("{}".format(n))


# index: 0 value: 1
# index: 1 value:  2

for i,n in enumerate(range(1,11)):
	print("index:{} value:{}".format(i,n))