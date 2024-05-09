class Player:
    def __init__(self, archetype):
        self.archetype = archetype
        self.num_books = 0
        self.num_pens = 0
        self.num_notebooks = 0
        self.num_chargers = 0
        self.num_styluses = 0
    
    def add_num_books(self, num_books):
        self.num_books += num_books

    def add_calc_type(self, calc_type):
        self.calc_type = calc_type

    def add_calc_type(self, calc_type):
        self.calc_type = calc_type

    def add_num_pens(self, num_pens):
        self.num_pens += num_pens

    def add_num_notebooks(self, num_notebooks):
        self.num_notebooks += num_notebooks
    
    def add_comp_type(self, comp_type):
        self.comp_type = comp_type
    
    def add_num_chargers(self, num_chargers):
        self.num_chargers += num_chargers

    def add_num_styluses(self, num_styluses):
        self.num_styluses += num_styluses

    
    
    



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
    



