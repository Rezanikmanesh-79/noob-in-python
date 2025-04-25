def main():
    user_input=int(input("give me a int to reverse : "))
    print(f"Reverse {user_input} is {reverse_int(user_input)}")
def reverse_int(x):
    ten=x//10
    one=x%10
    return(one*10)+ten
main()