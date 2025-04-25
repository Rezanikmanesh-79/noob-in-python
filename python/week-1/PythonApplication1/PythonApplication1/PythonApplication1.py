def main():
    user_input=input("give me string :").lower()
    string_chaker(user_input)
def string_chaker(user_i):
    if "hi"in user_i:
        print("Exist")
    else:
        print("not exist ")            
if __name__=="__main__":
    main()
