def main():
    user_input=int(input("give me input: "))
    is_bakhsh(user)
def is_bakhsh(user_i):
    for i in range(1,user_i):
        if user_i%i==0:
            print(i)
main()