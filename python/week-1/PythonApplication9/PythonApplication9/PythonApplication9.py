def main():
    user_input=int(input("Give me a int : "))
    print(promblem_solver(user_input))
def promblem_solver(x):
    ten=x//10
    one=x%10
    return f"ten^one is :{ten**one}   one^ten is : {one**ten}"
    
main()