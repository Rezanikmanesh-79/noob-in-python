def main():
    user_input=input("give me tow nubmer to compair : ")
    print(f"x is {compair(user_input)}  ")
    
def compair(user_i):
    x,y=user_i.split(",")
    x=int(x)
    y=int(y)
    if(x!=y):
        if (x>y):
            return f"is biger then so x-y = {x-y}"
        else:
            return f"is smaller then so x+1 ={x+1} "
    else:
        return f"they are equil so x^y={pow(x,y)}  "
if __name__=="__main__":
    main()