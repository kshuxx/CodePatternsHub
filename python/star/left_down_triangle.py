# Define a function to print a left-down triangle pattern
def left_down_triangle(rows):
    # Loop through each row
    for i in range(1, rows + 1):
        # Loop through each column in the current row
        for j in range(1, rows + 1):
            # Print a star if the column index is less than or equal to rows - i + 1, otherwise print a space
            if j <= rows - i + 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        # Move to the next line after each row
        print()

# Take input from the user
n = int(input("Enter number of rows: "))
# Call the function to print the left-down triangle
left_down_triangle(n)

# If the input is 12, the output will be:
# * * * * * * * * * * * * 
# * * * * * * * * * * *   
# * * * * * * * * * *     
# * * * * * * * * *       
# * * * * * * * *         
# * * * * * * *           
# * * * * * *             
# * * * * *               
# * * * *                 
# * * *                   
# * *                     
# *                       
