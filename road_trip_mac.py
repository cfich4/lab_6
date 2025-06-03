#SDM: I want to create a series of functions so that when I run my program it will help to plan my roadtrip
#Where I have a car, I have some money, my car has a full tank of gas to start, the tank has a size (max amount gallons),
#the car has a fuel efficiency in miles per gallon, and I have a destination in mind that is some number of miles away from home
#there is a fixed price of gasoline in dollars per gallon
# Bonus points: I have some friends/family who I want to take with me and I'd like to split the travel costs equally

#what kinds of information do I want to know that are relevant to my roadtrip?
#1. How many gallons of gas do I need to get to my destination?
#2. How many times will I need to stop for gas? (This can lead to when and where I might get snacks, bathroom breaks, etc.)
#3. How many hours/minutes will my trip take? (This can lead to hotel considerations)
#4. How much will the trip cost me?
#5. Can I even make the trip given how much money and gas I (currently) have and how much more would I need to complete my trip?
#6. (Bonus) Given how much money I have, and how much the trip costs, I would need how many people paying equal amounts to be able to afford the trip

#import math. at this time it seems we do not need to import any external libraries yet...

#list our constants
MIN_PER_HOUR = 60

#list out our "nouns" (what stuff do we have in our program?)

money = float(input("Please enter how much money (in dollars) you have: $ "))
#this can be dollars w/ fractional cents (e.g. $100 and 25 cents)
tank_size = 10 
# $this would be in gallons
mpg = 30 
#fuel efficiency in miles per gallon
price_per_gal = 3.25
distance = float(input("How far away (in miles) is your destination?: "))
#distnace in miles to my destination
avg_travel_speed = 60 
#60 miles per hour

#on one tank of gas, how far can you go?
#for example: if I have a 10 gallon size tank, and a fuel effic of 30 miles per gallon would mean we could travel 300 miles on one tank
#full_tank_distance = tank_size * miles_per_gallon??? #distance I can go on a full tank in miles

def calc_full_tank_distance(tank_size, mpg):
    '''
    tank_size = size in gallons   
    mpg = miles per gallon    
    returns the distance in miles that one can travel in miles on a full tank
    '''
    return tank_size * mpg

full_tank_distance = calc_full_tank_distance(tank_size, mpg)
print(f"On a single tank of gas, I can travel {full_tank_distance} miles")

#this function has a docstring which describes what it does and how it works, and this enables convient tooltips wherever the function is called, and also allows in VS code to "jump" 
#to a function definition with control click
def calc_buyable_gallons(money_I_have, costs_per_gal):
     '''This function calculates the amount of gallons of gas one can purchase given the amount of money they have (in dollars) and the cost per gallon (also in dollars) '''
     return money_I_have / costs_per_gal

gal_I_can_buy = calc_full_tank_distance(money, price_per_gal)

print(f"With the {money:.2} I have and current cost of cost per gallon({price_per_gal:.2f} dollars per gallon), I can purchase {gal_I_can_buy:.2f}")

#1. How many gallons of gas do I need to get to my destination?
total_gallons = calc_full_tank_distance(mpg, distance)
'''This function calculates how many gallons of gas I will need in order to travel a given distance in miles given what my car's fuel efficiency is'''
     #this is a function stub 
     #this means that it does nothing
     #and it won't cause erorrs
     #'empty function'
#print out annswer to question one:
print(f"The number of gallons I need to get my destinaation if my destination is {distance} miles away and fuel economy is {mpg} mpg, is {total_gallons}")

#2. How many times will I need to stop for gas? / How many tanks will I need for gas
def calc_tanks_needed(total_gas_needed, tank_size):
     #??? quotient + 1 (may work) round up number actually, dont add one
     '''This function calculates how many tanks of gas I will need in order to travel given a total amount of gas needed (in gallons) and the size of my tank (in gallons)'''
     return total_gas_needed / tank_size
#print out answer to question two:
tanks_needed = calc_tanks_needed(total_gallons, tank_size)
#How many tanks of gas will I need?
print(f"The number of tanks I will need to make my trip if my tank max capacity is {tank_size} gallons and my trip distance is {distance} miles, it will be {tanks_needed} tanks."
      + "This means I would need to round {round(tanks_needed)} times for gas")
    #i don't know how to get change {round(tanks_needed)} to an actual number. same with {calc_trip_time} and others later in code
    #just giving this heads up before you run

#3. How many hours/minutes will my trip take? (This can lead to hotel considerations)
def calc_trip_time_minutes(distance, speed):
     #speed = distance / time
     #times*speed = distance
     #time = distance/speed
     return (distance / speed)*MIN_PER_HOUR

print(f"If the distance to travel is {distance} miles, and the travel speed is {avg_travel_speed} miles per hour, then the trip time will" 
      + "be {calc_trip_time_minutes(distance, avg_travel_speed)} minutes" + "/n" )

#4. How much will the trip cost me?
def cal_trip_cost(gas_needed, cost_per_gallon ):
     ''' 
     gas needed = total gallons
     cost_per_gallon = price_per_gal
     '''
     return gas_needed* cost_per_gallon

#5. Can I even make the trip given how much money and gas I (currently) have and how much more would I need to complete my trip?
def calc_gas_I_can_afford(money_I_have, cost_per_gal):
     ''' 
     money_I _have = money   
     cost_per_gal = price_per_gal   
     '''
     return money_I_have / cost_per_gal #returs gallons

def can_make_trip(total_gas_needed, gas_I_start_with, gas_I_can_afford):
    '''
    Returns:
    - True and 0 if you have enough gas to make the trip.
    - False and the extra money needed if you don't.
    '''
    total_gas_available = gas_I_start_with + gas_I_can_afford

    if total_gas_available >= total_gas_needed:
        return True, 0  

    extra_gas_needed = total_gas_needed - total_gas_available
    extra_money_needed = extra_gas_needed * price_per_gal
    return False, round(extra_money_needed, 2)


     
#will use answer from 4. as an arguement
def money_I_will_still_need(money_I_have, total_trip_cost):
     ''' 
     money_I_have = money  
     total_trip_cost =  
     '''
     return max(0, total_trip_cost - money_I_have)
