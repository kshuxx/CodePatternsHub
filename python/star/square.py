# Define a function to print a square pattern using stars
def square(rows):
    # Loop through each row
    for i in range(rows):
        # Loop through each column in the current row
        for j in range(rows):
            print("*", end=" ")  # Print a star
        # Move to the next line after each row
        print()

# Take input from the user
n = int(input("Enter number of rows: "))
# Call the function to print the square pattern
square(n)

# If the input is 7, the output will be:
# * * * * * * * 
# * * * * * * * 
# * * * * * * * 
# * * * * * * * 
# * * * * * * * 
# * * * * * * * 
# * * * * * * * 
