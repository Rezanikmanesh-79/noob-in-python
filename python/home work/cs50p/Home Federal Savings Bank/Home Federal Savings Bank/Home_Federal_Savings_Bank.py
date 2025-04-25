def main():
    user_input=input("Greeting: ")
    print(f"${agent(user_input)}")
def agent(user_i):
    if "hello" in user_i.lower():
        return 0
    elif "h" in user_i.lower():
        return 20
    else:
        return 100
main()
