def main():
    user_input=input("give an equsen : ")
    print (calculator(user_input))
def calculator(us_i):
    if "+" in us_i:
        x=us_i.split("+")
        z=int(x[0])
        c=int(x[1])
        return(f"x+y ={z+c}")
    if "-" in us_i:
        x=us_i.split("-")
        z=int(x[0])
        c=int(x[1])
        return(f"x-y ={z-c}")
    if "*" in us_i:
        x=us_i.split("*")
        z=int(x[0])
        c=int(x[1])
        return(f"x*y ={z*c}")
    if "/" in us_i:
        x=us_i.split("/")
        z=int(x[0])
        c=int(x[1])
        return(f"x/y ={z/c}")
    if "^" in us_i:
        x=us_i.split("^")
        z=int(x[0])
        c=int(x[1])
        return(f"x^y ={z**c}")
    if "%" in us_i:
        x=us_i.split("%")
        z=int(x[0])
        c=int(x[1])
        return(f"x^y ={z%c}")
    
main()