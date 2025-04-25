def main():
    x,y=input("give me two number: ").split('+')
    x=int(x)
    y=int(y)
    print(add(x,y))
def add(x,y):
    return x+y

main()