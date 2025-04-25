def main():
    user_input=int(input("Give me an int : "))
    print(f"your number is {number_chaker(user_input)}")
def number_chaker(x):
    if x>0:
        return "psitive"
    elif x<0:
        return "nagative"
    else:
        return "zero"
    
main()
