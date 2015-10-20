# python learning exercises

# Functions
def echo(thing):
	return thing

def swap(thing1, thing2):
	return thing2, thing1


def main_function():
	print "testing echo('marco'): ", echo('marco')
	print "testing echo('shut up'): ", echo('no, you shut up')
	print "testing swap('fame', 'fortune'): ", swap('fame', 'fortune')


#Arithmetic Function
def reverse(x):
	return -x

def plus(y, z):
	return y + z

def diff(x, y):
	return x - y
	
def abs_diff(d, b):
	

def main_arithmetic():
	print "test reverse(3): ", reverse(3)
	print "test reverse(-3): ", reverse(-3)
	print "test plus(1, 1): ", plus (1, 1)
	print "test plus(2, 3): ", plus (2, 3)
	


def main():
	main_function()
	main_arithmetic()

main()