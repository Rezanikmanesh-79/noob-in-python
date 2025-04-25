def main():
    for i in range (10,100):
        revers_i=(i//10)+((i%10)*10)
        if revers_i==i:
            print(f"{i} is equial to {revers_i}")
main()