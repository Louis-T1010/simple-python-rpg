import os


class Game:
    
    def __init__(self):
        self.map_init = Map()
        self.game_map = self.map_init.get_game_map()
        self.game_map[4][2]='p'
        self.player_x = 0
        self.player_y = 0
        self.get_x_and_y()
        self.player_location = self.game_map[self.player_y][self.player_x]

        self.live(self.start())

    def live(self,player):
        while True:
            print(f"you are {player.name} health: {player.health} stamina: {player.stamina} ")
            menu_choice = input("what do you do:\n1: Embark\n2: level up menu\n3: Rest\n4: Inventory\nYour choice: ")
            if menu_choice == "1":
                self.embark()
            if menu_choice == "2":
                self.level_up_menu(player)

    def embark(self):
        print(self.player_location)
        self.map_init.print_map()
        self.get_x_and_y()
        while True:
            direction = input("what direction do you go:\n1: north\n2: east\n3: south\n4: west\nYour choice: ")
            self.game_map[self.player_y][self.player_x] = self.player_x
            if direction == "1":
                self.player_y -= 1
                self.game_map[self.player_y][self.player_x] = 'p'
                self.map_init.print_map()
            if direction == "2":
                self.player_x -= 1
                self.game_map[self.player_y][self.player_x] = 'p'
                self.map_init.print_map()
            if direction == "3":
                self.player_y += 1
                self.game_map[self.player_y][self.player_x] = 'p'
                self.map_init.print_map()
            if direction == "4":
                self.player_x += 1
                self.game_map[self.player_y][self.player_x] = 'p'
                self.map_init.print_map()

            print(f"x = {self.player_x} and y = {self.player_y}")

    def get_x_and_y(self):
        x = 0
        y = 0
        for row in self.game_map:
            y+=1
            for loc in row:
                x += 1
                if loc == 'p':
                    x -= 1
                    y -= 1
                    self.player_x = x
                    self.player_y = y
                    print(f"x = {self.player_x} and y = {self.player_y}")
                    break
                if x == 10:
                    x = 0



    def level_up_menu(self,player):
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            print(f"current starts: health: {player.max_health} strength: {player.strength} dexterity: {player.dexterity} stamina: {player.max_health} available points: {player.points}")
            level_options = {"1": {"name": "Max health", "variable": "max_health"},
                             "2": {"name": "Strength", "variable":"strength"},
                             "3": {"name": "Dexterity", "variable":"dexterity"},
                             "4": {"name":"Max Stamina","variable":"max_stamina"},
                             "0":"back"}
            level_choice = input(f"What will you level up?\n1: {level_options["1"]["name"]}\n2: {level_options["2"]["name"]}\n3: {level_options["3"]["name"]}\n4: {level_options["4"]["name"]}\n0: Back\nYour choice: ")
            if level_choice=="0":
                self.live(player)
            elif level_choice:
                current_level = getattr(player, level_options[level_choice]["variable"])
                print(current_level)
                level_amount = input(f"By how much do you want to raise your {level_options[level_choice]["variable"]}: ")
                if  int(level_amount)<=player.points:
                    setattr(player, level_options[level_choice]["variable"], (current_level+int(level_amount)))
                    player.points -= int(level_amount)
                    self.live(player)
                else:
                    print("Not enough level up points")





    @staticmethod
    def class_selector():
        while True:
            cl_input = input("choose class\n1: knight\n2: Warrior\nYour choice: ")
            if cl_input == "1":
                return "Knight"
            elif cl_input == "2":
                return "Warrior"
            else:
                print("invalid selection, please enter a valid option")


    def start(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("welcome to the game")
        ch_name = input("enter your name: ")
        ch_gender=input("enter your gender: ")
        ch_faction=input("enter your faction name: ")
        ch_class = self.class_selector()
        player = globals()[ch_class](ch_name, ch_gender, ch_faction)
        feckless1 = Feckless()
        print(f"{player.name} having awoken in a state of dismay finds themselves wondering the forest looking for a source of shelter, suddenly...")
        print(f"Suddenly you're attacked by a {feckless1.name}, he seeks to strike what will you do?")
        while player.health > 0 and feckless1.health > 0:
            att_input = input("will you: \n1: Strike\n2: Flee\nYour choice: ")
            if att_input == "activate god mode":
                GodModeDebug.enable_godmode(player)
            if att_input == "1":
                Combat(player,feckless1)
            elif att_input == "2":
                print("you run away")
                break        
        return player
        

class Character:
    def __init__(self, name, gender, faction, cl, base_health, base_strength, base_dexterity, base_stamina):
        self.name = name
        self.gender = gender
        self.faction = faction
        self.cl = cl
        self.base_health = base_health
        self.max_health = base_health
        self.health = base_health
        self.base_strength = base_strength
        self.strength = base_strength        
        self.base_dexterity = base_dexterity
        self.dexterity = base_dexterity
        self.base_stamina = base_stamina
        self.max_stamina = base_stamina
        self.stamina = base_stamina
        self.points = 0
    
    def __str__(self):
        return f"{self.name}, a {self.gender} {self.cl} and a member of the {self.faction} faction"
    
    def attack(self, target):
        print(f"{self.name} attacks")
        print(f"enemy health: {target.health}/{target.max_health}")
        self.stamina -= 4
        print(f"{self.name}'s stamina -4")
        print(f"-{self.strength} health to enemy")
        target.health = target.health-self.strength
        if target.health <= 0:
            print("enemy died")
            self.points += target.points
            print(f"victory! You have gained {target.points} level points")
        else:
            print(f"enemy health: {target.health}/{target.max_health}")        
            target.attack(self)
            
class Live:
    def __init__(self):
        pass

class Map:
    def __init__(self):
        self.game_map = []
        for x in range(10):
            row = []
            for y in range(10):
                row.append(y)
            self.game_map.append(row)


    def print_map(self):
        for row in self.game_map:
            print(row)

    def get_game_map(self):
        return self.game_map


    def print_map_to_file(self):
        with open("map.txt", "w") as file:
            for row in self.game_map:
                file.write(" ".join(str(cell) for cell in row) + "\n")

    

class GodModeDebug:
    @staticmethod
    def enable_godmode(target):
        for stat in target.__dict__:
            if stat != "name" and stat != "gender" and stat != "faction" and stat != "cl":
                setattr(target, stat, 1000)
        print(f"godmode activated {target.name} now has 1000 of every stat")
        

    
class Knight(Character):
    def __init__(self, name, gender, faction):
        super().__init__(name, gender, faction, "knight", base_health=14, base_strength=20, base_dexterity=8, base_stamina=14)


    
class Warrior(Character):
    def __init__(self, name, gender, faction):
        super().__init__(name, gender, faction, "warrior", base_health=11, base_strength=14, base_dexterity=21, base_stamina=17)

class Enemy:
    def __init__(self):
        self.name = "Enemy"
        self.max_health = 0
        self.health = 0
        self.strength = 0
        self.speed = 0
        self.max_stamina = 0
        self.stamina = 0
        self.points = 0


    def attack(self, target):
        print(f"the {self.name} attacks {target.name}")
        print(f"{target.name}'s health: {target.health}/{target.max_health}")
        self.stamina -= 4
        print(f"the bear's stamina -4")
        target.health -= self.strength
        print(f"-{self.strength} health to {target.name}")
        if target.health <= 0:
            print(f"{target.name} died")
            return "death"
        else:       
            print(f"{target.name}'s health: {target.health}/{target.max_health}")
        print("")


class Bear(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Bear"
        self.max_health = 100
        self.health = 100
        self.strength = 9
        self.speed = 4
        self.max_stamina = 50
        self.stamina = 50
        self.points = 20

class Feckless(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "Feckless bandit"
        self.max_health = 17
        self.health = 17
        self.strength = 2
        self.speed = 2
        self.max_stamina = 10
        self.stamina = 10
        self.points = 5
        

class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        player.attack(enemy)

# game = Game()
# game_map = Map()
# # game_map.print_map_to_file()
# game.embark()
