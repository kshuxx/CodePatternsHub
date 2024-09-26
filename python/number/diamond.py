# Define a function to print a diamond pattern using numbers
def diamond(rows):
    # Determine the number of columns for the diamond pattern
    columns = rows * 2 - 1  # This ensures the pattern is symmetrical for both even and odd numbers of rows
    
    # Top half of the diamond
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            # Print a number if within the diamond bounds, otherwise print a space
            if rows - i < j <= rows + i - 1:
                print(i, end=" ")  # Print the current row number
            else:
                print(" ", end=" ")  # Print a space
        # Move to the next line after each row
        print()
    
    # Bottom half of the diamond
    for i in range(rows - 1, 0, -1):
        for j in range(1, columns + 1):
            # Print a number if within the diamond bounds, otherwise print a space
            if rows - i < j <= rows + i - 1:
                print(i, end=" ")  # Print the current row number
            else:
                print(" ", end=" ")  # Print a space
        # Move to the next line after each row
        print()

# Take input from the user
while True:
    n = int(input("Enter number of rows (1-9): "))
    if 1 <= n <= 9:
        break
    else:
        print("Please enter a number between 1 and 9.")

# Call the function to print the diamond pattern
diamond(n)

# If the input is 8, the output will be:
#               1               
#             2 2 2             
#           3 3 3 3 3           
#         4 4 4 4 4 4 4         
#       5 5 5 5 5 5 5 5 5       
#     6 6 6 6 6 6 6 6 6 6 6     
#   7 7 7 7 7 7 7 7 7 7 7 7 7   
# 8 8 8 8 8 8 8 8 8 8 8 8 8 8 8 
#   7 7 7 7 7 7 7 7 7 7 7 7 7   
#     6 6 6 6 6 6 6 6 6 6 6     
#       5 5 5 5 5 5 5 5 5       
#         4 4 4 4 4 4 4         
#           3 3 3 3 3           
#             2 2 2             
#               1