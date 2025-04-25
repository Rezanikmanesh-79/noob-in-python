def main():
    print(my_power(2,4))
def my_power(x,m=2):
    f=1
    for i in range(m):
        f*=x
    return f
        
main()