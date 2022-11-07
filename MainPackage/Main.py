"""
Name: Amanda Rapien and Grace Hertzfeld 
email: rapienaa@mail.uc.edu and hertzfgc@mail.uc.edu
Assignment: Assignment 11
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This project demonstrates that we can understand various data, dictionaries, and APIs.
Citations:
Anything else that's relevant: 
"""
#Main.py

import json  #Built in, no need to install
import requests #Add with pop

#This is our personal API Key     
response = requests.get('https://api.weatherbit.io/v2.0/current?city=Cincinati&country=United%20States&key=839131a2085f49389bff0cee0a8460fb')
json_string = response.content
    
parsed_json = json.loads(json_string) # Now we have a python dictionary
    

    
for City in parsed_json['data']:         #Get the value associated with paresed_json['data']
#   print (City)  #this has a list of aspects of the weather
    print("City Name :", City["city_name"])
    print("Country Name :", City["country_code"])
    print("Date and Time :", City["datetime"])
    print("Sunrise Time :", City["sunrise"])
    #Will need to print out each aspect indivually 