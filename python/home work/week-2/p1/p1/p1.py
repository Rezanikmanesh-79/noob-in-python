def main():
    user_input=input("give me input : ")
    print(compair(user_input))
def compair(user_i):
    x,y=user_i.split(',')
    x=int(x)
    y=int(y)
    if x>y:
        return f"{x} , {y}"
    elif x<y:
        return f"{y} , {x}"
    else:
        return "equal"
main()