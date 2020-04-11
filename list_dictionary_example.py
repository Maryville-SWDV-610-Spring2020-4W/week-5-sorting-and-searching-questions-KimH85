import math
from random import randrange

d_person_lucky_number = {}
l_1thru10 = [1,2,3,4,5,6,7,8,9,10]
    
def main():
    
    #creates the dictionary
    setup_lucky_numbers() 
    
    #loop until winner declared
    have_winner = False
    while have_winner == False:
        
        #get a random number not already called and determine
        #if someone had it as a lucky number in dictionary
        have_winner = determine_winner(drawing_number())
    

#sets up dictionary with person and their lucky number    
def setup_lucky_numbers():
    
    #loop until name is not entered by user
    name = None
    while name != "":
        
        #get name of person to be added into dictionary as key
        name = input("\nEnter name. (To exit leave blank) ")
        if name == "":
            break
        
        #determine if name already entered in dictionary - error if true
        if d_person_lucky_number.get(name) != None:
            print("This person is already entered.  One try per person please.")
        
        #if valid, continue...
        else:
            
            #adding entry into dictionary for key with no value.
            d_person_lucky_number[name] = None
            
            #get person's lucky number and add to dictionary
            try:
                lucky_number = int(input("Enter their lucky number between 1-10: "))
                
                #validate the entry, handle error if invalid
                if lucky_number < 1 or lucky_number > 10:
                    lucky_number_error(name)
                   
                #otherwise update dictionary
                else:
                    d_person_lucky_number[name] = lucky_number
                    
            except:
                #if non-integer entered, handle error
                lucky_number_error(name)
    
        
    print("\nGood Luck: ", d_person_lucky_number)
    input("Press Enter to Continue...")

#show error and remove person from dictionary
def lucky_number_error(name):
    print("Must enter an integer value between 1-10.  Try again.")
    del d_person_lucky_number[name]
    
#draw a random number that has not already been selected
def drawing_number():
    
    while True:
        x = randrange(1,10)
        
        #evaluate list index that should hold the value
        #and if value is still there - show and return
        if l_1thru10[x-1] > 0:
            input("\nNumber is " + str(x) + ". Press Enter to Continue...")
            return x

#using random number selected, determine if anyone selected
#as their lucky number - if so announce winner.  If not,
#select next number
def determine_winner(selected_number):
    
    is_winner = False
    
    #loop through dictionary to determine if anyone has selected number
    for name in d_person_lucky_number:
        if d_person_lucky_number[name] == selected_number:
            
            #winner declared - exit loop and return True
            print(name,"WON!  Congratulations!")
            is_winner = True
            
    
    if is_winner == False:
        #if get here - no winner declared.  Update the
        #list, changing selected number to 0 in list and return False
        l_1thru10[selected_number-1] = 0
        print("No winner yet - getting next number.")
    
    return is_winner
 

main()