# Define a function to print a reverse pyramid pattern using stars
def reverse_pyramid(n):
    # Calculate the total number of columns
    col = n * 2 - 1

    # Use outer for loop for rows
    for i in range(n):
        # Use inner for loop for columns / stars
        for j in range(col):
            # Checking the conditions to print space or star
            if j >= i and j < col - i:
                # Print stars in each row
                print("*", end=" ")
            else:
                # Print spaces in each row
                print(" ", end=" ")
        # End of line after each row
        print()

# Taking input from user
n = int(input("Enter number of rows: "))
# Calling function
reverse_pyramid(n)
# If the input is 7, the output will be:
# * * * * * * * * * * * * * 
#   * * * * * * * * * * * 
#     * * * * * * * * * 
#       * * * * * * * 
#         * * * * * 
#           * * * 
#             * 
