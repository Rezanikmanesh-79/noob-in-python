def main():
    user_input=float(input("give me your cricle r : "))
    print(f"Area of your cricle is : {area_of_cricle(user_input)}")
def area_of_cricle(r):
    pi=3.14
    return pi*pow(r,2)
    
if __name__=="__main__":
    main()
