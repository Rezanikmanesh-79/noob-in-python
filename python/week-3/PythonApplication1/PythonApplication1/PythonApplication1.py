def main():
    user_input=int(input("give me a int : "))
    print(f"fact {user_input} is {factsolver(user_input)}")
def factsolver(user_i):
    f=1
    for i in range(1,user_i+1):
        f*=user_i
    return f
main()
