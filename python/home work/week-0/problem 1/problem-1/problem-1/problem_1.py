def main():
    x=5
    y=3
    problem_solver(x,y)
def problem_solver(x,y):
    sume=x+y
    print(f"sume of x and y is :{sume} ")
    subtraction=x-y
    print(f"subraction x and y is : {subtraction}")
    multiplicataion=x*y
    print(f"multiplicataion x and is : {multiplicataion}")
    divide=x/y
    print (f"x divide y is : {divide}") 
    divided=x//y
    print (f"divided x and y is : {divided}")
    power=pow(x,y)
    print(f"power of x to y : {power}")
    remain_of_dive=x%y
    print(f"remain of x and y {remain_of_dive}")
if __name__=="__main__":
    main()