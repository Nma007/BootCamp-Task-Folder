# Get number of rows from user using input
# Cast string to integer
# Save in variable name rows
rows = int(input("Enter the number rows of the pattern : "))

# Step 2: Use a for loop to create the upper half of the triangle
for i in range(1, rows + 1):  # Loop from 1 to rows 
    if i % 2 >=0:       #If number is more than 0
     print("*" * i)  # Print i stars in each row

# Step 3: Use another for loop to create the lower inverted half of the triangle
else:
    for i in range(rows - 1, 0, -1):  # Loop from height-1 down to 1
     print("*" * i)  # Print i stars in each row