import math
from random import randrange

players_dictionary = {}
lucky_number_list = []

def main():
    #creates a list of numbers that is used for drawing lucky numbers
    setup_lucky_number_list()
    
    #creates the dictionary
    setup_players_dictionary() 
    
    #loop until winner declared
    have_winner = False
    while have_winner == False:
        
        #get a random number not already called and determine
        #if someone had it as a lucky number in dictionary
        have_winner = determine_winner(drawing_number())

#set up a list of numbers that will be drawn from
def setup_lucky_number_list():
    greatest_number = None
    while greatest_number == None:
        try:
            greatest_number = int(input("Enter an integer that will be used to create the number pool of lucky numbers: "))
            
        except:
            print("Must enter an integer value.  This value will be used to create the number pool to draw lucky numbers. Try again.")
            
    #create list with length set as the selected greatest number
    #add sequential number into the list
    for i in range(greatest_number):
        lucky_number_list.append(i + 1)
        

#sets up dictionary with person and their lucky number    
def setup_players_dictionary():
    
    #loop until name is not entered by user
    name = None
    while name != "":
        
        #get name of person to be added into dictionary as key
        name = input("\nEnter name. (To exit leave blank) ")
        if name == "":
            break
        
        #determine if name already entered in dictionary - error if true
        if players_dictionary.get(name) != None:
            print("This person is already entered.  One try per person please.")
        
        #if valid, continue...
        else:
            
            #adding entry into dictionary for key with no value.
            players_dictionary[name] = None
            
            #get person's lucky number and add to dictionary
            try:
                lucky_number = int(input("Enter their lucky number between 1-" + str(len(lucky_number_list)) + ":"))
                
                #validate the entry, handle error if invalid
                if lucky_number < 1 or lucky_number > len(lucky_number_list):
                    lucky_number_error(name)
                   
                #otherwise update dictionary
                else:
                    players_dictionary[name] = lucky_number
                    
            except:
                #if non-integer entered, handle error
                lucky_number_error(name)
    
        
    print("\nGood Luck: ", players_dictionary)
    input("Press Enter to Continue...")

#show error and remove person from dictionary
def lucky_number_error(name):
    print("Must enter an integer value between 1-" + str(len(lucky_number_list)) + ".  Try again.")
    del players_dictionary[name]
    
    
#draw a random number that has not already been selected
def drawing_number():
    
    while True:
        x = randrange(1,len(lucky_number_list))
        
        #evaluate list index that should hold the value
        #and if value is still there - show and return
        if lucky_number_list[x-1] > 0:
            input("\nNumber is " + str(x) + ". Press Enter to Continue...")
            return x



#using random number selected, determine if anyone selected
#as their lucky number - if so announce winner.  If not,
#select next number
def determine_winner(selected_number):
    
    is_winner = False
    
    #loop through dictionary to determine if anyone has selected number
    for name in players_dictionary:
        if players_dictionary[name] == selected_number:
            
            #winner declared - exit loop and return True
            print(name,"WON!  Congratulations!")
            is_winner = True
            
    
    if is_winner == False:
        #if get here - no winner declared.  Update the
        #list, changing selected number to 0 in list and return False
        lucky_number_list[selected_number-1] = 0
        print("No winner yet - getting next number.")
    
    return is_winner
 

main()