pattern_size = int(input("Enter the size of the pattern: "))
counter = 1
while counter <= pattern_size:
    for j in range(0, pattern_size):
        print ("*", end = " ")
    counter += 1
    print ()