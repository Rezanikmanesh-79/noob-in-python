def main():
    user_input=input("give me tow number : ")
    print (comaoir(user_input))
def comaoir(user_i):
    x,y=user_i.split(",")
    x=int(x)
    y=int(y)
    if (x==y):
        return "they are even "
    elif x>y:
        return x,y
    else:
        return y,x
    
main()
