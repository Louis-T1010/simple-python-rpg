class character:
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
            return "victory"
        else:
            print(f"enemy health: {target.health}/{target.max_health}")        
            target.attack(self)

class Map:
    def __init__(self):
        for x in range(10):
            for y in range(10):
                self.game_map={x,y}

class GodmodeDebug:
    @staticmethod
    def enable_godmode(target):
        for stat in target.__dict__:
            if stat != "name" and stat != "gender" and stat != "faction" and stat != "cl":
                setattr(target, stat, 1000)
        print(f"godmode activated {target.name} now has 1000 of every stat")
        

    
class Knight(character):
    def __init__(self, name, gender, faction):
        super().__init__(name, gender, faction, "knight", 14, 20, 8, 14)


    
class Warrior(character):
    def __init__(self, name, gender, faction):
        super().__init__(name, gender, faction, "warrior", 11, 14, 21, 17)

        
class bear:
    def __init__(self):
        self.max_health = 100
        self.health = 100
        self.strength = 9
        self.speed = 4
        self.max_stamina = 50
        self.stamina = 50
        
    def attack(self, target):
        print(f"the bear attacks {target.name}")
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

class Combat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        player.attack(enemy)
        
map = Map()
with open ("notes.txt","w") as file_object:
    for line in map.game_map: 