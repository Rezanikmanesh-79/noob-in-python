def main():
    user_input=int(input("give me a int : "))
    while user_input>0:
        d=user_input%10
        user_input//=10
        print(d,end=' ')
main()


