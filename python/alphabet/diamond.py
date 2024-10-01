# Define a function to print a diamond pattern using alphabets
def diamond(rows):
    # Determine the number of columns for the diamond pattern
    columns = rows * 2 - 1  # This ensures the pattern is symmetrical for both even and odd numbers of rows
    
    # Top half of the diamond
    for i in range(1, rows + 1):
        char = chr(64 + i)  # Determine the alphabet to print (A=65 in ASCII)
        for j in range(1, columns + 1):
            # Print the alphabet if within the diamond bounds, otherwise print a space
            if rows - i < j < rows + i:
                print(char, end=" ")  # Print the alphabet
            else:
                print(" ", end=" ")  # Print a space
        # Move to the next line after each row
        print()
    
    # Bottom half of the diamond
    for i in range(rows - 1, 0, -1):
        char = chr(64 + i)  # Determine the alphabet to print (A=65 in ASCII)
        for j in range(1, columns + 1):
            # Print the alphabet if within the diamond bounds, otherwise print a space
            if rows - i < j < rows + i:
                print(char, end=" ")  # Print the alphabet
            else:
                print(" ", end=" ")  # Print a space
        # Move to the next line after each row
        print()

# Take input from the user
n = int(input("Enter number of rows: "))
# Call the function to print the diamond pattern
diamond(n)

# If the input is 8, the output will be:
#               A               
#             B B B             
#           C C C C C           
#         D D D D D D D         
#       E E E E E E E E E       
#     F F F F F F F F F F F     
#   G G G G G G G G G G G G G   
# H H H H H H H H H H H H H H H 
#   G G G G G G G G G G G G G   
#     F F F F F F F F F F F     
#       E E E E E E E E E       
#         D D D D D D D         
#           C C C C C           
#             B B B             
#               A
