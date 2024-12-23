#Request input from user, save input under variable name str_manip

str_manip = input("Write a sentence: ")

#Calculate and display the length of str_manip using the len function
print(len(str_manip))
#Find the last letter in str_manip and save under variable name letter1
letter1 = str_manip[-1]
print(letter1)
#Replace every occurence of variable letter1 with @ using replace method
new_char = '@'
nstr_manip = str_manip.replace(letter1, new_char)
print(nstr_manip)

#Print last three characters in str_manip backwards using slice method
backward_slice = str_manip[-1:-4:-1]
print(backward_slice)

#Create 5 letter word using the first 3 characters and last 2 character of str_manip
front_slice = str_manip[:3]
back_slice = str_manip[-2:]
new_word = front_slice + back_slice
print(new_word)