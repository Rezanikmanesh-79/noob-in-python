import re
import os
def main():
    while True:
        user_input=input("give a equseion: ")
        if re.match(r"^\d+[+\-*/^%]\d$|clr|off", user_input):
            if "clr" in user_input:
                os.system('cls')
            elif "off" in user_input:
                break
            else:
                print(calculator(user_input))
    
def calculator(uzer_input):
    if "+" in uzer_input:
        my_number=uzer_input.split("+")
        return int(my_number[0])+int(my_number[1])
    elif "-" in uzer_input:
        my_number=uzer_input.split("-")
        return int(my_number[0])-int(my_number[1])
    elif "*" in uzer_input:
        my_number=uzer_input.split("*")
        return int(my_number[0])*int(my_number[1])
    elif "/" in uzer_input:
        my_number=uzer_input.split("/")
        return int(my_number[0])/int(my_number[1])
    elif "%" in uzer_input:
        my_number=uzer_input.split("%")
        return int(my_number[0])%int(my_number[1])
    elif "^" in uzer_input:
        my_number=uzer_input.split("^")
        return pow(int(my_number[0]), int(my_number[1]))
       
if __name__ == "__main__":
    main()