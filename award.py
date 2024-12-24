#Request input from user showing times, in minutes, used in completing 3 games in a triathalon
#Save times under variable names new_swim, new_cyc, new_run
#Cast the numbers from string format to float, to allow for integers and decimals

new_swim = input("My best swimming time in minutes: ")
new_swim1 = float(new_swim)
new_cyc = input("My best cycling time in minutes is: ")
new_cyc1 = float(new_cyc)
new_run = input("My best running time in minutes is: ")
new_run1 = float(new_run)

#Calculate and print total taken to complete the triathalon
#Save under variable name total_time

time = new_swim1 + new_cyc1 + new_run1
print(f"When you add all your time together, you get: {time}")

#Determine award based on total time


if time >= 111:
    print("You recieve no award")
elif time >= 106:
    print("You receive the Honorary scroll")
elif time >= 101:
    print("You receive the Honorary half colors")
else:
    print("You receive the Honorary colors")



if time <= 100:
    print("You receive the Honorary colors")
elif time <= 105:
    print("You receive the Honorary half colors")
elif time <= 110:
    print("You receive the Honorary scroll")
else:
    print("You receive no award")






