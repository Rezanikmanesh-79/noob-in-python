from lib import compair
def main():
    user_input=input("give me two number to compair : ")
    if (compair(user_input)=="is equil "):
        print(user_input)
    elif(compair(user_input)=="is biger then "):
        print(user_input[0])
    else:
        print(user_input[2])

if __name__=="__main__":
    main()
