def main():
    n=int(input("give me n : "))
    for i in range(1,n+1):
        for j in range(i):
            print("*",end='')
        print()
main()