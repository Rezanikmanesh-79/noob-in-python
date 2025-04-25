def main():
    user_input=input("give me tow nubmer to compair : ")
    print(f"x is {compair(user_input)} y ")
    
def compair(user_i):
    x,y=user_i.split(",")
    x=int(x)
    y=int(y)
    if(x!=y):
        if (x>y):
            return "is biger then "
        else:
            return"is smaller then "
    else:
        return "equil to "
if __name__=="__main__":
    main()