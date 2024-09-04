# Define a function to print a left-aligned triangle
def left_triangle(rows):
    # Use outer loop to iterate through each row
    for i in range(1, rows + 1):
        # Use inner loop to iterate through each column in the current row
        for j in range(1, rows + 1):
            # Check the condition to print either a star or a space
            if j <= i:
                # Print a star if the column index is less than or equal to the row index
                print("*", end=" ")
            else:
                # Print a space if the column index is greater than the row index
                print(" ", end=" ")    
        # Move to the next line after each row
        print()

# Take input from the user
n = int(input("Enter number of rows: "))
# Call the function to print the left-aligned triangle
left_triangle(n)

# If the input is 12, the output will be:
# *                                       
# * *                                     
# * * *                                   
# * * * *                                 
# * * * * *                               
# * * * * * *                             
# * * * * * * *                           
# * * * * * * * *                         
# * * * * * * * * *                       
# * * * * * * * * * *                     
# * * * * * * * * * * *                   
# * * * * * * * * * * * *                 
