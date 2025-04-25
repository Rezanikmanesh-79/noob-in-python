def main():
    user_input = input("give me two numbers to multi (separated by space): ")
    print(taavan(user_input))

def multi(x, y):
    z = 0
    for i in range(y):
        z += x
    return z

def taavan(user_i):
    x, y = user_i.split()
    x = int(x)
    y = int(y)
    z = 1
    for i in range(y):
        z = multi(z, x)
    return z

main()
