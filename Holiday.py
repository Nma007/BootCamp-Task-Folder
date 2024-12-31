# Request a user to input city they want to travel to
#Give the user an option of cities to visit and their flight costs in a dictionary

#set up a dictionary with cities and flight costs
cities_cost = {"London": 100, #The dicyionary stores the city names as the keys and their fight prices are the values
           "Belaruse": 250,
          "Paris": 200,
          "Dubai": 90,
          "Sydney": 100,
          "Accra": 200,}
#Display available cities and their flight costs

print("Choose your city of travel: ")
for city, cost in cities_cost.items(): #the loop retrieves the city name, its cost and displays them
        print(f"{city} - £{cost}") # Formats and prints each city along with its cost

# Get the user to input city of travel and store under varible name city_flight
# Use while loop to make sure valid input is gotten
while True:
    city_flight = input("Enter destination city: ") # Get user input
# Use if statment to check user's choice is valid
#If valid print name and price from dictionary
#Break statement and exit loop
#If invalid print error message and continue
    if city_flight in cities_cost:
        flight_cost = cities_cost[city_flight]
        print(f"\nYou have chosen to travel to {city_flight}. The flight cost is £{flight_cost}.")
        break
    else:
        print("\nInvalid choice. Please enter valid destination: ")


#Get number of nights the usser will stay in a hotel
num_nights = int(input("Enter number of nights in hotel: "))

#Get number of days for car rental
rental_days = int(input("Enter number of days for car rental: "))

#Define a function that will take num_nights as an argument and multiply it with price of hotel per night 
#return a total cost for the hotel stay (you can choose the price per night charged at the hotel).
#Print the product

def hotel_cost(num_nights):
     hotel_price = 150
     product = num_nights * hotel_price
     return product
     print(f"{num_nights} * {hotel_price} is £{product} ")

num_nights = int(input("Enter the number of nights you want to stay at the hotel: "))
if num_nights < 0:
        print("The number of nights cannot be negative. Please enter a valid number.")
else:
        # Step 2: Calculate the hotel cost
        cost = hotel_cost(num_nights)
        print(f"The total cost for your hotel stay of {num_nights} night(s) is ${cost}.")

#Define a function that will city_flight as an argument
# return and print cost of flight


def validate_cities(city_flight):
     validate_cities =["London", "Belaruse", "Paris", "Dubai", "Sydney", "Accra"]
     return city_flight in validate_cities

def plane_cost(city_flight):
     
     if city_flight == "London": 
        return 100
     elif city_flight =="Belaruse":
      return 250
     elif city_flight =="Paris":
        return 200
     elif city_flight == "Dubai":
        return 90
     elif city_flight == "Sydney":
        return 100
     elif city_flight == "Accra": 
         return 200

#  program to interact with the user
print("Choose a city you want to travel to:")
cities = ["Belaruse", "London", "Dubai", "Paris", "Sydney", "Accra"]
for city in cities:
    print(city)

while True:  # Infinite loop to ensure valid input
    city_flight = input("\nEnter the name of the city you want to travel to: ").strip()
    
    # Validate the user's input
    if validate_cities(city_flight):  # Call the validate_cities function
        cost = plane_cost("city_flight")  # Get the flight cost
        print(f"\nYou have chosen to travel to {city_flight}. The flight cost is £{cost}.")
        break  # Exit the loop if input is valid
    else:
        print("\nInvalid city name. Please enter a valid city from the list.")

    

#This function will take rental_days as an argument and
#return the total cost of the car rental (you can choose the daily rental cost).

def car_rental(rental_days, rental_price = 60):
    product = rental_days * rental_price
    return product
    print(f"{rental_days} * {rental_price} is £{product}")

#holiday_cost(): This function takes three arguments: num_nights,
#city_flight, and rental_days. Using these three arguments, call the
#hotel_cost(), plane_cost(), and car_rental() functions with their
#respective arguments, and finally return the total cost for the holiday.

def holiday_cost(num_nights, city_flight, rental_days):

     hotel_total = hotel_cost(num_nights)  # Call hotel_cost with num_nights
     flight_total = plane_cost(city_flight)  # Call plane_cost with city_flight
     rental_total = car_rental(rental_days)  # Call car_rental with rental_days
    
     total_holiday_cost = hotel_total + flight_total + rental_total  # Sum up all costs
     return total_holiday_cost
   





     
     

