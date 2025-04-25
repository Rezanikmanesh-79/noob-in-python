def main():
    user_input=input("give me two number : ")
    print(f"avrage is :{avrage(user_input)}")
def avrage(m):
    z=m.split(",")
    return ((int(z[0])+int(z[1]))/2)
if __name__ == "__main__":
    main()