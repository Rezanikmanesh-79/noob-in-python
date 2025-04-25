def main():
    user_input=input("Give me x y z to chack it is try angel  : ")
    if is_it_try_angel(user_input):
        print ("it is ")
    else:
        print("sorry its not")
def is_it_try_angel(user_i):
    x,y,z=user_i.split(",")
    x=int(x)
    y=int(y)
    z=int(z)
    if (x+y>z)and(x+z>y)and(z+y>x):
        return True
    else:
        return False
main()
