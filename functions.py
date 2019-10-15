# def printme(string):
# 	pass
# 	print string
# 	return
# printme('hello')	
import support
def changeme(mylist):
	mylist.append([1,2,3,4])
	print 'mylist inside the function', mylist
	return
mylist = [10,20,30]
changeme(mylist)
print 'mylist outside the function', mylist	

support.print_name('monika')