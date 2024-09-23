# Define a function to print a right-down triangle pattern using stars
def right_down_triangle(rows):
    # Loop through each row
    for i in range(1, rows + 1):
        # Loop through each column in the current row
        for j in range(1, rows + 1):
            # Print a space if the column index is less than the current row index, otherwise print a star
            if j < i:
                print(" ", end=" ")
            else:
                print("*", end=" ")
        # Move to the next line after each row
        print()

# Take input from the user
n = int(input("Enter number of rows: "))
# Call the function to print the right-down triangle
right_down_triangle(n)

# If the input is 12, the output will be:
# * * * * * * * * * * * * 
#   * * * * * * * * * * * 
#     * * * * * * * * * * 
#       * * * * * * * * * 
#         * * * * * * * * 
#           * * * * * * * 
#             * * * * * * 
#               * * * * * 
#                 * * * * 
#                   * * * 
#                     * * 
#                       *
