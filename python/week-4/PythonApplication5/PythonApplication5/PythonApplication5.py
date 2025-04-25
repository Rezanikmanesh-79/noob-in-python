def main():
    stu()
def stu():
    s=0
    for i in range(5):
        ts=0
        for j in range(4):
            user_input=int(input(f"give me score {j+1} of student {i+1} : "))
            s+=user_input
            ts+=user_input
        print(f"avrage of student {i+1} :{ts/4} ")
    print(f"total avrage is {s/20}")
main()
