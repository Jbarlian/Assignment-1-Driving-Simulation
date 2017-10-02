name = input().split("-")  # Splits the string by a "-"
initials = []


def aids():

        for i in name:
                # Appends the first letter of the string(s).
                initials.append(i[0])

        # Temp variable representing blank space
        abc = ""

        for i in initials:
                abc = abc + i

        print(abc.upper())


aids()
