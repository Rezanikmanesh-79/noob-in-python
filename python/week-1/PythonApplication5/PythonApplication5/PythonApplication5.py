def main():
    user_input=input("give me x and y to solve : ")
    print (f"your answer is : {equsion_solver(user_input)}")
def equsion_solver(user_i):
    x,y=user_i.split(",")
    x=int(x)
    y=int(y)
    z=(x**3)+2*(x**2*y)+3*y-7
    return z
main()