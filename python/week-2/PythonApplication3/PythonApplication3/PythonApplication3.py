def main():
    f=[]
    x,y=input("give an int : ").split(",")
    x=int(x)
    y=int (y)
    if x<y:
           for i in range(x+1,y):
                print(f"your number is : {i}")
                f.append(i)
    elif x>y :
             for i in range(y+1,x):
                print(f"your number is : {i}") 
    else:
        print("input not valid")
    print (f)
main()
