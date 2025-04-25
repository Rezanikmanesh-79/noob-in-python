
from tkinter import Y


def main():
    user_input=input("give me input : ")
    print(compair(user_input))
def compair(user_i):
    z,x,y=user_i.split(',')
    x=int(x)
    y=int(y)
    z=int(z)
    if x>=y>=z:
        return f"{x} , {y}, {z}"
        
    elif x<=y<=z:
        return f"{z} , {y} , {x}"
    elif x<=y<=z:
        return f"{y} , {x} , {z}"
main()