def main():
    user_input=int(input("user input : "))
    if is_even(user_input):
        print("is even")
    else:
        print("is odd")
        
def is_even(x):
    if x%2==0:
        return True
    else:
        return False
main()
