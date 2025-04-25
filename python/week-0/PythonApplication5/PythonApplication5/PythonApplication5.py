def main():
    user_input=input("give me two number to compair: ")
    print(compair(user_input))
def compair(x):
    y=x.split(",")
    z=int(y[0])
    c=int(y[1])
    if (z!=c):
        if (z>c):
            return (f"x grater then y so : {z}")
        else:
            return (f"y grater then x so : {c}")
    else:
        return ("x and y are equal ")
main()