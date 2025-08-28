import entity_manager

print("welcome to the game")
ch_name = input("enter your name: ")
ch_gender=input("enyer your gender: ")
ch_faction=input("enter your faction name: ")
def class_selector():
    while True:    
        cl_input = input("choose class\n1: kight\n2: Warrior\nYour choice: ")
        if cl_input == "1":
            return "Knight"
            break
        elif cl_input == "2":
            return "Warrior"
            break
        else:
            print("invlid selection, please enter a valid option")
ch_class = class_selector()
player = getattr(entity_manager, ch_class)(ch_name, ch_gender, ch_faction)
print(f"{player.name} having awoken in a state of dismay finds themselves wondering the forest looking for a source of shelter")
print(f"Suddenly you're charged by a large agitated bear, he seeks to strike what will you do?")
bear1 = entity_manager.bear()
while player.health > 0 and bear1.health > 0:
    att_input = input("will you: \n1: Strike\n2: Flee\nYour choice: ")
    if att_input == "activate godmode":
        entity_manager.GodmodeDebug.enable_godmode(player)
    if att_input == "1":
        entity_manager.Combat(player,bear1)
    elif att_input == "2":
        print("you run away")
        break
        
