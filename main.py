from archetype import Player
import keyboard


def load_game():
    # If they have preloaded gamestate, load that here
    pass

def choose_archetype():
    continue_input = input("Hello. Welcome to EPS Trail. Your goal is to make it through 4 years of EPS. First you need to choose an arcehtype. Type yes to continue to the possible archetypes.")

    if continue_input == "yes":
        print("Here are the possible archetypes:")
        print("Academic Weapon-- GPA: 4.0")
        print("STEM Overachiever-- GPA: 3.95")
        print("Humanaties Overachiver-- GPA: 3.95")
        print("Theatre/Arts kid-- GPA: 3.7")
        print("Ultimate Frisbee Kid-- GPA: 3.7")
        print("Class Ditcher-- GPA: 3.1")
        chosen_archetype = input("Which archetype do you want to be?")
        player = Player(chosen_archetype)

        return player

player = choose_archetype()
def buy_supplies(player):

   


    '''
    print("Now it's time to buy supplies. Here are your options:")
    print("1. Books")
    print("2. Calculator")
    print("3. Pens/Pencils")
    print("4. Notebooks")
    print("5. Computer Quality")
    print("6. Charger")
    print("7. Stylus")
    print("Press spacebar to exit the supplies")
    supplies_input = input("What would you like to buy? (Press the number)")
    '''
    '''
    while keyboard.read_key != "space":

        if supplies_input == "1":
            num_books = input("How many books would you like to buy for the school year?")

            print("Now it's time to buy supplies. Here are your options:")
            print("1. Books")
            print("2. Calculator")
            print("3. Pens/Pencils")
            print("4. Notebooks")
            print("5. Computer Quality")
            print("6. Charger")
            print("7. Stylus")
            print("Press spacebar to exit the supplies")
            supplies_input = input("What would you like to buy? (Press the number)")
        if supplies_input == "2":
            calculator = input("What type of calculator do you want?")

            print("Now it's time to buy supplies. Here are your options:")
            print("1. Books")
            print("2. Calculator")
            print("3. Pens/Pencils")
            print("4. Notebooks")
            print("5. Computer Quality")
            print("6. Charger")
            print("7. Stylus")
            print("Press spacebar to exit the supplies")
            supplies_input = input("What would you like to buy? (Press the number)")

        if supplies_input == "3":
            num_pencils = input("How many pens pencils do you want?")

            print("Now it's time to buy supplies. Here are your options:")
            print("1. Books")
            print("2. Calculator")
            print("3. Pens/Pencils")
            print("4. Notebooks")
            print("5. Computer Quality")
            print("6. Charger")
            print("7. Stylus")
            print("Press spacebar to exit the supplies")
            supplies_input = input("What would you like to buy? (Press the number)")
           

        if supplies_input == "4":
            num_notebooks = input("How many notebooks do you want?")

            print("Now it's time to buy supplies. Here are your options:")
            print("1. Books")
            print("2. Calculator")
            print("3. Pens/Pencils")
            print("4. Notebooks")
            print("5. Computer Quality")
            print("6. Charger")
            print("7. Stylus")
            print("Press spacebar to exit the supplies")
            supplies_input = input("What would you like to buy? (Press the number)")
            

        if supplies_input == "5":
            computer_type = input("What computer type do you want?")
 
            print("Now it's time to buy supplies. Here are your options:")
            print("1. Books")
            print("2. Calculator")
            print("3. Pens/Pencils")
            print("4. Notebooks")
            print("5. Computer Quality")
            print("6. Charger")
            print("7. Stylus")
            print("Press spacebar to exit the supplies")
            supplies_input = input("What would you like to buy? (Press the number)")
            

        if supplies_input == "6":
            num_chargers = input("How many chargers do you want?")
            
            print("Now it's time to buy supplies. Here are your options:")
            print("1. Books")
            print("2. Calculator")
            print("3. Pens/Pencils")
            print("4. Notebooks")
            print("5. Computer Quality")
            print("6. Charger")
            print("7. Stylus")
            print("Press spacebar to exit the supplies")
        supplies_input = input("What would you like to buy? (Press the number)")
          
    
        if supplies_input == "7":
            num_styluses = input("How many styluses do you want?")
            
            print("Now it's time to buy supplies. Here are your options:")
            print("1. Books")
            print("2. Calculator")
            print("3. Pens/Pencils")
            print("4. Notebooks")
            print("5. Computer Quality")
            print("6. Charger")
            print("7. Stylus")
            print("Press spacebar to exit the supplies")
            supplies_input = input("What would you like to buy? (Press the number)")
        
    if keyboard.read_key == "space":
        print("You are ready for the school year")
'''
    #space_not_pressed = True
    supplies_input = "x"
    while supplies_input != "8":
        
        print("Now it's time to buy supplies. Here are your options:")
        print("1. Books")
        print("2. Calculator")
        print("3. Pens/Pencils")
        print("4. Notebooks")
        print("5. Computer Quality")
        print("6. Charger")
        print("7. Stylus")
        print("8. Exit")
        print("Press spacebar to exit the supplies")
        supplies_input = input("What would you like to buy? (Press the number) ")

        if supplies_input == "1":
            num_books = input("How many books would you like to buy for the school year? ")
            player.add_num_books(int(num_books))
        elif supplies_input == "2":
            calculator = input("What type of calculator do you want? ")
            player.add_calc_type(calculator)
        elif supplies_input == "3":
            num_pencils = input("How many pens/pencils do you want? ")
            player.add_num_pens(int(num_pencils))
        elif supplies_input == "4":
            num_notebooks = input("How many notebooks do you want? ")
            player.add_num_notebooks(int(num_notebooks))
        elif supplies_input == "5":
            computer_type = input("What computer type do you want? ")
            player.add_comp_type(computer_type)
        
        elif supplies_input == "6":
            num_chargers = input("How many chargers do you want? ")
            player.add_num_chargers(int(num_chargers))
          
        elif supplies_input == "7":
            num_styluses = input("How many styluses do you want? ")
            player.add_num_styluses(int(num_styluses))
        elif supplies_input == "8":
            print("Exit")

        else:
            supplies_input = input("Choose one of the options ")

        print("You are ready for the school year")
        print("Here are your supplies")
        print("Notebooks:", player.num_books)
    
            

    '''
    while keyboard.read_key != "space":
        
        print("Now it's time to buy supplies. Here are your options:")
        print("1. Books")
        print("2. Calculator")
        print("3. Pens/Pencils")
        print("4. Notebooks")
        print("5. Computer Quality")
        print("6. Charger")
        print("7. Stylus")
        print("Press spacebar to exit the supplies")
        supplies_input = input("What would you like to buy? (Press the number) ")

        if supplies_input == "1":
            num_books = input("How many books would you like to buy for the school year? ")
            player.add_num_books(int(num_books))
        elif supplies_input == "2":
            calculator = input("What type of calculator do you want? ")
            player.add_calc_type(calculator)
        elif supplies_input == "3":
            num_pencils = input("How many pens/pencils do you want? ")
            player.add_num_pens(int(num_pencils))
        elif supplies_input == "4":
            num_notebooks = input("How many notebooks do you want? ")
            player.add_num_notebooks(int(num_notebooks))
        elif supplies_input == "5":
            computer_type = input("What computer type do you want? ")
            player.add_comp_type(computer_type)
        
        elif supplies_input == "6":
            num_chargers = input("How many chargers do you want? ")
            player.add_num_chargers(int(num_chargers))
          
        elif supplies_input == "7":
            num_styluses = input("How many styluses do you want? ")
            player.add_num_styluses(int(num_styluses))
        else:
            supplies_input = input("Choose one of the options ")
    
            

    if keyboard.read_key == "space":
        print("You are ready for the school year")

    '''

#chosen_archetype = choose_archetype()      
buy_supplies(player)     
            
    #pass

# save player state in variables here

def game_loop():
    # month passes
    # action
    # Randomly pre-scheduled event
    pass

def finish():
    pass
