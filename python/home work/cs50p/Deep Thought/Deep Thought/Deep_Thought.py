def main():
    user_input=input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    print(Answer(user_input))
def Answer(user_i):
    if "42" in user_i:
        return "yes"
    elif "forty-two" in user_i.lower():
        return "yes"
    elif "forty two" in user_i.lower():
        return "yes"
    else:
        return "no"
main()