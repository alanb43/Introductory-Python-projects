# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 08:15:12 2020

@author: bergsnei
"""

''' This function:
        Asks for an input name for a file, attempts to open file
        When successful: calculates multipliers, priority values, and creates
        various lists and tuples. Also calculates the number of house 
        representatives for each state and displays them under a header through
        different functions: all of which called through "main". '''

import math,csv

def open_file():
    ''' This file prompts a user for a filename to open until an acceptable 
    file is entered. If an unopenable file name is entered, an error message 
    appears '''
    
    x = 1
    while x == 1: #Guarantees continuous reprompt until acceptable file entered
        file_name = input("Enter filename: ")
        try:
            fp = open(file_name)
            return fp
            break # breaks out of loop because useful file found
        except FileNotFoundError:
            print("Error: File Not Found.") # error message
            continue # restarts loop to reprompt

def calc_multipliers():
    ''' Calculates 59 multipliers for the allocation of house seats through
    a known formula and adds them to a list '''
   
    multipliers = []
    for x in range(2,61): # given range from US Gov website
        multiplier = (1/math.sqrt(x*(x-1))) # given forumla
        multipliers.append(multiplier) # adds each multiplier to list
    return multipliers
    
def calc_priorities(state,population,multipliers):
    ''' Multiplies each multiplier by the inputted population, creates a tuple
    made up of the product and the associated state, then appends each tuple to
    a list which is then sorted in decreasing order by value. Returns list '''
    
    pop = int(population)
    priority_list = []
    for m in multipliers:
        priority = int(m * pop) # multiplies each multiplier w/ population
        tup = (priority, state) # creates a tuple w/ priority & assoc. state
        priority_list.append(tup) # adds each tuple to the priority list
    priority_list = sorted(priority_list, reverse = True) # sorts decreasing
    return priority_list

def read_file_make_priorities(fp,multipliers): 
    ''' reads the file, skips unnecessary elements, adds to two lists; one for
    lists of each state and their initial rep value (1) and the other for 
    tuples of priority values calculated in (calc_priorities) and their 
    associated states '''

    priority_list = []
    state_reps = []
    fp.readline() # skips first line
    reader = csv.reader(fp) # reads csv file
    for line_list in reader:
        state = line_list[1].replace('"','') # removes quotation marks from csv
        if state == "Puerto Rico" or state == "District of Columbia":
            continue # skips non-states in the files
        else:
            population = line_list[2] 
            state_reps.append([state, 1]) # list of state & initial reps (1)
            for item in calc_priorities(state,population,multipliers):
                # next line of code appends priority lists from calc_priorities 
                # to priority list within this function
                priority_list.append(item) 
    state_reps = sorted(state_reps) # sorts state_reps list
    priority_list = sorted(priority_list, reverse = True) # sorts decreasing
    return state_reps, priority_list[:385] 
    
def add_to_state(state,state_reps):
    ''' adds representatives to the rep count within state_reps list '''
    
    for item in state_reps: 
        match_state = item[0] # name of the state we're looking for
        state_count = item[1] # its representative value
        # if the state matches the state we're looking for, adds 1 to rep value
        if state == match_state: 
            item[1] += 1

def display(states):
    ''' prints header, then each state & its rep count, properly formatted '''
    
    print("{:15s}{:s}".format("State", "Representatives")) # header
    for item in states: # iterates for each state
        state = item[0]
        count = item[1]
        print("{:<15s}{:>4d}".format(state,count)) # properly formatted
          
def main():
    ''' calls functions & defines some variables to use in a function '''
    
    fp = open_file()
    multipliers = calc_multipliers()
    x = read_file_make_priorities(fp,multipliers)
    state_reps = x[0] # first item returned by read_file_make_priorities
    priority_list = x[1] # second item returned by read_file_make_priorities
    for tup in priority_list: # iterates through each tuple in priority list
        state = tup[1] # second item in tuple is state value
        if state: # uses each state as an input for the function in next line
            add_to_state(state,state_reps) 
    display(state_reps) 

if __name__ == "__main__":
    main()