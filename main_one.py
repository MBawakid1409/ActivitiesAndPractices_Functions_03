# Activities & Practices
# --------- [Functions] ---------
print("--------- [Functions] ---------")
print("----------------------------------")
# Practise 01
print("Practise #01")
def trip_welcome(origin, destination):
    print("Welcome to Tripcademy")
    print("Looks like you are traveling from " + origin)
    print("And you are heading to " + destination)

trip_welcome("Medina", "Makkah")    
print("----------------------------------")
# Practise 02
print("Practise #02")
# Types of Arguments
# Positional arguments: called by their position in the function definition.
def calculate_taxi_price(miles_to_travel, rate, discount):
    print(miles_to_travel * rate - discount)
    
calculate_taxi_price(100, 10, 5)
print("----------------------------------")
# Practise 03
print("Practise #03")
# Keyword arguments: called by their name.
def calculate_taxi_price2(miles_to_travel, rate, discount):
    print(miles_to_travel * rate - discount)

calculate_taxi_price2(rate=0.5, discount=10, miles_to_travel=100) # 40.0
print("----------------------------------")
# Practise 04
print("Practise #04")    
# Default arguments: arguments that are given default values.
def calculate_taxi_price3(miles_to_travel, rate, discount = 10):
    print(miles_to_travel * rate - discount)

# Using the default value of 10 for discount.
calculate_taxi_price3(10, 0.5) # -5.0
# or
# Overwriting the default value of 10 with 20    
calculate_taxi_price3(10, 0.5, 20) # -15.0
print("----------------------------------")
# Practise 05
print("Practise #05")
# Built-in Functions
# len()
destination_name = "studyHarderNotSmarter"
length_of_destination = len(destination_name)
print(length_of_destination)  # 21
# help()
# help("string") # print a link to documentation and provide some details:
tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00
# max()
max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price) # 15.5
# min()
min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price) # 2.0
# round()
rounded_price = round(tshirt_price, 1)
print(rounded_price) # 9.8
print("----------------------------------")
# Practise 06
print("Practise #06")
# Variable Access
favorite_locations = "Paris, Norway, Iceland"
def print_count_locations():
    print("There are 3 locations")

def show_favorite_locations():
    print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()        
print("----------------------------------")
# Practise 07
print("Practise #07")
def calculate_exchange_usd(us_dollars, exchange_rate):
    return us_dollars * exchange_rate

new_zealand_exchange = calculate_exchange_usd(100, 1.4)

print("100 dollars in US currency would give you " + str(new_zealand_exchange) + " New Zealand dollars")
# 100 dollars in US currency would give you 140.0 New Zealand dollars
print("----------------------------------")
# Practise 07
print("Practise #07")
current_budget = 3500.75

def print_remaining_budget(budget):
    print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)
# Your remaining budget is: $3500.75

def deduct_expense(budget, expense):
    return budget - expense

shirt_expense = 9
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt)
# Your remaining budget is: $3491.75
print("----------------------------------")
# Practise 08
print("Practise #08")
def top_tourist_locations_italy():
    first = "Medina"
    second = "Makkah"
    third = "Jeddah"
    return first, second, third

most_popular1, most_popular2, most_popular3 = top_tourist_locations_italy()

print(most_popular1) # Medina
print(most_popular2) # Makkah
print(most_popular3) # Jeddah
print("----------------------------------")
# Practise 09
print("Practise #09")
weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']

def threeday_weather_report(weather):
    first_day = " Tomorrow the weather will be " + weather[0]
    second_day = " The following day it will be " + weather[1]
    third_day = " Two days from now it will be " + weather[2]
    return first_day, second_day, third_day

monday, tuesday, wednesday = threeday_weather_report(weather_data)

print(monday) # Tomorrow the weather will be Sunny
print(tuesday) # The following day it will be Sunny
print(wednesday) # Two days from now it will be Cloudy
print("----------------------------------")
# Practise 10
print("Practise #10")
def trip_planner_welcome(name):
    print("Welcome to tripplanner v1.0 " + name)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
    print("Your trip starts off in " + origin)
    print("And you are traveling to " + destination)
    print("You will be traveling by " + mode_of_transport)
    print("It will take approximately " + str(estimated_time) + " hours")

