class Player:
    def __init__(self, archetype):
        self.archetype = archetype



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
    


