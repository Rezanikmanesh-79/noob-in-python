def main():
    user_input=int(input(("give me int : ")))
    rev_r(user_input)
def rev_r(user_i):
    count=0
    while user_i>0:
        my_rev=(user_i%10)
        user_i=user_i//10
        print(my_rev,end=' ')
        count+=1
    print("\n",count)
        
main()