def main():
    while True:
        x = int(input("Enter Number: "))
        # Even numbers = Bob Wins
        if x % 2 == 0:
            print("Bob")
            continue
        # Odd numbers = Alice Wins
        if x % 2 != 0:
            print("Alice")
            continue


main()