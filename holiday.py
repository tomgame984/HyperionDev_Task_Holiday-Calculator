# *** PROGRAM STRUCTURE ***
# City Flight:
    # List with cities.
    # List with flight prices per city.
    # User input (Please select which city you would like to fly to?)
    # Display city names and flight prices for each.

# Num Nights:
    # User input (How many nights would like to stay for?)

# Rental Days:
    # How many days would you like to hire a car for?

# FUNCTIONS
# hotel_cost
    # number of nights x hotel option
    # return total cost

# plane_cost
    # lookup city and return flight price

# car_rental 
    # rental days x day rental cost

# holiday cost:
    # hotel_cost + plane_cost + car_rental

# ************  START OF PROGRAM  ************

# FUNCTIONS:
# ITEMS CHARGED ON PER DAY/NIGHT BASIS
# hotel_cost and car_rental cost functions require the same calculation. So I 
# only created this per_day_rate function.
def per_day_rate(num1, num2):
    """Calculates the total cost of items where there is a per day rate and
    a varying number of days.

    Args:
        num1 (int): user defined number of days/nights.
        num2 (int): daily charge for the associated item.

    Returns:
        int: total costs = num of days * daily charge.
    """
    rate_tot = num1 * num2
    return rate_tot

# FLIGHT COST
def plane_cost(x, y, z):
    """Returns the total cost of a flight based on user defined inputs.

    Args:
        x (list): A list of cities.
        y (str): User input - selection made from 'city' list.
        z (dict): Dictionary with key (cities) value (flight price)
    """
    for item in x:
        if item == y:
            return(z[item])
        
# HOLIDAY COST
def holiday_cost(x, y, z):
    """Provides a grand total for the holiday.

    Args:
        x (int): returned value from flight_cost func.
        y (int): returned value from per_day_rate func. Called for hotel cost.
        z (int): returned value from per_dat_rate func. called for car rental cost.

    Returns:
        int: the sum of x, y, z values.
    """
    total_cost = int(x + y + z)
    return total_cost

# CITY LIST
city = ['Bangkok', 'Barcelona', 'Johannesburg', 'New York', 'Rome',
        'Rio De Janeiro', 'Sydney', 'Tokyo']

# FLIGHT PRICE DICTIONARY
flight_prices = {'Bangkok': 1015, 
                 'Barcelona': 254,
                 'Johannesburg': 848, 
                 'New York': 652, 
                 'Rome': 184, 
                 'Rio De Janeiro': 1268, 
                 'Sydney': 1744, 
                 'Tokyo': 1880}

car_rent_rate = 125 # standard per day car rental charge
hotel_rate = 235 # Per night rate for hotel

# USER INPUT
print("\n *** CITY BREAK SALE NOW ON *** \n")
print("We have some great offers on holidays to amazing cities worldwide!\n")
print("The best offers are currently available on the following locations:")

for item in city:
    print(item)
    
print(" ")

city_flight = input("Which city would you be interested in visting?  ")

while city_flight not in city:
    print("Unfortunately, we don't have any offers for this location for now.")
    city_flight = input("Please make a selection from the cities listed:  ")

print(f"\n{city_flight} is a great choice!\n")
num_nights = int(input("How many nights would you like to go for?  "))
rental_days = int(input(f"\nHow many days would you like to have a rental car for?  "))

# OUTPUTS BASED ON USER INPUTS
flight_cost = (plane_cost(city, city_flight, flight_prices))
hotel_tot = (per_day_rate(num_nights, hotel_rate))
car_rent_tot = (per_day_rate(rental_days, car_rent_rate))
holiday_tot = (holiday_cost(flight_cost, hotel_tot, car_rent_tot))

print(f"\nBased on your criteria, please find below the price breakdown:\n")

print("FLIGHT DETAILS")
print(f"Return Flights to {city_flight}:  £{flight_cost}\n")

print("HOTEL ACCOMODATION:")
print(f"Duration: {num_nights} nights (B&B rate)")
print(f"Accommodation Cost:  £{hotel_tot}\n")

print("CAR RENTAL:")
print(f"Duration: {rental_days} days.")
print(f"Rental Cost:  £{car_rent_tot}\n")

print(f"TOTAL PACKAGE PRICE:  £{holiday_tot}")

# ************  END OF PROGRAM  ************