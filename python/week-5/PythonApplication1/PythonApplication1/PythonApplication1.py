def main():
    user_input=int(input("give me an int : "))
    print(type_of_my_number(user_input))
def type_of_my_number(user_input):
    if user_input>0:
        return "positive"
    elif user_input<0:
        return "nagtive"
    else:
        return "is zero"
main()