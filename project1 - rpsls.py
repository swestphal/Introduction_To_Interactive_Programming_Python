import random

def name_to_number(name):
    """
    converts the string 'name' into a number between 0 and 4
    """
    
    if name == "rock":
        number = 0
    elif name == "Spock":
        number = 1
    elif name == "paper":
        number = 2
    elif name == "lizard":
        number = 3
    elif name == "scissors":
        number = 4
        
    else:
        number = -1
        print "The name is not valid"  
 
    return number


def number_to_name(number):
    """
    converts the number 'number' in the range of 0 to 4
    in the corresponding string
    """
    
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "Spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
        
    else:
        print "The number is not valid"
         
    return name
     
    
def rpsls(player_choice):
    """
    pass player choice, generate random_number for comp_choice
    then check with modulo who wons
    if both have same choice than tie
    """
    
    if (name_to_number(player_choice)!=-1):
        print("\nPlayers chooses "+ player_choice)
        player_number = name_to_number(player_choice)
          
        comp_number = random.randrange(0,5)
        comp_choice = number_to_name(comp_number)
        print("Computer chooses " + comp_choice)
        
        difference = (comp_number - player_number)%5 
        if (difference == 0):
            print("Player and computer tie!") 
       
        elif (difference !=0 and difference <=2):
            print ("Computer wins!")
        
        else: print("Player wins!")
    
    else:
        print("\nGame is over\nPlease retry with new choice")
        return

    
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")