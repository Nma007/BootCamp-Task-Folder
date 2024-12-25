# Create an empty list to store numbers under variable name user_num
user_num = []

#Countinually request an integer input from user
#Store the numbers under variable name num
num = int(input("Enter number (or-1 to stop): "))
while num != -1: #Continue until -1 is entered
    user_num .append(num)  #Add number to list
    num = int(input("Enter number (or-1 to stop): "))

#Check if the user entered '0' as it is a valid number
#Let the user know it is not valid
#Skip the rest of the loop and prompt user again

    if num == 0:
        print("0 is not valid, try again")
        num = int(input("Enter number (or-1 to stop): "))
        user_num.append(num)

#Exit loop when '-1' is entered
if num == -1:
    print(f" Your numbers are: {user_num}")

# Calculate average of valid numbers entered
#Store under variable name avg
avg = sum(user_num)/len(user_num)
print(f"Average of numbers you entered is: {avg}")





    
