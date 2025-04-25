def main():
    user_input=input("give me two number to multi :")
    print(multi(user_input))
def multi(user_i):
    x,y=user_i.split('.')
    x=int(x)
    y=int(y)
    z=0
    for i in range (y):
        z+=x
    return(z)
main()