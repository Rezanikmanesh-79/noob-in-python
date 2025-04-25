def main():
    l=[]
    x=0
    while True:
        user_input=input("give me your score: ")
        if user_input=='x':
            break
        else:
             user_input=int(user_input)
             l.append(user_input)
             x+=int(user_input)
    if (len(l))>0:
        print(f"your avrage is : {x/(len(l))}")
main()