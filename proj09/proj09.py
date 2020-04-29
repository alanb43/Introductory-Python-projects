# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 23:06:39 2020

@author: ab43p
"""

''' This program offers multiple selections to users regarding the nCoV info
available. The program opens a file containing nCoV data (user-inputted) and 
builds a dictionary using the information given. Dictionary is then used to 
assemble data for countries with highest # of areas affected, highest case #, 
# of affected areas, and whether or not a country is affected. This information
is printed, and users can choose to plot using this info. If selected, the plot 
function plots the data in a user-friendly manner.'''

import csv
import matplotlib.pyplot as plt
plt.style.use("ggplot")
from operator import itemgetter

def open_file():
    ''' This function prompts for a filename and opens the file assuming it 
    exists, now with a default file incase '''
    
    x = 0
    while x == 0: # guarantees continuous prompt
        try:
            filename = input("Data file: ")
            if filename == '':
                fp = open('ncov.csv') # default is ncov.csv if nothing entered
            else:
                fp = open(filename) # tries to open filename
            return(fp)
            break
        except FileNotFoundError:
            print("Error. Try again.") # error if filename not found
            continue

def build_dictionary(fp):
    ''' This function reads the file from open_file() and creates a dictionary
    storing all necessary information. '''
    
    fp.readline() # skips first
    reader = csv.reader(fp) 
    D1 = {} # initializes
    for line in reader:
        country = line[2].strip()
        area = line[1].strip()
        if area == '': # sets up empty areas for use in dictionary
            area = 'N/A'
        last_update = line[3].strip()
        cases = int(line[4].strip()) # int
        deaths = int(line[5].strip()) # int
        recovered = int(line[6].strip()) # int
        if country not in D1.keys(): #ensures a list exists for each country
            D1[country] = [] # initializes list that dictionaries are added to
        inside_dict2 = (last_update, cases, deaths, recovered) # tup for dict
        D1[country].append({area:inside_dict2}) # key : value dict inside list
    
    return D1

def top_affected_by_spread(D1):
    ''' This function sorts through the dictionary returned by build_dictionary
    and creates tuples of country and # of affected areas. This info is sorted
    and returned in a list. '''
    
    affected_list = []
    for key, lst in D1.items():
        count = 0
        for dct in lst: # for dictionary in list
            count += 1 # tracks number of affected areas by # of dictionaries
        tup = (key, count) # country, # of affected areas
        affected_list.append(tup)
    affected_list.sort() # sorts alphabetically
    affected_list.sort(key = itemgetter(1), reverse = True) # sorts by # desc.
    
    return affected_list[:10]
       
def top_affected_by_numbers(D1):
    ''' This function does the same as top_affected_by_spread except instead of
    number of affected areas the information is actually the top 10 countries
    with the highest # of cases. '''
    
    cases_list = []
    for key, lst in D1.items(): # country, list in D1
        cases = 0
        for dct in lst: # for dictionary in list
            for tup in dct.values():
                cases += tup[1] # of cases counter
        tup = (key, cases) # country, # of cases
        cases_list.append(tup)
    cases_list.sort() # sorts alphabetically
    cases_list.sort(key = itemgetter(1), reverse = True) #sorts # of cases desc
    
    return cases_list[:10]
    
def is_affected(D1, country):
    ''' This function receives an input of a country and returns whether or not
    the country is affected by nCoV. '''
    
    keys = D1.keys() # countries
    keys_list = []
    for key in keys: # for country in countries array
        key = key.lower() # makes lowercase for easier verification
        keys_list.append(key)
    if country.lower() in keys_list: # if user input == country in list
        return True
    else:
        return False

def plot_by_numbers(list_of_countries, list_of_numbers):
    '''
        This function plots the number of areas/people inffected by country.
        
        parameters: 
            list_of_countries: list of countries
            list_of_numbers: list of the number of areas/people inffected
            
        Returns: None
    '''
    fig, ax = plt.subplots()
    
    x_pos = [i for i, _ in enumerate(list_of_countries)]
    
    ax.barh(x_pos, list_of_numbers, align='center', color='red')
    ax.set_yticks(x_pos)
    ax.set_yticklabels(list_of_countries)
    ax.invert_yaxis()
    ax.set_xlabel('Count')
    ax.set_title('Novel Coronavirus statistics')
    
    plt.show()

def affected_states_in_country(D1, country):
    ''' This function accepts a user input of a country and returns a set of 
    affected areas in the country. '''
    
    keys = D1.keys() # all the countries in D1
    keys_list = []
    affected_set = set() # initializes empty set
    for key in keys: # country in array of countries
        key = key.lower() # makes it easier to verify countries
        keys_list.append(key) 
    if country.lower().strip() in keys_list: # if user country in list
        for key, value in D1.items(): 
            if key.lower() == country.lower(): # if country in D1 = user input
                for dct in value: # dictionary inside of list 
                    for key, value in dct.items(): 
                        area = key # area is key of inner dictionary
                        affected_set.add(area)
    
    return affected_set

def main():
    BANNER = '''
.__   __.   ______   ______   ____    ____
|  \ |  |  /      | /  __  \  \   \  /   /
|   \|  | |  ,----'|  |  |  |  \   \/   / 
|  . `  | |  |     |  |  |  |   \      /  
|  |\   | |  `----.|  `--'  |    \    /   
|__| \__|  \______| \______/      \__/  
    '''
    print(BANNER)
    MENU = ''' 
[1] Countries with most areas infected
[2] Countries with most people affected
[3] Affected areas in a country
[4] Check if a country is affected
[5] Exit

Choice: '''
    
    fp = open_file() # opens file
    D1 = build_dictionary(fp) # only main dictionary in use
    choice = input(MENU) # prints MENU while asking for input
    while choice != '5': # choice 5 closes program
        # Choice 1: Program compiles list of country with highest # of areas
        # affected, displays formatted info, & plots data if user chooses to 
        if choice == '1':
            areas_affected = top_affected_by_spread(D1) # gathers info
            country_list = []
            numbers_list = []
            print("{:<20s} {:15s}".format("Country", "Areas affected")) #header
            print("-"*40) # formatting
            for item in areas_affected:
                country = item[0]
                number = item[1]
                country_list.append(country) # grabs countries for plotting
                numbers_list.append(number) # grabs # of areas for plotting
                print("{:<20s} {:5d}".format(item[0],item[1]))
            plot = input('Plot? (y/n) ')
            if plot.lower() == 'y': # user chooses to plot
                plot_by_numbers(country_list, numbers_list)
            choice = input(MENU) # reprompt
        elif choice == '2':
            people_affected = top_affected_by_numbers(D1)
            country_list = []
            people_list = []
            print("{:<20s} {:15s}".format("Country", "People affected"))#header
            print("-"*40) # format
            for item in people_affected:
                if item[0].lower() != "mainland china": # skips mainland china*
                    country_list.append(item[0])
                    people_list.append(item[1])
                print("{:<20s} {:5d}".format(item[0],item[1]))
            plot = input('Plot? (y/n) ') # plot input
            if plot.lower() == 'y':
                plot_by_numbers(country_list[:5], people_list[:5]) # top 5*
            choice = input(MENU) # reprompt
        elif choice == '3':
            country = input("Country name: ").lower() # user input
            # sorted makes next line in alphabetical order
            affected_set = sorted(affected_states_in_country(D1, country))
            print("-"*30) # format
            if len(affected_set) > 0: # ensures country in set / set not empty
                print("{:<30s}".format("Affected area")) # header
                print("-"*30) # format
                for num, country in enumerate(affected_set):
                    num += 1 # enumerate starts off at 0
                    print("[{:02d}] {:<30s}".format(num, country))
            else:
                print("Error. Country not found.") # error msg
            choice = input(MENU) # reprompt 
        elif choice == '4':
            country = input("Country name: ").lower() # user input
            is_aff = is_affected(D1, country) # returns boolean
            print("-"*30) # format
            if is_aff == True: # country is affected
                print("{} is affected.".format(country))
            else: # country is not affected
                print("{} is not affected.".format(country))
            choice = input(MENU) # reprompt
        else:
            print("Error. Try again.") # error if input is not one of choices
            choice = input(MENU) # reprompt
    else:
        print("Stay at home. Protect your community against COVID-19")

if __name__ == "__main__":    
    main()
