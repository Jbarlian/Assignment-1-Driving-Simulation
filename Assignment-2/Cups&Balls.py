ball =[1, 0, 0]


def trick(option):
    if option == "A":
        # Swaps the left cup with the middle cup
        ball[0], ball[1] = ball[1], ball[0]
    elif option == "B":
        # Swaps the middle cup with the right cup
        ball[1], ball[2] = ball[2], ball[1]
    elif option == "C":
        # Swaps the right cup with the left cup
        ball[0], ball[2] = ball[2], ball[0]


# Uses the function above to swap the cups with the input given
for x in list(input()):
    trick(x)

print(ball.index(1)+1)