def main():
    for i in range(10000,100000):
        if rev_r(i)==i:
            print(i)

def rev_r(user_i):
    count=0
    while user_i>0:
        my_rev=(user_i%10)
        count=count*10+my_rev
        user_i=user_i//10
    return count
        
main()