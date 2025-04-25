def main():
    mylist = []
    while True:
        user_input = int(input())
        if 10 <= user_input <= 90:
            mylist.append(user_input)
        elif user_input <= 0:
            mylist.sort()  
            print(mylist[-1]) 
            break

main()
