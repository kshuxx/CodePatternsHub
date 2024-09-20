# Define a function to print a pyramid
def pyramid(n):
    # Determine the number of columns for the pyramid pattern
    col = 2 * n - 1  # This ensures the pattern is symmetrical for both even and odd numbers of rows

    # Use outer for loop for rows
    for i in range(1, n + 1):
        # Use inner for loop for columns / stars
        for j in range(1, col + 1):
            # Check the conditions to print space or star
            if n + 1 - i <= j <= n - 1 + i:
                # Print stars in each row
                print("*", end=" ")
            else:
                # Print spaces in each row
                print(" ", end=" ")
        # Move to the next line after each row
        print()

# Take input from the user
n = int(input("Enter number of rows: "))
# Call the function to print the pyramid pattern
pyramid(n)

# If the input is 8, the output will be:
#               * 
#             * * * 
#           * * * * * 
#         * * * * * * * 
#       * * * * * * * * * 
#     * * * * * * * * * * * 
#   * * * * * * * * * * * * * 
# * * * * * * * * * * * * * * *
