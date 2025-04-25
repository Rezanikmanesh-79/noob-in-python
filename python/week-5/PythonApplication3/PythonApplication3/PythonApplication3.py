def main():
    user_input = input("camelCase: ")
    print(snake(user_input))

def snake(user_input):
    y = ''
    for i in range(len(user_input)):
        char = user_input[i]
        if char.isupper() and i != 0:
            y += '_' + char.lower()
        else:
            y += char.lower()
    return y

main()
