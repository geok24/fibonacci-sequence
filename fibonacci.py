non = 10 #NUMBER OF NUMBERS
a = 0 
b = 1
c = 0
print ("1") 
for i in range (non):
	c = b + a
	a = b
	b = c
	print (c)
