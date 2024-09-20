def print_even_square(rows):
    # Ensure the number of rows is even
    if rows % 2 != 0:
        rows += 1  # If odd, increase by 1 to make it even
    
    # Loop through each row
    for i in range(1, rows + 1):
        # Loop through each column in the current row
        for j in range(2, 2 * rows + 1, 2):  # Print even numbers
            print(j, end=" ")
        # Move to the next line after each row
        print()

# Take input from the user
while True:
    n = int(input("Enter number of rows (even number preferred): "))
    if 1 <= n <= 9:
        break
    else:
        print("Please enter a number between 1 and 9.")

# Call the function to print the even square
print_even_square(n)

# If the input is 8, the output will be:
# 2 4 6 8 10 12 14 16
# 2 4 6 8 10 12 14 16
# 2 4 6 8 10 12 14 16
# 2 4 6 8 10 12 14 16
# 2 4 6 8 10 12 14 16
# 2 4 6 8 10 12 14 16
# 2 4 6 8 10 12 14 16
# 2 4 6 8 10 12 14 16
