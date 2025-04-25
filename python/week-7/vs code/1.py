from os import path
def main():
    if path.exists("1.txt"):
        a=int(input("please enter an int : "))
        factorial(a)
        fibo(a)
        star_print(a)
def factorial(a):
    s=1
    myFile=open("1.txt","a")
    myFile.write("factorial is : \n")
    for i in range(1,a+1):
        s=s*i
    myFile.write(str(s)+"\n")
    myFile.close
def fibo(a):
    myFile=open("1.txt","a")
    f1=1
    f2=1
    myFile.write("febonachi : \n")
    myFile.write(str(f1))
    myFile.write(str(f2))
    for i in range(2,a+2):
        f3=f1+f2
        myFile.write(str(f3))
        f1=f2
        f2=f3
        myFile.write("\n")
    
    myFile.close()

def star_print(a):
    myFile=open("1.txt","a")
    myFile.write("star maker : \n")
    for i in range(1,a+1):
        myFile.write("*"*i+"\n")
    myFile.close()
main()
