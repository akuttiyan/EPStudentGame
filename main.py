from archetype import Player
import keyboard

print(keyboard.read_key)
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

    print(player.archetype)

def buy_supplies():

    
    
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
            
    #pass

# save player state in variables here

def game_loop():
    # month passes
    # action
    # Randomly pre-scheduled event
    pass

def finish():
    pass

buy_supplies()