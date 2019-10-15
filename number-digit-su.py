# number = int(raw_input("enter the number :"))
# sum =0
# while(number!=0):
# 	sum = sum + (number%10)
# 	number = number/10

# print sum

# Checks a prime Number

# number = int(raw_input('enter number to check wheather it is prime or not:'))
# for i in range(2,(number//2 +1)):
# 	pass
# if(number%i==0):
# 		print 'number is not prime'
# else:
#     print 'number is prime'	

# Genrate the random number
# import random
# list = [1,2,3]
# number = random.choice(list)
# print number


 # Remove duplicates from the list  
     
# mylist = ['a','b','a','c','d','b']
# changed_list = list(dict.fromkeys(mylist))
# print changed_list

# def my_function(mylist):
# 	return list(dict.fromkeys(mylist))

# mylist = ['a','b','a','c','d','b']
# print my_function(mylist)

# Reverse a string

test_string = raw_input('Enter the string for Reverse and check it is palindrom or not: ')
my_string = test_string [::-1]
print my_string
if(test_string == my_string):
	print 'this string is palindrom'
else:
    print 'this string is not palindrom'	