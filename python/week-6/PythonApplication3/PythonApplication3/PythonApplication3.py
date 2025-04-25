def main():
    while True:
        user_input=input("give me a number : ")
        if user_input.lower()=="x":
            print("off")
            break
        user_input=int(user_input)
        for i in range(1,user_input+1):
            print(" "*(user_input-i)+"*"*i)
main()