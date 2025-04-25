def main():
    for i in range(10000,100000):
        x=i
        m=0
        while x>0:
            d=x%10
            x//=10
            m=m*10+d
        if i==m:
            print(i)
main()