def pyramid(n):
    # Determine the number of columns for the pyramid pattern
    if n % 2 == 0:
        col = int(n * 2 - 1)  # For even numbers of rows
    else:
        col = int(n * 2)  # For odd numbers of rows

    # Use outer for loop for rows
    for i in range(1, n + 1):
        # Use inner for loop for columns / numbers
        for j in range(1, col + 1):
            # Check the conditions to print space or number
            if n + 1 - i <= j <= n - 1 + i:
                # Print numbers in each row
                print(i, end=" ")
            else:
                # Print spaces in each row
                print(" ", end=" ")
        # Move to the next line after each row
        print()

# Take input from the user
while True:
    n = int(input("Enter number of rows (1 to 9): "))
    if 1 <= n <= 9:
        break
    else:
        print("Invalid input. Please enter a number between 1 and 9.")

# Call the function to print the pyramid pattern
pyramid(n)

# If the input is 7, the output will be:
#              1 
#            2 2 2 
#          3 3 3 3 3 
#        4 4 4 4 4 4 4 
#      5 5 5 5 5 5 5 5 5 
#    6 6 6 6 6 6 6 6 6 6 6 
#  7 7 7 7 7 7 7 7 7 7 7 7 7 
