def main():
    user_input=int(input("give me your age : "))
    age_convertor(user_input)
def age_convertor(age):
    year=365
    day=24
    hure=age*year*day
    minet=hure*60
    sec=60*minet
    print(f"Hours= {hure}")
    print(f"Min= {minet}")
    print(f"Sec= {sec}")
    
main()