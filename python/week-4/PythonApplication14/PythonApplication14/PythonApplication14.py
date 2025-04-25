def main():
    x,y=input("give me two number to compair : ").split(',')
    x,y=int(x),int(y)
    print(compair_if_two_number(x,y))
def compair_if_two_number(x,y):
    if x!=y:
        if x>y:
            return x
        else:
            return y
    else:
        return "two number are equial "
main()