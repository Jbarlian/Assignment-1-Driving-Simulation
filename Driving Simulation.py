#Output each second distance travelled with stars
#If the person went over the speed limit
#If reached the destination

time_driving = int(input("Enter time: "))
acceleration = int(input("Enter speed: "))
distance = int(input("Enter distance: "))

for x in range(0,11):
    d = ((acceleration*(x**2))/2)//10
    print("Duration:",x, "Distance: ", "*" * int(d))

y = acceleration*time_driving
z = (acceleration*(time_driving**2))/2

if y > 60:
    print("\nThe person went over the speed limit! Reached,", y, "m/s \n")
else:
    print("\nThe person did not go over the speed limit. Reached,", y, "m/s \n ")

if z >= int(distance):
    print("The person reached their destination. Distance reached:", z, "meters")
else:
    print("The person did not reach their destination. Distance reached:", z, "meters")
