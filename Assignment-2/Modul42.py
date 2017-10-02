def module42 (): #

    list = []

    for x in range(0,10):
        number = int(input("Enter number: "))
        # Find the modulus of the number inserted
        result = number % 42
        # Adds the result to the list
        list.append(result)
    # Prints the list according to its length and the set reduces any duplicate answers.
    print(len(set(list)))

module42()