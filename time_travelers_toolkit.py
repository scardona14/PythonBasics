import datetime as dt
from decimal import Decimal
from random import randint, choice
import custom_module

# Retrieve the current date and time
current_datetime = dt.datetime.now()
current_date = current_datetime.date()  # Get current date (e.g., 2025-01-10)
current_time = current_datetime.time()  # Get current time (e.g., 14:30:45)

# Print the current date and time
print(f"Current Date: {current_date}")
print(f"Current Time: {current_time}")

# Base cost of time travel
base_cost = Decimal('1000.00')

# List of possible time travel destinations
destinations = [
    "Mars",
    "Ancient Egypt",
    "The year 3025",
    "The Jurassic period",
    "The future",
    "Medieval Europe",
    "The moon",
    "Atlantis",
    "Victorian London",
    "The Lost City of El Dorado"
]

# Function to calculate the cost of time travel
def calculate_time_travel_cost(target_year):
    current_year = current_datetime.year  # Get the current year
    
    # Calculate the difference between the current year and target year
    year_difference = abs(target_year - current_year)
    
    # Determine the cost multiplier (5% increase per year difference)
    cost_multiplier = Decimal('1.05') ** year_difference
    
    # Calculate the final cost
    final_cost = base_cost * cost_multiplier
    
    # Return the final cost, rounded to two decimal places
    return final_cost.quantize(Decimal('0.01'))

# Generate a random year between 2025 and 3025 for the time travel
target_year = randint(2025, 3025)

# Select a random destination from the list
random_destination = choice(destinations)

# Calculate the travel cost
calculated_cost = calculate_time_travel_cost(target_year)

# Ensure the final cost is formatted to two decimal places and print the time travel message
message = custom_module.generate_time_travel_message(target_year, random_destination, calculated_cost)
print(message)