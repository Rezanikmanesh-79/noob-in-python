def main():
    list_mahgsom=[]
    list_adad=[]
    list_biggest=[]
    for i in range(20):
        user_input=int(input())
        list_mahgsom.append(mahgsom(user_input))
        list_adad.append(user_input)
    sorted_mahgsom = sorted(list_mahgsom)
    for i in range(len(list_adad)):
        if sorted_mahgsom[-1] == list_mahgsom[i]:
            x=(list_mahgsom[i])
            list_biggest.append(list_adad[i])

    if len(list_biggest)==1:
        print(f"{list_biggest[0]} {x}")
    elif len(list_biggest)>1:
        list_biggest=sorted(list_biggest)
        print(f"{list_biggest[-1]} {x}")
def mahgsom(x):
    j=0
    for i in range(1,x+1):
        if x%i==0:
            j+=1
    return j
main()