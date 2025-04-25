def main():
    sume=mazrab_9=mazrab_6=mazrab_7=0
    for i in range(10):
        user_input=int(input("give me a int : "))
        if user_input%6==0:
            mazrab_6+=1
        if user_input%7==0:
            mazrab_7+=1
        if user_input%9==0:
            mazrab_9+=1
        sume+=user_input
    print(f"avrage is : {sume/10} marab 6 is : {mazrab_6} mazrab7 is : {mazrab_7} mazrab 9 is:{mazrab_9} ")
        
main()