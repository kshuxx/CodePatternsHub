def right_down_triangle(rows):
    # Loop through each row
    for i in range(1, rows + 1):
        # Print leading spaces
        for _ in range(i - 1):
            print(" ", end=" ")
        # Loop through each column in the current row
        for j in range(1, rows - i + 2):
            # Print the number
            print(j, end=" ")
        # Move to the next line after each row
        print()

# Take input from the user
while True:
    n = int(input("Enter number of rows (1-9): "))
    if 1 <= n <= 9:
        break
    else:
        print("Please enter a number between 1 and 9.")

# Call the function to print the right-down triangle
right_down_triangle(n)

# If the input is 8, the output will be:
# 1 2 3 4 5 6 7 8
#   1 2 3 4 5 6 7
#     1 2 3 4 5 6
#       1 2 3 4 5
#         1 2 3 4
#           1 2 3
#             1 2
#               1
