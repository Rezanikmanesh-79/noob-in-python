def main():
    user_input=input("give me two number to for problem: ")
    print(problem_solver(user_input))
def problem_solver(x):
    y=x.split(",")
    z=int(y[0])
    c=int(y[1])
    if (z!=c):
        if (z>c):
            return (f"x grater then y so x-y : {z-c}")
        else:
            return (f"y grater then x so x+1 : {z+1}")
    else:
        return (f"x and y are equal so x^y : {pow(c,z)}")

main()