def main():
    user_input=input("give me a input : ")
    print(evener(user_input))
def evener(user_i):
    list_of_even=[]
    x,y=user_i.split(",")
    x=int(x)
    y=int (y)
    if x<y:
           for i in range(x+1,y):
              if i%2==0:
                  list_of_even.append(i) 
    elif x>y :
           for i in range(y+1,x):
              if i%2==0:
                  list_of_even.append(i) 
    else:
        return "not valid"
    return list_of_even
main()