def estimated_time_rounded(estimated_time):
    rounded_time = round(estimated_time)
    return rounded_time

trip_planner_welcome("Mohammad")
estimate = estimated_time_rounded(2.43)
destination_setup("Jeddah", "Medina", estimate)     

# Output:
# Welcome to tripplanner v1.0 Khaled Yaseen
# Your trip starts off in Jeddah
# And you are traveling to Medina
# You will be traveling by Car
# It will take approximately 2 hours

print("----------------------------------")
# Practise 11
print("-----[Getting Ready for Physics Class]-----")
# You are a physics teacher preparing for the upcoming semester. You want to provide your students with some functions that will help them calculate some fundamental physical properties.
print("----------------------------------")
# Data for this exercise
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1 

print("-----[Turn up the Temperature]-----")
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

# fahrenheit 100
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)

def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp

# Celsius 0
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)
print("----------------------------------")
print("-----[Use the Force]-----")
# Define a function called [get_force] that takes in [mass] and [acceleration]. It should return [mass] multiplied by [acceleration].
def get_force(mass, acceleration):
    result = mass * acceleration
    return result

# Test [get_force] by calling it with the variables [train_mass] and [train_acceleration]. Save the result to a variable called [train_force] and print it out.
train_force = get_force(train_mass, train_acceleration)
print("The GE train supplies {} Newtons of force.".format(train_force))

# Define a function called [get_energy] that takes in [mass] and [c].
# [c] is a constant that is usually set to the speed of light, which is roughly 3 x 10^8. Set [c] to have a default value of [3*10**8].
# [get_energy] should return [mass] multiplied by [c] squared.
def get_energy(mass):
    c = 3*10**8
    return mass * c**2

# Test [get_energy] by using it on [bomb_mass], with the default value of [c]. Save the result to a variable called [bomb_energy].
bomb_energy = get_energy(bomb_mass)
print("A 1kg bomb supplies {} Joules.".format(bomb_energy))
print("----------------------------------")
print("-----[Do the Work]-----")
# Define a final function called [get_work] that takes in [mass], [acceleration], and [distance].
# Work is defined as force multiplied by distance. First, get the [force] using [get_force], then multiply that by [distance]. Return the result.
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration) * distance
    return force

# Test [get_work] by using it on [train_mass], [train_acceleration], and [train_distance]. Save the result to a variable called [train_work].
train_work = get_work(train_mass, train_acceleration, train_distance)
print("The GE train does {} Joules of work over {} meters.".format(train_work, train_distance))
print("----------------------------------")
# Practise 12
print("Practise #12")
balance = 12.55
name = "Mohammad"

def withdraw_money(amount):
    result = balance - amount
    print("Hello " + name + " your balance remaining is: $" + str(result))
    return amount

withdraw_money(2)
print("Save your money " + name + "!")
print("----------------------------------")
# Practise 13
print("Practise #13")    
balance = 1000

def print_balance():
    print("Your balance is " + str(balance)) # Your balance is 1000

def deduct(amount):
    print("Your new balance is " + str(balance - amount)) 
    # Your new balance is 500

savings = 500

def calculate_interest_on_savings():
    print("You will gain interest on: " + str(savings))
    # You will gain interest on: 500

    def calculate_taxes():
        tax_amount = savings * 0.13
        print("You will be taxed: " + str(tax_amount))
    calculate_taxes() 
    # You will gain interest on: 500   


print_balance()
deduct(500)
calculate_interest_on_savings()
print("----------------------------------")
# Practise 14
print("Practise #14") 
print("-----[Tenth Power]-----")
# Write a function named [tenth_power()] that has one parameter named [num].
# The function should return [num] raised to the 10th power.
def tenth_power(num):
    return num ** 10

print(tenth_power(1)) # 1

print(tenth_power(0)) # 0

print(tenth_power(2)) # 1024
print("----------------------------------")
# Practise 15
print("Practise #15") 
print("-----[Square Root]-----")
# Write a function named [square_root()] that has one parameter named [num].
# Use exponents (**) to return the square root of [num].
def square_root(num):
    return num ** 0.5


