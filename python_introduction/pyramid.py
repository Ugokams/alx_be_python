rows = 5
i = 1

while i <= rows:
    # Print spaces
    space = 1
    while space <= rows - i:
        print(" ", end="")
        space += 1

        # Print stars
        star = 1
        while star <= (2 * i - 1):
            print("*", end="")
            star += 1

    print()  # Move to next line after each row
    i += 1
