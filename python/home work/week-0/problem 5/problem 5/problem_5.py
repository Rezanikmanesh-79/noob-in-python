def main():
    user_input=input("give me two number : ")
    print(f"your avrage : {avrage(user_input)}")

def avrage(user_i):
    x,y=user_i.split(",")
    x=int(x)
    y=int(y)
    return (x+y)/2
if __name__=="__main__":
    main()