print(square_root(16)) # 4    
print(square_root(100)) # 10
print("----------------------------------")
# Practise 16
print("Practise #16") 
print("-----[Win Percentage]-----")
# Create a function called win_percentage() that takes two parameters named wins and losses.
# This function should return out the total percentage of games won by a team based on these two numbers.
def win_percentage(wins, losses):
    total_percentage = str(round(wins/(wins+losses)*100)) + str("%")
    return total_percentage 

    # or
    # total_games = wins + losses
    # ratio_won = wins / total_games
    # return ratio_won * 100
    
print(win_percentage(5, 5)) # كانت كذا 50.0% وصارت كذا 50% بعد الروند ميثود
print(win_percentage(10, 0)) # هنا نفس الشيء صارت 100% من دون ديسمال بوينت
print("----------------------------------")
# Practise 17
print("Practise #17") 
print("-----[Average]-----")
# Write a function named average() that has two parameters named num1 and num2.
# The function should return the average of these two numbers.
def average(num1, num2):
    average_result = (num1 + num2) / 2
    return int(average_result)
    # or just return (num1 + num2) / 2

print(average(4, 2))    
print("----------------------------------")
# Practise 18
print("Practise #18") 
print("-----[Remainder]-----")
# Write a function named remainder() that has two parameters named num1 and num2
# The function should return the remainder of twice num1 divided by half of num2
def remainder(num1, num2):
    result = (num1*2) % (num2/2)
    return result

print(remainder(15, 14)) # 2.0
print(remainder(9, 6))   # 0.0
print("----------------------------------")
# Practise 19
print("Practise #19") 
print("-----[First Three Multiples]-----")
# Write a function named [first_three_multiples()] that has one parameter named [num].
# This function should print the first three multiples of num. Then, it should return the third multiple.
# For example, first_three_multiples(7) should print 7, 14, and 21 on three different lines, and return 21.
def first_three_multiples(num):
    print(num) # 7
    print(num*2) # 14
    print(num*3) # 21
    return num * 3 # 21

print(first_three_multiples(7))    
print("----------------------------------")
# Practise 20
print("Practise #20") 
print("-----[Tip]-----")
# Create a function called tip() that has two parameters named total and percentage.
# This function should return the amount you should tip given a total and the percentage you want to tip.
def tip(total, percentage):
    tip_amount = (total*percentage) / 100
    return tip_amount

print(tip(10, 25)) # 2.5
print(tip(0, 100)) # 0.0
print("----------------------------------")
# Practise 21
print("Practise #21") 
print("-----[Bond, James Bond]-----")
# Write a function named introduction() that has two parameters named first_name and last_name.
# The function should return the last_name, followed by a comma, a space, first_name another space, and finally last_name.
def introduction(first_name, last_name):
    return ("{}, {} {}".format(last_name, first_name, last_name))

print(introduction("James", "Bond"))
print("----------------------------------")
# Practise 22
print("Practise #22") 
print("-----[Dog Years]-----")
# Some say that every one year of a human's life is equivalent to seven years of a dog's life. Write a function named dog_years() that has two parameters named name and age.
# The function should compute the age in dog years and return the following string: "{name}, you are {age} years old in dog years"
# Test this function with your name and your age!
def dog_years(name, age):
    age *= 7
    return ("{}, you are {} years old in dog years".format(name,age))

print(dog_years("Gomba",16)) # Gomba, you are 112 years old in dog years
print(dog_years("Frogy",2)) # Frogy, you are 14 years old in dog years
print("----------------------------------")
# Practise 23
print("Practise #23") 
print("-----[All Operations]-----")
# Create a function named lots_of_math(). This function should have four parameters named a, b, c, and d. The function should print 3 lines and return 1 value.
# First, print the sum of a and b.
# Second, print c minus d.
# Third, print the first number printed, multiplied by the second number printed.
# Finally, return the third number printed modulo a.
def lots_of_math(a, b, c, d):
    first_num = a + b
    print(first_num)
    second_num = c - d
    print(second_num)
    third_num = first_num * second_num
    print(third_num)
    return third_num % a

print(lots_of_math(7, 9, 68, 41)) # 1st:16  2nd:27  3rd:432  4th:5 