# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 22:35:09 2020

@author: ab43p
"""

''' This program has the user open a file (with video game information), reads
the information, sorts it into different dictionaries sorted by different
categorical search queries, and then uses the information to assemble various
different lists and arrays of information, which it then sorts through and 
presents for the user. This program allows for user-specific input and graphs
piecharts and bar-graphs. '''

import csv
import pylab
from operator import itemgetter


def open_file():
    ''' Prompts a user for a filename to open until an acceptable 
    file is entered. Error message displayed until acceptable file received '''
    
    x = 1
    while x == 1: #Guarantees continuous reprompt until acceptable file entered
        filename = input("Enter filename: ")
        try: 
            fp = open(filename, encoding = 'utf-8')
            return fp
            break # breaks out of loop because useful file found
        except FileNotFoundError:
            print("File not found! Please try again!") # error message
            continue # restarts loop to reprompt

def read_file(fp):
    ''' This function reads a csv file and finds data in each line of the file,
    including but not limited to: video game name, platform, genre, etc. It 
    also calculates global sales for each game. With this information, 3 
    dictionaries are created, with different keys and values using the data 
    found in the csv file. '''
    
    D1_orig = {}
    D2_orig = {}
    D3_orig = {}
    
    fp.readline() # skips file header row
    reader = csv.reader(fp) # reads file
    global_sales = 0
    for line in reader:
        # .strip().lower() guarantees no whitespace or uppercase lettering
        # makes information more easy to sort
        name = line[0].strip().lower() 
        plat = line[1].strip().lower() 
        if not line[2].isdigit(): # checks that a year is in the year column
            continue              # skips game without year
        year = int(line[2].strip().lower()) 
        genre = line[3].strip().lower()
        pub = line[4].strip().lower()
        # following lines place sales figures in their actual amounts
        na_sales = float(line[5].strip().lower()) * 1000000 
        eur_sales = float(line[6].strip().lower()) * 1000000
        japan_sales = float(line[7].strip().lower()) * 1000000
        other_sales = float(line[8].strip().lower()) * 1000000
        # total sales for each game (each iteration) and rounds it
        global_sales_gme = round((na_sales + japan_sales + eur_sales + \
                         other_sales), 1)
        # adds sales for all games total for each iteration, giving total sales
        global_sales += round((na_sales + japan_sales + eur_sales + \
                         other_sales), 1)
            
        #################creates dictionary sorted by name#####################   
        if name in D1_orig.keys():
            D1_orig[name].append((name, plat, year, genre, pub,\
                             global_sales_gme))
        else:
            D1_orig[name] = [(name, plat, year, genre, pub, global_sales_gme)]
        #######################################################################
        ##############creates second dictionary sorted by genre################
        if genre in D2_orig.keys():
            D2_orig[genre].append((genre, year, na_sales, eur_sales, \
                                  japan_sales, other_sales, global_sales_gme))
        else:
            D2_orig[genre] = [(genre, year, na_sales, eur_sales, japan_sales, \
                               other_sales, global_sales_gme)]
        #######################################################################        
        #############creates third dictionary sorted by publisher##############
        if pub in D3_orig.keys():
            D3_orig[pub].append((pub, name, year, na_sales, eur_sales, \
                                 japan_sales, other_sales, global_sales_gme))
        else:
            D3_orig[pub] = [(pub, name, year, na_sales, eur_sales, \
                          japan_sales, other_sales, global_sales_gme)]
        #######################################################################
    # new dictionaries
    D1 = {} 
    D2 = {}
    D3 = {}
    # data we want in dictionaries, but now sorted by global sales (in reverse)
    for key in sorted(D1_orig):
        D1[key] = sorted(D1_orig[key], key = itemgetter(-1), reverse = True)
    for key in sorted(D2_orig):
        D2[key] = sorted(D2_orig[key], key = itemgetter(-1), reverse = True)
    for key in sorted(D3_orig):
        D3[key] = sorted(D3_orig[key], key = itemgetter(-1), reverse = True)
    
    return D1, D2, D3
    
def get_data_by_column(D1, indicator, c_value):
    ''' This function takes in a dictionary, indicator, and value and seeks to 
    find the value in the dictionary's values based on the indicator. If found, 
    a new list appends the dictionary's values and is returned '''
    
    L1 = [] # initializes empty list
    # tries to integerize the c_value to ensure year or platform
    try: 
        c_value = int(c_value)
    except ValueError:
        c_value = c_value.strip()
    values = D1.values() # values are all of the keys' different values
    for item in values: # for each list in values
        for tup in item: # for each tuple in said list
            year = int(tup[2]) 
            platform = tup[1]
            if c_value == year or str(c_value) == platform:
                L1.append(tup)
    L1.sort(key = itemgetter(5), reverse = True) # sorts by global sales, desc.
    if indicator == 'year':
        L1.sort(key = itemgetter(1)) # sorts by platform alphabetically
    elif indicator == 'platform':
        L1.sort(key = itemgetter(2)) # sorts by year in ascending order
    else:
        L1 = [] # returns empty list for indicator that is n't recognized
    
    return L1

def get_publisher_data(D3, publisher):
    ''' This function searches the values of dictionary 3 for the publisher.
    If the publisher in the dictionary values matches the publisher in the 
    function's input, the tuple from the dictionary is added to a list. Then 
    sorted by name ascending and global sales descending. '''
    
    publisher_list = []
    values = D3.values() # values are all of the keys' different values
    for items in values: # for each list in values
        for tup in items: # for each tuple in said list
            pub = tup[0] # publisher
            if pub == publisher: # if tuple publisher = inputted publisher
                publisher_list.append(tup)
    publisher_list.sort(key = itemgetter(1)) # sorts by name alphabetically
    # sorts by global sales in descending order
    publisher_list.sort(key = itemgetter(7), reverse = True) 
    
    return publisher_list
    
def display_global_sales_data(L1, indicator):
    ''' This function displays global sales data based on either a year or 
    platform the user inputs for tons of games. The sorting differs based on 
    which indicator the user chooses, though both show individual game sales 
    and the sales total for all the games on the list. '''
    
    header1 = ['Name', 'Platform', 'Genre', 'Publisher', 'Global Sales']
    header2 = ['Name', 'Year', 'Genre', 'Publisher', 'Global Sales']
    global_sales_total = 0
    
    if indicator == 'year':
        # this for loop is needed to properly display the first heading line
        for tup in L1: 
            year = tup[2]
        # next 2 lines format a header based on year & a header row for columns
        print("\n{:^80}".format("Video Game Sales in {}".format(year)))
        print("{:<30s}{:<10s}{:<20s}{:<30s}{:<12s}".format(*header1)) 
        # this for loop had to come after the headers
        for tup in L1:
            year = tup[2]
            name = tup[0]
            plat = tup[1] # platform
            genre = tup[3]
            pub = tup[4] # publisher
            glob_sales = tup[5] # individual global sales for a game
            global_sales_total += int(glob_sales) # composite sales total
            
            # prints information for year indicator, formatted like header
            if year: 
                print("{:30s}{:10s}{:20s}{:30s}{:<12,.02f}".format\
                      (name[:25], plat, genre[:15], pub[:25], glob_sales))
                    
    elif indicator == 'platform':
        # this for loop is needed to properly display the first heading line
        for tup in L1:
            plat = tup[1]
        # next 2 lines format a header based on year & a header row for columns
        print("\n{:^80s}".format("Video Game Sales for {}".format(plat)))
        print("{:<30s}{:<10s}{:<20s}{:<30s}{:<12s}".format(*header2))
        # this for loop had to come after the headers
        for tup in L1:
            year = tup[2]
            name = tup[0]
            plat = tup[1] # platform
            genre = tup[3]
            pub = tup[4] # publisher
            glob_sales = tup[5] # individual global sales for a game
            global_sales_total += int(glob_sales) # composite sales total
            
            # prints information for platform indicator, formatted like header
            if plat: 
                print("{:30s}{:<10d}{:20s}{:30s}{:<12,.02f}".format\
                      (name[:25], year, genre[:15], pub[:25], glob_sales))
    
    # prints total sales of all items in the displayed list, at the end
    print("\n{:90s}{:<12,.02f}".format("Total Sales", global_sales_total))
    
def get_genre_data(D2, year):
    ''' This function sorts through the second dictionary's list to create a 
    list of genres with their regional sales and occurences in a year. '''
    
    genres_list = []
    values = D2.values()
    for value in values:
        count = 0 # number of occurrences of the genre or year
        na_total = 0 # total na sales
        eur_total = 0 # total europe sales
        jpn_total = 0 # total japan sales
        oth_total = 0 # total other sales
        glob_total = 0 # total global sales (adds up all other totals)
        genre = '' # initial genre for the initial tuple below
        genre_tup = (genre, count, na_total, eur_total, jpn_total, oth_total, \
                     glob_total)
        
        for tup in value:
            if year == tup[1]: # checks if inputted year = year of items in D2
                count += 1 # adds to the count of occurrence
                na_total += tup[2] # adds tuple's na sales to the genre's total
                eur_total += tup[3] # adds tup's eur sales to the genre's total
                jpn_total += tup[4] # adds tup's jpn sales to the genre's total
                oth_total += tup[5] # adds tup's other sales to genre's total
                glob_total += tup[6] # adds tup's total to the genre's total
                genre = tup[0] # genre in tup
                genre_tup = (genre, count, na_total, eur_total, jpn_total, \
                             oth_total, glob_total) # tup with previous values
        if count > 0: # appends the tup to the list if the count is more than 0
            genres_list.append(genre_tup) 
    
    genres_list.sort(key = itemgetter(0)) # sorts by genre name
    # sorts by global sales, descending
    genres_list.sort(key = itemgetter(-1), reverse = True) 
                    
    return genres_list
    
def display_genre_data(genre_list):
    ''' This function displays sales data for each genre in the csv file. '''
    
    header = ['Genre', 'North America', 'Europe', 'Japan', 'Other', 'Global']
    
    print("\nRegional Video Games Sales per Genre") # first header
    print("{:15s}{:15s}{:15s}{:15s}{:15s}{:15s}".format(*header)) # header row
    complete_total = 0
    for tup in genre_list:
        genre = tup[0] 
        na = tup[2] # na sales
        eur = tup[3] # eur sales
        jpn = tup[4] # jpn sales
        other = tup[5] # other sales
        total = tup[6] # total sales 
        complete_total += total # adds total sales for each genre 
        # prints desired information according to header row format
        print("{:15s}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}"\
              .format(genre, na, eur, jpn, other, total))
    # prints the total of all the genres' sales added together
    print("\n{:75s}{:<15,.02f}".format('Total Sales', complete_total))    

def display_publisher_data(pub_list):
    ''' This function displays sales data for titles from a publisher. '''
    
    pub = pub_list[0][0] # publisher within the pub_list tuple
    header = ['Title', 'North America', 'Europe', 'Japan', 'Other', 'Global']
    complete_total = 0
    print("\nVideo Games Sales for {}".format(pub)) # header for publisher
    print("{:30s}{:15s}{:15s}{:15s}{:15s}{:15s}".format(*header)) # header row
    
    for tup in pub_list:
        title = tup[1]
        na = tup[3] # na sales
        eur = tup[4] # eur sales
        jpn = tup[5] # jpn sales
        other = tup[6] # other sales
        total = tup[7] # total sales for a publisher
        complete_total += total # adds sales of all the publishers
        # prints desired information according to header row format
        print("{:30s}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}{:<15,.02f}"\
              .format(title[:25], na, eur, jpn, other, total)) 
    # prints the total of all the publishers' sales added together
    print("\n{:90s}{:<15,.02f}".format('Total Sales', complete_total))    

def get_totals(L1, indicator):
    ''' Receives list of information and creates list of either the year's
    games or platforms in a year and an associated list with sales information
    using a dictionary and sorting. '''
    
    L2 = [] # initializes empty list for platform names / years
    L3 = [] # initializes empty list for associated sales
    Dict = {} # initializes empty dictionary for transferring information
    if indicator == 'year':
        for tup in L1:
            platform = tup[1]
            sales = tup[5]
            if platform not in Dict:
                Dict[platform] = sales # makes dictionary key w/ value as sales
            else:
                Dict[platform] += sales # adds sales for dictionary key
        for key in sorted(Dict):
            L2.append(key) # adds platforms to L2
        for index in L2: # sorts dictionary
            L3.append(Dict[index]) # adds sales info to L3
    
    elif indicator == 'platform':
        for tup in L1:
            year = tup[2]
            sales = tup[5]
            if year not in Dict:
                Dict[year] = sales # creates dictionary key w/ sales as value
            else:
                Dict[year] += sales # adds sales for dictionary key
        for key in sorted(Dict): # sorts dictionary
            L2.append(key) # adds year to L2
        for key, value in Dict.items():          
            L3.append(value) # adds sales info to L3
    return L2, L3

def prepare_pie(genres_list):
    ''' This function creates two lists: one of genre names and one with their
    corresponding global sales numbers, done by using the genres_list from 
    get_genre_data. '''
    
    genre_list = [] # first return list initialized
    sales_list = [] # second return list initialized
    transfer_list = [] # list used to move sorted information into desired list
    for tup in genres_list:
        glob_sales = tup[-1] # global sales
        genre = tup[0] 
        genre_sales_tup = (genre, glob_sales) # makes tuples using above info
        transfer_list.append(genre_sales_tup) # appends tuples to transfer list
    # sorts transfer list according to global sales in descending order
    transfer_list.sort(key = itemgetter(1), reverse = True)
    
    for tup in transfer_list: 
        genre = tup[0]
        sales = tup[1]
        genre_list.append(genre) # appends sorted genre strings
        sales_list.append(sales) # appends sorted sales figures
    
    return genre_list, sales_list

def plot_global_sales(x,y,indicator, value):
    '''
        This function plots the global sales per year or platform.
        
        parameters: 
            x: list of publishers or year sorted in ascending order
            y: list of global sales that corresponds to x
            indicator: "publisher" or "year"
            value: the publisher name (str) or year (int)
        
        Returns: None
    '''
    
    if indicator == 'year':    
        pylab.title("Video Game Global Sales in {}".format(value))
        pylab.xlabel("Platform")
    elif indicator == 'platform':    
        pylab.title("Video Game Global Sales for {}".format(value))
        pylab.xlabel("Year")
    
    pylab.ylabel("Total copies sold (millions)")
    
    pylab.bar(x, y)
    pylab.show()

def plot_genre_pie(genre, values, year):
    '''
        This function plots the global sales per genre in a year.
        
        parameters: 
            genre: list of genres that corresponds to y order
            values: list of global sales sorted in descending order 
            year: the year of the genre data (int)
        
        Returns: None
    '''
            
    pylab.pie(values, labels=genre,autopct='%1.1f%%')
    pylab.title("Video Games Sales per Genre in {}".format(year))
    pylab.show()
    
def main():
    fp = open_file() # opens file
    # Menu options for the program
    MENU = '''Menu options
    
    1) View data by year
    2) View data by platform
    3) View yearly regional sales by genre
    4) View sales by publisher
    5) Quit
    
    Enter choice: '''
    
    choice = input(MENU)
    dictionary = read_file(fp) # gets dictionaries for other functions
    D1 = dictionary[0] # recognizes D1
    D2 = dictionary[1] # D2
    D3 = dictionary[2] # D3

    while choice != '5':
        
        #Option 1: Display all platforms for a single year
        if choice == '1':
            try: # guarantees year value is an integer, if not, error given
                year = int(input("Enter year: "))
                indicator = 'year' # for this choice, indicator is year
                L1 = get_data_by_column(D1, indicator, year) 
                if L1 != []: # If List returned from above function isn't empty
                    display_global_sales_data(L1, indicator)
                    plot_input = input("Do you want to plot (y/n)? ")
                    if plot_input == 'y':
                        x = []
                        y = []
                        for tup in L1:
                            publisher = tup[0]
                            sales = tup[5]
                            x.append(publisher)
                            y.append(sales)
                        plot_global_sales(x, y, indicator, year)
                else: # If L1 empty, platform wasn't in data, giving error msg
                    print("The selected year was not found in the data.")
            except ValueError:
                print("Invalid year.")
        
        # Option2: Display data by platform
        elif choice == '2':
            platform = input("Enter platform: ")
            if platform.isdigit(): # ensures platform entry has letters
                print("Invalid platform.") # error message
            else:
                indicator = 'platform' # for this choice, indicator is platform
                L1 = get_data_by_column(D1, indicator, platform) 
                if L1 != []: # If List returned from above function isn't empty
                    display_global_sales_data(L1, indicator) # displays sales
                    plot_input = input("Do you want to plot (y/n)? ")
                    if plot_input == 'y':
                        lists = get_totals(L1, indicator) # gets lists of info
                        x = lists[0] # either a list of platforms or year
                        y = lists[1] # sales data associated  w/ previous list
                        plot_global_sales(x,y,indicator, platform) # plots info
                else: # If L1 empty, platform wasn't in data, gives error msg
                    print("The selected platform was not found in the data.")
        
        # Option 3: Display yearly regional sales by genre
        elif choice == '3':
            try: # ensures year is an integer
                year = int(input("Enter year: "))
                genre_list = get_genre_data(D2, year) # calls_get_genre_data
                if genre_list != []: 
                    display_genre_data(genre_list)
                    plot_input = input("Do you want to plot (y/n)? ")
                    if plot_input == 'y':
                        lists = prepare_pie(genre_list) # the lists returned
                        genre = lists[0] # hold genre
                        sales = lists[1] # and sales lists as their lists
                        plot_genre_pie(genre, sales, year) # plots piechart
                else: # if genre_list is empty, it means year wasn't in data
                    print("The selected year was not found in the data.")
            except ValueError:
                print("Invalid year") # error if non-int year
        
        #Option 4: Display publisher data
        elif choice == '4': 
            # Enter keyword for the publisher name
            publisher = input("Enter keyword for publisher: ")
                # search all publisher with the keyword
            match = [] # for later use
            matcher = [] # for later use
            for key in D3.keys():
                if publisher in key:
                    match.append(key)
            if match == []:
                print('No publisher name containing "{}" was found!'\
                      .format(publisher))
            # print the number of matches found with the keywords
            if len(match) > 1:    
                print("There are {} publisher(s) with the requested" \
                      " keyword!".format(len(match)))
                for i,t in enumerate(match):
                    print("{:<4d}{}".format(i,t))
                    match_tup = (i,t) # i = index t = publisher
                    matcher.append(match_tup) # appends index & publisher
                try:
                    index =input("Select the index for the publisher to use: ")
                except IndexError: 
                    print("Invalid Index.") # error msg
                while index:
                    try:
                        index = int(index) 
                        for i,t in matcher: # for index, publisher
                            if i == index: # now able to use index and 
                                publisher = t # publisher for functions
                        # print("\nVideo Games Sales for {}".format(publisher))
                        pub_list = get_publisher_data(D3, publisher)
                        display_publisher_data(pub_list) # display info
                        break
                    except ValueError:
                        print("Invalid index.")
                        index = input("Select the index for the publisher " \
                                        "to use: ") # reprompts
            else:
                index = 0 # first item because no other options
        else:
            print("Invalid option. Please Try Again!") # error
        choice = input(MENU) # reprints menu
    else:
        print("\nThanks for using the program!")
        print("I'll leave you with this: \"All your base are belong to us!\"")

if __name__ == "__main__":
    main()