a = int(raw_input('Enter first Number '))
b = int(raw_input('Enter Second Number '))
def gcd(a,b):
	if(b==0):
		return a
	return gcd(b,a%b)	
 	
print 'gcd of number', a, 'and', b ,'is : ', gcd(a,b)
