import os


class Game:
    
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.map_init = Map()
        self.game_map = self.map_init.get_game_map()
        self.game_map[4][2]='p'
        self.player_x = 2
        self.player_y = 4
        self.first_encounter = True
        self.player_location = self.game_map[self.player_y][self.player_x]
        self.prev_location = self.player_location
        self.player =Warrior("player", "male", "player faction")
        # self.player = (self.start())
        # self.live(self.player)

    def live(self,player):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.map_init.print_map()
        if player.just_earned_victory:
            print(player.victory_message)
        while True:
            print(f"you are {player.name} health: {player.max_health} strength: {player.strength} dexterity: {player.dexterity} stamina: {player.max_health} available points: {player.points}")
            menu_choice = input("what do you do:\n1: Embark\n2: level up menu\n3: Rest\n4: Inventory\nYour choice: ")
            if menu_choice == "1":
                self.embark()
            if menu_choice == "2":
                self.level_up_menu(player)

    def embark(self):
        while True:
            self.prev_location = self.game_map[self.player_y][self.player_x]
            self.move()
            print(f"x = {self.player_x} and y = {self.player_y}")

    def move(self, flee=False):
        os.system('cls' if os.name == 'nt' else 'clear')
        self.map_init.print_map()
        while True:
            if flee and self.first_encounter:
                direction = "east"
            else:
                direction = self.get_choices("where to go...\n1: North\n2: East\n3: South\n4: West\n5: Back\nYour choice: ",["north","east","south","west","back"])
            if direction == "north":
                if self.player_y > 0:
                    self.game_map[self.player_y][self.player_x] = self.player_x
                    self.player_y -= 1
                    self.game_map[self.player_y][self.player_x] = 'p'
                    self.map_init.print_map()
                    break
                else:
                    print("can't go further north")
                    self.map_init.print_map()
                    return False
            if direction == "east":
                if  self.player_x > 0:
                    self.game_map[self.player_y][self.player_x] = self.player_x
                    self.player_x -= 1
                    self.game_map[self.player_y][self.player_x] = 'p'
                    self.map_init.print_map()
                    break
                else:
                    print("can't go further east")
                    return False
            if direction == "south":
                if  self.player_y < 9:
                    self.game_map[self.player_y][self.player_x] = self.player_x
                    self.player_y += 1
                    self.game_map[self.player_y][self.player_x] = 'p'
                    self.map_init.print_map()
                    break
                else:
                    print("can't go further south")
                    return False
            if direction == "west":
                if self.player_x < 9:
                    self.game_map[self.player_y][self.player_x] = self.player_x
                    self.player_x += 1
                    self.game_map[self.player_y][self.player_x] = 'p'
                    self.map_init.print_map()
                    break
                else:
                    print("can't go further west")
                    return False
            if direction == "prev":
                self.game_map[self.player_y][self.player_x] = self.player_x
                self.game_map[self.player_y][self.player_x] = 'p'
                self.map_init.print_map()
                break
            if direction == "back":
                self.live(self.player)



    def level_up_menu(self,player):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"current starts: health: {player.max_health} strength: {player.strength} dexterity: {player.dexterity} stamina: {player.max_health} available points: {player.points}")
            level_options = {"1": {"name": "Max health", "variable": "max_health"},
                             "2": {"name": "Strength", "variable":"strength"},
                             "3": {"name": "Dexterity", "variable":"dexterity"},
                             "4": {"name":"Max Stamina","variable":"max_stamina"},
                             "0":"back"}
            # level_choice = input(f"What will you level up?\n1: {level_options["1"]["name"]}\n2: {level_options["2"]["name"]}\n3: {level_options["3"]["name"]}\n4: {level_options["4"]["name"]}\n0: Back\nYour choice: ")
            level_choice = 
            if level_choice=="0":
                self.live(player)
            elif level_choice:
                current_level = getattr(player, level_options[level_choice]["variable"])
                print(f"Current {level_options[level_choice]["name"]}: {current_level}")
                level_amount = input(f"By how much do you want to raise your {level_options[level_choice]["variable"]} (enter 0 to go back): ")
                if int(level_amount) == 0:
                    continue
                if  int(level_amount)<=player.points:
                    setattr(player, level_options[level_choice]["variable"], (current_level+int(level_amount)))
                    player.points -= int(level_amount)
                    self.live(player)
                else:
                    print("Not enough level up points")





    @staticmethod
    def class_selector():
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            cl_input = input("choose class\n1: knight\n2: Warrior\nYour choice: ")
            if cl_input == "1":
                return "Knight"
            elif cl_input == "2":
                return "Warrior"
            else:
                print("invalid selection, please enter a valid option")


    def start(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("welcome to the game")
            ch_name = self.get_non_empty_string("enter your name: ")
            ch_gender = self.get_choices("select your gender\n1: Male\n2:Female\n3:Other\nYour choice: ",["male","female","other"])
            ch_faction=self.get_non_empty_string("enter your faction name: ")
            ch_class = self.get_choices("select your class\n1:Knight\n2:Warrior\nYour choice: ",["Knight","Warrior"])
            player = globals()[ch_class](ch_name, ch_gender, ch_faction)
            feckless1 = Feckless()
            print(player)
            print(f"{player.name} having awoken in a state of dismay finds themselves wondering the forest looking for a source of shelter, suddenly...")
            self.enemy_encounter(player,feckless1)
            return player

    @staticmethod
    def get_non_empty_string(prompt):
        while True:
            value = input(prompt).strip()
            if value:
                if len(value) > 10:
                    print("please use less than 10 characters")
                else:

                    return value
            else:
                print("please enter a valid input")


    @staticmethod
    def get_choices(prompt, choices):
        while True:
                value = input(prompt).strip()
                if value.isdigit():
                    value = int(value)-1
                    if 0 <= value < len(choices):
                        selection = choices[value]
                        print(f"selection: {selection}")
                        if selection=="other":
                            other_in = input("specify your option (more than one character): ").strip()
                            if len(other_in) > 10:
                                print("please use less than 10 characters")
                            if len(other_in) > 1:
                                return other_in
                            else:
                                print("input too short, try again")
                                continue
                        return selection
                    else:
                        print(f"please enter a number between 1 and {len(choices)}")
                else:
                    print("Enter a valid value")



    def enemy_encounter(self, player, enemy):
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            print(f"you are attacked by a {enemy.name}")
            att_in = self.get_choices("What will you do\n1: Attack\n2: Flee\nYour choice: ",["attack","flee"])
            print(att_in)
            if att_in == "attack":
                player.attack(enemy)
                break
            if att_in == "flee":
                if self.first_encounter:
                    self.move(True)
                    break
                if not self.move():
                        print("You are unable to flee")





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
        self.just_earned_victory = False
        self.victory_message = ""
    
    def __str__(self):
        return f"{self.name}, a {self.gender} {self.cl} and a member of the {self.faction} faction"
    
    def attack(self, target):
        while self.health > 0 and target.health > 0:
            print(f"{self.name} attacks")
            print(f"enemy health: {target.health}/{target.max_health}")
            self.stamina -= 4
            print(f"{self.name}'s stamina -4")
            print(f"-{self.strength} health to enemy")
            target.health = target.health-self.strength
            if target.health <= 0:
                self.just_earned_victory = True
                print("enemy died")
                self.points += target.points
                self.victory_message = f"{target.name} died!\nvictory! You have gained {target.points} level points"
                break
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

game = Game()
player = Warrior("player", "male", "player faction")
enemy = Feckless()
game.embark()
