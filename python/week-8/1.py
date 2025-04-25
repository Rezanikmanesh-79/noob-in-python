def main():
    score=[]
    x=0
    for i in range(10):
        user_input=int(input(f"give me your {i}st score : "))
        score.append(user_input)
        x+=score[i]
    print(f"you avrage is : {x/10}")
main()