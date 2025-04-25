def main():
    user_input=int(input("give me int : "))
    print(fact_solver(user_input))
def fact_solver(n):
    i=1
    f=1
    while i<n+1:
        f*=i
        i+=1  
    return f
main()