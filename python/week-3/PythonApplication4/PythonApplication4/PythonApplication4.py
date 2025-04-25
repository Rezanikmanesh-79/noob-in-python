def main():
    user_input=int(input("give me a int : "))
    febonachi(user_input)
    
def febonachi(user_i):
    f1,f2=0,1
    print (f1,f2,end=",")
    for i in range(2,user_i+1):
        f=f1+f2
        print(f,end=",")
        f1,f2=f2,f
    print()
main()