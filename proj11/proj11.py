# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 20:48:54 2020

@author: ab43p
"""

''' This program allows the user to play a game as a student who's running late
for their CSE231 Exam, running through a building and its classrooms looking 
for materials needed for the exam as well as the room where the exam is being 
taken. This program makes use of 3 classes; Student, Classroom, and Rush, in 
order to integrate the functions and methods for each aspect of thegame in a 
way in which the player can search through rooms, picking up & dropping items
along the way, until they've won or quit.? '''

#DO NOT DELETE THis LINES
MAP = {"U":"Up","D":"Down","L":"Left","R":"Right"}

class Student(object):
    ''' This class creates a student for the game, starting with an empty 
    backpack, the ability to be placed in another room, the ability to pickup / 
    drop items, as well as methods for representing this information. '''
    
    def __init__(self, item_list=None, classroom_id=-1):
        '''Initializes yourself, with an empty backpack by default. The 
           default position of the student is room -1.'''

        if item_list == None:
            self.backpack = []
        else:
            self.backpack = item_list
        self.classroom_id = classroom_id # sets instance to the id

    def __repr__(self):
        '''Returns a string representation of the student.'''

        return self.__str__()

    def __str__(self):
        '''Returns a string representing the student's inventory.'''
        
        s = "Backpack: "
        if len(self.backpack) == 0:
            s += "Empty"
        else:
            for item in self.backpack:
                s += item + ", "
            else:
                s = s[:-2] # remove trailing comma and space
        return s

    def __eq__( self, S ):
        ''' Checks that the classroom id and backpack are the same for the 
        instance and the inputted student'''
        
        if S.classroom_id == self.classroom_id and S.backpack == self.backpack:
            return True
        else:
            return False
     
    def place(self, classroom_id):
        ''' Places the student into the room at classroom_id. '''
    
        # sets the instance of student's class ID equal to the inputted ID
        self.classroom_id = classroom_id # effectively 'placing' them there
    
    def add_item(self, item):
        ''' Adds item to the student's backpack, if the backpack not full '''
        
        # if backpack isn't full, add item 
        if 6 > len(self.backpack): 
            self.backpack.append(item) # adds item to backpack
        else:
            print("Backpack is full.")
        
    def remove_item(self, item):
        ''' Removes item from student's backpack, if it is inside.
            Returns True if able to remove, False if item not present as well
            as printing an error message. '''
        
        if item not in self.backpack: # can't remove an item that's not inside
            print("Failed to remove item from backpack.")
            return False
        else: # removes item because it for sure is inside
            self.backpack.remove(item)
            return True

class Classroom(object):
    ''' This class creates an instance of a classroom (single room at a time),
    with a list of items found in the room that can be picked up & the ability
    for this list to be expanded by the user dropping an item from the student
    backpack. Also initializes a dictionary with all of the room's exits, and
    has a method to check if a class exists in the direction the user wants to 
    go, among other methods. Another notable method is get_win, which checks to
    see if the player has won the game. '''
    
    def __init__(self, text_desc="0 empty"):
        '''Initialzes a classroom. By default it has id 0 and is a "empty" 
         room with no inventory or exits.'''
        
        description = text_desc.split()
        self.id = int(description[0])
        self.course = description[1]
        # Initialize a dictionary of potential exits as empty
        self.exits = {}
        # Initialize a "backpack" of items as empty list
        self.backpack = []

        for item in description[2:]:
            # if the first character is uppercase & second is a number (ex: U3)
            if item[0].isupper() and item[1].isdigit():
                # the key to the dictionary is the direction indicator [UDLR]
                self.exits[item[0]] = int(item[1:]) # the value is the number
            elif item[0].isalpha() and not item[0].isupper():
                self.backpack.append(item)
        
    def __repr__(self):
        '''Returns a string representation of the classroom.'''
       
        classroom_repr = '''Classroom("''' + repr(self.id) + " " + self.course
        
        # had to change this: added a .replace to remove ' ' that showed up 
        for direction in self.exits: # around the number values for directions
            classroom_repr += " {}".format(direction) + \
                repr(self.exits[direction]).replace("'","")

        for item in self.backpack:
            classroom_repr += " " + item

        classroom_repr += '''")'''

        return classroom_repr

    def __str__(self):
        '''Returns a string representing the room in a nice conversational 
            style.'''

        # Basic classroom description
        classroom_str = "You see a " + self.course + " classroom."

        # List the things in the classroom
        if len(self.backpack) == 1:
            classroom_str += " On the desk you see a " + \
                             self.backpack[0] + "."
        if len(self.backpack) == 2:
            classroom_str += " On the desk you see a " + \
                             self.backpack[0] + \
                             " and a " + self.backpack[1] + "."
        elif len(self.backpack) > 2:
            classroom_str += " On the desk you see "
            for item in self.backpack[:-1]:
                classroom_str += "a " + item + ", "
            classroom_str += "and a " + self.backpack[-1] + "."

        # List the exits
        if len(self.exits) == 0:
            classroom_str += " Run through the classroom grab what you need "\
                "(if possible). Exit and run to the exam!"
        elif len(self.exits) == 1:
            classroom_str += " Run through the classroom grab what you need "\
                "(if possible). Now, run into the hallway and go " + \
                             MAP[list(self.exits.keys())[0]] + "."
        elif len(self.exits) == 2:
            classroom_str += " Run through the classroom grab what you need"\
                " (if possible). Now, run into the hallway and go " + \
                             MAP[list(self.exits.keys())[0]] + " or " + \
                                 MAP[list(self.exits.keys())[1]] + "."
        elif len(self.exits) > 2:
            classroom_str += " Run through the classroom grab what you need"\
                " (if possible). Now, run into the hallway and go "
            for direction in list(self.exits.keys())[:-1]:
                classroom_str += MAP[direction] + ", "
            classroom_str += "or " + MAP[list(self.exits.keys())[-1]] + "."

        return classroom_str
    
    def __eq__( self, C ):
        ''' If the classroom 'C' is the same as the current classroom, returns
        True, otherwise returns False '''
    
        # checks that ID, course, exits, and backpack are all equal to inputted
        # classroom C for the instance (self)
        if C.id == self.id and C.course == self.course and C.exits == \
            self.exits and C.backpack == self.backpack: 
            return True
        else:
            return False
    
    def add_item(self, item):
        ''' This one-liner adds an item to the classroom's inventory. '''
    
        self.backpack.append(item) # appends item to list
        
    def remove_item(self, item):
        ''' This if statement checks to see if an item is in the classroom's
            inventory, and removes it if so, otherwise prints an error '''
        
        if item in self.backpack:
            self.backpack.remove(item) # removes from list
            return True
        else:
            print("Failure to find the item in the classroom.") # error msg
            return False
        
    def get_room(self, direction):
        ''' If direction user chooses has an exit, the room # is returned 
            Returns False if an exit doesn't exist in the direction chosen,
            returns the integer value attached to the exit if exit exists '''
        
        keys = self.exits.keys() # keys of the dictionary of exits for a room
        if direction not in keys: # user direction not a possible exit
            return False
        
        for key, value in self.exits.items():
            if direction == key: # if the direction is a key, return the ID
                return int(value)
            
class Rush(object):
    ''' This class controls the interactions between the Student & Classroom 
    classes, reading a file of classrooms then iterating through it to create
    a dictionary of classrooms that are used to play the game. Printing the
    game's instructions occurs in this class, as well as actually moving the 
    student between classrooms as well as moving items between Student & Room
    inventories. '''
    
    def __init__(self, filename="rushing.txt"):
        '''Initializes the student rushing to class.  The student starts in 
           the classroom with the lowest id.'''

        self.student = Student() # initializes student
        self.classrooms = {} # sets up empty dictionary for classrooms
        fp = open(filename) # opens file
        for line in fp: # iterates through each line in the file
            line = line.strip()
            class_id = int(line.split()[0])
            # print(class_id)
            self.classrooms[class_id] = Classroom(line) # adds dict entries
        # Place the student in the room with lowest id
        self.student.place(min(self.classrooms.keys()))
        # print(self.classrooms)
        
    def __repr__(self):
        '''Returns a string representation.'''

        return self.__str__()

    def __str__(self):
        '''Returns a string representing the journey to the class, simply "\
            giving the number of rooms.'''
        search_str = "You are searched in "
        if len(self.classrooms) == 0:
            search_str += "no classrooms at all, you are in the hallway. You "\
                "are late run in a random class and get items from the desks."
        elif len(self.classrooms) == 1:
            search_str += "a classroom."
        else:
            search_str += "a set of " + str(len(self.classrooms)) + \
                          " classrooms."

        return search_str

    def intro(self):
        '''Prints an introduction to the search for items because you are late
        This prompt includes the commands.'''
        
        print("\nAHHHH! I'm late for class\n")
        print("*runs out the house to catch the bus with an empty backpack*")

        print("\nYou're popular and have friends in many classes. Find and "\
              "collect any items you find useful for your exam.")
        print("You are already late, and have a CSE231 Final Exam in 10 "\
              "mins.\n")
        self.print_help()


    def print_help(self):
        '''Prints the valid commands.'''
        
        print("Use your instincts: ")
        print("*thinks*.. *thinks*.. what to do?!?!?!?!")
        print("*running*")
        print("S or search -- prints a description of the classroom you ran "\
              "into")
        print("B or backpack - prints a list of items in your backpack")
        print("P pencil or pickup pencil - *mental* instruction to pick up "\
              "an item called pencil")
        print("DR pencil or drop pencil - *mental* instruction to drop off "\
              "an item called pencil")
        print("U or up - *mental* instruction to up the hallway to find "\
              "another classroom")
        print("D or down - *mental* instruction to down the hallway to find "\
              "another classroom")
        print("R or right - *mental* instruction to right in the hallway to "\
              "find another classroom")
        print("L or left - *mental* instruction to left in the hallway to "\
              "find another classroom")
        print("G or giveup - I have no more time, I need to get to class!!!")
        print("H or help - prints this list of options again")
        print()
        print("Remember that uppercase and lowercase SHOULD NOT matter. ")
        print("JUST GRAB WHAT YOU NEED AND GET TO CLASS TO START YOUR FINAL "\
              "EXAM!!! HURRYYYY!!!")
        print()

    def prompt(self):
        '''Prompts for input and handles it, whether by error message or 
        handling a valid command. Returns True as long as the user has not 
        chosen to quit, False if they have.'''

        print("In room {} with course {}".format(self.student.classroom_id,\
                                                 self.classrooms[self.student\
                                                                 .classroom_id\
                                                                     ].course))
        print(self.student)
        user_input = input("Enter a command (H for help): ")
        print()

        # Handle input: split for pickup/drop, capitalization unimportant
        input_list = user_input.split()

        if len(input_list) == 0:
            user_input = "?"  # No command is not a valid command
            return False
        else:
            try:
                command = input_list[0].upper()  # The command
                if len(input_list) > 1:
                    item = input_list[1]
                if command == 'S':
                    self.search()
                elif command == 'B':
                    self.backpack()
                elif command == 'P':
                    self.pickup(item)
                elif command == 'DR':
                    self.drop(item)
                elif command in "UDLR":
                    self.move(command)
                elif command == 'G':
                    print("I have no more time, I need to get to class!!!")
                    return False
                elif command == 'H':
                      self.print_help() 
                else:
                    print("Unfortunately, that's not a valid option.")
                    return False
            except:
                print("Problem with the option or the item.")
                return False
        if self.win():
            return "win"
        return True

    def search(self):
        '''Prints the description of the current room.'''
        
        current_classroom = self.classrooms[self.student.classroom_id]
        print(current_classroom)

    def backpack(self):
        '''Prints the student's current inventory in their backpack.'''
        
        # prints the student's backpack per __str__ in Student class
        self.student.__str__

    def pickup(self, item):
        '''Coordinates movement of an object from the student's current
        1) determine the current_classroom (hint: see search method)
        2) remove the item from current_classroom
        3) add the item to student's backpack.'''
    
        # gets the room id that the student is in, then finds the value
        # of the dictionary key that is the ID, in order for the remove_item 
        # method called in the 3rd line of code to work.
        current_room_id = self.student.classroom_id
        current_room = self.classrooms[current_room_id]
        # for remove_item in Classroom class, I went and added return True & 
        # return False to the if statement in order for the if statement here
        # to work.
        pickup = current_room.remove_item(item)
        if pickup:
            self.student.add_item(item)
    
    def drop(self, item):
        '''Coordinates movement of an object from the student's inventory
        1) determine the current_classroom (hint: see search method)
        2) remove the item from the student's backpack.
        3) add the item to the current_classroom.'''
        # gets the room id that the student is in, then finds the value
        # of the dictionary key that is the ID, in order for the add_item 
        # method called to work.
        current_room_id = self.student.classroom_id
        current_room = self.classrooms[current_room_id]
        # inside of remove_item method, added return True/False in order to 
        # get if statement to work.
        drop = self.student.remove_item(item)
        if drop:
            current_room.add_item(item)
        
    def move(self, direction):
        '''Coordinates the movement of students between rooms.
        1) determine the current classroom (hint: see search method)
        2) get the classroom_id of the room in the specified direction
        3) if there is a classroom_id, 'place' the student in the room
            (hint: you actually place the room in the student)
        '''
        # gets the room id that the student is in, then finds the value
        # of the dictionary key that is the ID, in order for the get_room 
        # method called in the 3rd line of code to work.
        current_room_id = self.student.classroom_id
        current_room = self.classrooms[current_room_id]
        # sees if the next room exists based on direction user chooses to go
        next_room = current_room.get_room(direction)
        if next_room: # if existent in particular direction:
            # places student in room using place from Student class
            self.student.place(next_room)
            print("You went " + MAP[direction] + " and found a new classroom.")
        else:
            errMsg = "Unfortunately, you went " + MAP[direction] + " and "\
                "there was no classroom."
            print(errMsg)

    def win(self):
        ''' Checks that the course for the room the student is in is CSE 231
            and that the student's backpack has all of the materials needed '''
        
        winning_backpack = ['cheatsheet', 'eraser', 'paper', 'pencil']
        current_room_id = self.student.classroom_id
        current_room = self.classrooms[current_room_id]
        if current_room.course == "CSE231" and sorted(self.student.backpack) \
            == winning_backpack:
            return True
        else:
            return False
    
def main():
    ''' Prompts the user for a file, then plays that file until the user 
        chooses to give up. Does not check formatting of input file. '''

    while True:
        try:
            filename = input("Enter a text filename: ")
            escapade = Rush(filename)
            break
        except IOError:
            print("Cannot open file:{}. Please try again.".format(filename))
            continue
    
    escapade.intro()
    escapade.__str__()
    escapade.search()
    
    keep_going = True
    while keep_going:
        keep_going = escapade.prompt()
        if keep_going == 'win':
            break
    if keep_going == 'win':
        print("You succeeded!")
    else:
        print("Thank you for playing")

if __name__ == "__main__":    
    main()
