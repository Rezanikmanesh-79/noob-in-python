def main():
    user_input=input("give me two number to compair: ")
    print(compair(user_input))
def compair(x):
    y=x.split(",")
    z=int(y[0])
    c=int(y[1])
    if (z!=c):
        if (z>c):
            return ("x grater then y ")
        else:
            return ("y grater then x ")
    else:
        return ("x and y are equal ")

main()