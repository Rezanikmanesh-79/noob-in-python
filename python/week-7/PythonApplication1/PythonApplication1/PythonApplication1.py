def main():
    import os.path
    import math
    user_input=int(input("pleas enter an intger : "))
    if os.path.isfile("C:\\Users\\rezan\\Desktop\\python\\week-7\\PythonApplication1\\PythonApplication1\\1.txt"):
        print("File exists")
        #op
        f=open("C:\\Users\\rezan\\Desktop\\python\\week-7\\PythonApplication1\\PythonApplication1\\1.txt","a")
        f.write(f"your fact is :{math.factorial(user_input)}\n")
        f.write(f"your feb is :{fibonacci(user_input)}\n")
        for i in range(1, user_input + 1):
			      f.write(" " * (user_input - i) + "*" * i + "\n")		
				  
def fibonacci(n):
	a = 0
	b = 1
	
	# Check is n is less
	# than 0
	if n < 0:
		print("Incorrect input")
		
	# Check is n is equal
	# to 0
	elif n == 0:
		return 0
	
	# Check if n is equal to 1
	elif n == 1:
		return b
	else:
		for i in range(1, n):
			c = a + b
			a = b
			b = c
		return b


main()