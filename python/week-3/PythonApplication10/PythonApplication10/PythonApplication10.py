def main():
    s=0
    count=0
    while True:
        user_input=int(input("Enter x :"))
        if user_input == 0:
              break        
        s+=user_input
        count+=1

    print(s/count) 
    
main()