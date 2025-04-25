def main():
    user_input=int(input("give me an int : "))
    print(abs1(user_input))
def abs1(x):
    if x<0:
        x*=-1
    return x

main()