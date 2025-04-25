a=input("plse givr me your name : ")
for i in range(0,len(a)):
    if a[i]==" ":
        a=a[i+1].upper()+a[i+2:] +","+a[0].upper()+a[1:i]
print(a)
        
