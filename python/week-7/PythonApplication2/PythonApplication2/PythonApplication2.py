from os import path
def main():
    print(factorial(5))
def factorial(a):
    s=1
    for i in range(1,a+1):
        s=s*i
    print(a)
main()
