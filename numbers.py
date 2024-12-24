#Request input(numbers) from user and save under variable name user_num1, user_num2, user_num3
#Cast the numbers from string format to float, to allow for integers and decimals
#Save them using the variable names nuser_num1, nuser_num2, nuser_3
user_num1 = input("Enter number: ")
nuser_num1 = float(user_num1)
user_num2 = input("Enter a new number: ")
nuser_num2 = float(user_num2)
user_num3 = input("Enter another number:" )
nuser_num3 = float(user_num3)

#Print the sum of all the numbers and save under variable name total
total = nuser_num1 + nuser_num2 + nuser_num3
print(f"If you add {nuser_num1}, {nuser_num2} and {nuser_num3} you get: {total}")

#Subtract the second number, nuser_num2 from the first number nuser_num1 
#Save result under variable name difference
difference = nuser_num1 - nuser_num2
print(f"Your answer is: {difference}")

#Find the product of the first number, nuser_num1 and the third number nuser_num3
#Save result under variable name product
product = nuser_num3 * nuser_num1
print(f"The product of {nuser_num3} and {nuser_num1} is: {product}")

#Find the sum of all three numbers and divide it using the third number
#save answer under variable name ans
ans = (nuser_num1 + nuser_num2 + nuser_num3)/ nuser_num3
print(f"When to add {nuser_num1}, {nuser_num2}, {nuser_num3} and divide by {nuser_num3}, you get: {ans}")