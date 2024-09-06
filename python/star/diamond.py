# Define a function to print a diamond pattern using stars
def diamond(rows):
    # Determine the number of columns for the diamond pattern
    columns = rows * 2 - 1  # This ensures the pattern is symmetrical for both even and odd numbers of rows
    
    # Top half of the diamond
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            # Print a star if within the diamond bounds, otherwise print a space
            if rows - i < j <= rows + i - 1:
                print("*", end=" ")  # Print a star
            else:
                print(" ", end=" ")  # Print a space
        # Move to the next line after each row
        print()
    
    # Bottom half of the diamond
    for i in range(rows - 1, 0, -1):
        for j in range(1, columns + 1):
            # Print a star if within the diamond bounds, otherwise print a space
            if rows - i < j <= rows + i - 1:
                print("*", end=" ")  # Print a star
            else:
                print(" ", end=" ")  # Print a space
        # Move to the next line after each row
        print()

# Take input from the user
n = int(input("Enter number of rows: "))
# Call the function to print the diamond pattern
diamond(n)

# If the input is 8, the output will be:
#               *               
#             * * *             
#           * * * * *           
#         * * * * * * *         
#       * * * * * * * * *       
#     * * * * * * * * * * *     
#   * * * * * * * * * * * * *   
# * * * * * * * * * * * * * * * 
#   * * * * * * * * * * * * *   
#     * * * * * * * * * * *     
#       * * * * * * * * *       
#         * * * * * * *         
#           * * * * *           
#             * * *             
#               *
