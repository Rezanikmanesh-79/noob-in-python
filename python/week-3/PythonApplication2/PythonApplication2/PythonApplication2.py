def main():
    number_of_even=number_of_postive=number_of_fard=number_of_nagtive=0
    
    for i in range(10):
        user_i=int(input("give me namber :"))
        if user_i>0:
            number_of_postive+=1
            if user_i%2==0:
                 number_of_even+=1
            else:
                number_of_fard+=1
        else:
            number_of_nagtive+=1
            if user_i%2==0:
                number_of_even+=1
            else:
                number_of_fard+=1
    print(f"all nagative are :{number_of_nagtive}")
    print(f"all postive are :{number_of_postive}")
    print(f"all even are :{number_of_even}")
    print(f"all odd :{number_of_fard}")
main()