import random
import pickle

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.armor = None
        self.weapon = None
        self.inventory = []

    def attack(self):
        base_damage = random.randint(5, 15)
        if self.weapon:
            base_damage += self.weapon.damage_bonus
            self.weapon.ammo_count -= 1
            if self.weapon.ammo_count == 0:
                print("Out of ammo! Choose another weapon.")
                self.weapon = None
        return base_damage

    def defense(self):
        base_defense = random.randint(5, 20)
        if self.armor:
            base_defense += self.armor.defense_bonus
        return base_defense

    def show_inventory(self):
        print("\nInventory:")
        for item in self.inventory:
            print(item)

    def taken_damage(self, damage):
        self.health -= damage

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def equip_armor(self, armor):
        self.armor = armor

class Food:
    def __init__(self, name, health_bonus):
        self.name = name
        self.health_bonus = health_bonus

    def __str__(self):
        return f"{self.name} (Health Bonus: {self.health_bonus})"

class FirstAid:
    def __init__(self, name, health_bonus):
        self.name = name
        self.health_bonus = health_bonus

    def __str__(self):
        return f"{self.name} (Health Bonus: {self.health_bonus})"

class Weapon:
    def __init__(self, name, damage_bonus, ammo_capacity):
        self.name = name
        self.damage_bonus = damage_bonus
        self.ammo_capacity = ammo_capacity
        self.ammo_count = ammo_capacity

    def attack(self):
        if self.ammo_count > 0:
            return self.damage_bonus
        else:
            print("Out of ammo! Choose another weapon.")
            return 0

class Armor:
    def __init__(self, name, defense_bonus):
        self.name = name
        self.defense_bonus = defense_bonus

    def __str__(self):
        return f"{self.name} (Defense Bonus: {self.defense_bonus})"

class Building:
    def __init__(self, building_type):
        self.building_type = building_type


class Food:
    def __init__(self, name, health_bonus):
        self.name = name
        self.health_bonus = health_bonus

    def __str__(self):
        return f"{self.name} (Health Bonus: {self.health_bonus})"

class FirstAid:
    def __init__(self, name, health_bonus):
        self.name = name
        self.health_bonus = health_bonus

    def __str__(self):
        return f"{self.name} (Health Bonus: {self.health_bonus})"

class Weapon:
    def __init__(self, name, damage_bonus, ammo_capacity):
        self.name = name
        self.damage_bonus = damage_bonus
        self.ammo_capacity = ammo_capacity
        self.ammo_count = ammo_capacity

    def attack(self):
        # Calculate attack damage with consideration for ammo
        if self.ammo_count > 0:
            self.ammo_count -= 1
            return self.damage_bonus
        else:
            print("Out of ammo! Choose another weapon.")
            return 0

class Armor:
    def __init__(self, name, defense_bonus):
        self.name = name
        self.defense_bonus = defense_bonus

    def __str__(self):
        return f"{self.name} (Defense Bonus: {self.defense_bonus})"

class Building:
    def __init__(self, building_type):
        self.building_type = building_type

def intro():
    print("The zombie apocalypse has begun ... ")
    print("You are in a mostly deserted town after the evacuation.")
    print("The streets are dead silent apart from a lone zombie that is approaching. ")

def explore_town(player):
    is_night = False
    #base_built = False

    while True:
        if is_night:
            print("It's nighttime.")
        else:
            print("It's daytime.")

        print("[1] Scavenge for supplies")
        print("[2] Show Inventory")
        print("[3] Eat To Rebuild Health")
        print("[4] Use First Aid")
        print("[5] Confront Zombie")
        print("[6] Save Game")
        print("[7] Load Game")
        print("[8] Quit the game")

        choice = input("\nWhat would you like to do: ")

        if choice == "1":
            scavenge(player)
        elif choice == "2":
            player.show_inventory()
        elif choice == "3":
            eat(player)
        elif choice == "4":
            first_aid(player)
        elif choice == "5":
            confront_zombie(player)
        elif choice == "6":
            save_game(player)
        elif choice == "7":
            player = load_game()
            if player:
                explore_town(player)
        elif choice == "8":
            print("You have decided to quit the game. ): ")
            exit()
        else:
            print("Invalid Choice. \n")

def scavenge(player):

    print("[1] House")
    print("[2] Supermarket")
    print("[3] Pharmacy")
    print("[4] Hospital")
    print("[5] Police Station")
    print("[6] Hardware Store")
    print("[7] Gas Station")
    print("[8] Library")
    print("[9] School")
    print("[10] Factory")
    print("[11] Church")

    choice = input("\nChoose a building to scavenge for supplies! \n")

    if choice == "1":
        print("You decided to scavenge the House.")
        loot_chance = random.random()

        if loot_chance < 0.2:
            new_food = get_random_food()
            print(f"You have found {new_food.name}! \n")
            player.inventory.append(new_food)
        elif loot_chance < 0.4:
            new_weapon = get_random_weapon()
            print(f"You have found a {new_weapon.name}! \n")
            player.inventory.append(new_weapon)
        elif loot_chance < 0.6:
            new_first_aid = get_random_first_aid()
            print(f"You have found a {new_first_aid.name}! \n")
            player.inventory.append(new_first_aid)
        elif loot_chance < 0.8:
            new_armor = get_random_armor()
            print(f"You have found a {new_armor.name}! \n")
            player.inventory.append(new_armor)
        else:
            print("You have attracted a zombie! \n")
            confront_zombie(player)

    elif choice == "2":
        print("You decided to scavenge the supermarket.")
        loot_chance = random.random()

        if loot_chance < 0.5:
            new_food = get_random_food()
            print(f"You have found {new_food.name}! \n")
            player.inventory.append(new_food)
        elif loot_chance < 0.6:
            new_weapon = get_random_weapon()
            print(f"You have found a {new_weapon.name}! \n")
            player.inventory.append(new_weapon)
        elif loot_chance < 0.7:
            new_first_aid = get_random_first_aid()
            print(f"You have found a {new_first_aid.name}! \n")
            player.inventory.append(new_first_aid)
        elif loot_chance < 0.9:
            new_armor = get_random_armor()
            print(f"You have found a {new_armor.name}! \n")
            player.inventory.append(new_armor)
        else:
            print("You have attracted a zombie! \n")
            confront_zombie(player)

    elif choice == "3":
        print("You decided to scavenge the pharmacy.")
        loot_chance = random.random()

        if loot_chance < 0.1:
            new_food = get_random_food()
            print(f"You have found {new_food.name}! \n")
            player.inventory.append(new_food)
        elif loot_chance < 0.2:
            new_weapon = get_random_weapon()
            print(f"You have found a {new_weapon.name}! \n")
            player.inventory.append(new_weapon)
        elif loot_chance < 0.8:
            new_first_aid = get_random_first_aid()
            print(f"You have found a {new_first_aid.name}! \n")
            player.inventory.append(new_first_aid)
        elif loot_chance < 0.9:
            new_armor = get_random_armor()
            print(f"You have found a {new_armor.name}! \n")
            player.inventory.append(new_armor)
        else:
            print("You have attracted a zombie! \n")
            confront_zombie(player)

    elif choice == "4":
        print("You decided to scavenge the hospital.")
        loot_chance = random.random()

        if loot_chance < 0.1:
            new_food = get_random_food()
            print(f"You have found {new_food.name}! \n")
            player.inventory.append(new_food)
        elif loot_chance < 0.2:
            new_weapon = get_random_weapon()
            print(f"You have found a {new_weapon.name}! \n")
            player.inventory.append(new_weapon)
        elif loot_chance < 0.8:
            new_first_aid = get_random_first_aid()
            print(f"You have found a {new_first_aid.name}! \n")
            player.inventory.append(new_first_aid)
        elif loot_chance < 0.9:
            new_armor = get_random_armor()
            print(f"You have found a {new_armor.name}! \n")
            player.inventory.append(new_armor)
        else:
            print("You have attracted a zombie! \n")
            confront_zombie(player)

    elif choice == "5":
        print("You decided to scavenge the police station.")
        loot_chance = random.random()

        if loot_chance < 0.2:
            new_food = get_random_food()
            print(f"You have found {new_food.name}! \n")
            player.inventory.append(new_food)
        elif loot_chance < 0.7:
            new_weapon = get_random_weapon()
            print(f"You have found a {new_weapon.name}! \n")
            player.inventory.append(new_weapon)
        elif loot_chance < 0.8:
            new_first_aid = get_random_first_aid()
            print(f"You have found a {new_first_aid.name}! \n")
            player.inventory.append(new_first_aid)
        elif loot_chance < 0.9:
            new_armor = get_random_armor()
            print(f"You have found a {new_armor.name}! \n")
            player.inventory.append(new_armor)
        else:
            print("You have attracted a zombie! \n")
            confront_zombie(player)

    elif choice == "6":
        print("You decided to scavenge the hardware store.")
        loot_chance = random.random()

        if loot_chance < 0.1:
            new_food = get_random_food()
            print(f"You have found {new_food.name}! \n")
            player.inventory.append(new_food)
        elif loot_chance < 0.3:
            new_weapon = get_random_weapon()
            print(f"You have found a {new_weapon.name}! \n")
            player.inventory.append(new_weapon)
        elif loot_chance < 0.4:
            new_first_aid = get_random_first_aid()
            print(f"You have found a {new_first_aid.name}! \n")
            player.inventory.append(new_first_aid)
        elif loot_chance < 0.9:
            new_armor = get_random_armor()
            print(f"You have found a {new_armor.name}! \n")
            player.inventory.append(new_armor)
        else:
            print("You have attracted a zombie! \n")
            confront_zombie(player)

    elif choice == "7":
        print("You decided to scavenge the gas station.")
        loot_chance = random.random()

        if loot_chance < 0.5:
            new_food = get_random_food()
            print(f"You have found {new_food.name}! \n")
            player.inventory.append(new_food)
        elif loot_chance < 0.6:
            new_weapon = get_random_weapon()
            print(f"You have found a {new_weapon.name}! \n")
            player.inventory.append(new_weapon)
        elif loot_chance < 0.7:
            new_first_aid = get_random_first_aid()
            print(f"You have found a {new_first_aid.name}! \n")
            player.inventory.append(new_first_aid)
        elif loot_chance < 0.8:
            new_armor = get_random_armor()
            print(f"You have found a {new_armor.name}! \n")
            player.inventory.append(new_armor)
        else:
            print("You have attracted a zombie! \n")
            confront_zombie(player)

    elif choice == "8":
        print("You decided to scavenge the library.")
        loot_chance = random.random()

        if loot_chance < 0.2:
            new_food = get_random_food()
            print(f"You have found {new_food.name}! \n")
            player.inventory.append(new_food)
        elif loot_chance < 0.4:
            new_weapon = get_random_weapon()
            print(f"You have found a {new_weapon.name}! \n")
            player.inventory.append(new_weapon)
        elif loot_chance < 0.6:
            new_first_aid = get_random_first_aid()
            print(f"You have found a {new_first_aid.name}! \n")
            player.inventory.append(new_first_aid)
        elif loot_chance < 0.8:
            new_armor = get_random_armor()
            print(f"You have found a {new_armor.name}! \n")
            player.inventory.append(new_armor)
        else:
            print("You have attracted a zombie! \n")
            confront_zombie(player)

    elif choice == "9":
        print("You decided to scavenge the school.")
        loot_chance = random.random()

        if loot_chance < 0.2:
            new_food = get_random_food()
            print(f"You have found {new_food.name}! \n")
            player.inventory.append(new_food)
        elif loot_chance < 0.4:
            new_weapon = get_random_weapon()
            print(f"You have found a {new_weapon.name}! \n")
            player.inventory.append(new_weapon)
        elif loot_chance < 0.6:
            new_first_aid = get_random_first_aid()
            print(f"You have found a {new_first_aid.name}! \n")
            player.inventory.append(new_first_aid)
        elif loot_chance < 0.8:
            new_armor = get_random_armor()
            print(f"You have found a {new_armor.name}! \n")
            player.inventory.append(new_armor)
        else:
            print("You have attracted a zombie! \n")
            confront_zombie(player)

    elif choice == "10":
        print("You decided to scavenge the factory.")
        loot_chance = random.random()

        if loot_chance < 0.1:
            new_food = get_random_food()
            print(f"You have found {new_food.name}! \n")
            player.inventory.append(new_food)
        elif loot_chance < 0.3:
            new_weapon = get_random_weapon()
            print(f"You have found a {new_weapon.name}! \n")
            player.inventory.append(new_weapon)
        elif loot_chance < 0.5:
            new_first_aid = get_random_first_aid()
            print(f"You have found a {new_first_aid.name}! \n")
            player.inventory.append(new_first_aid)
        elif loot_chance < 0.8:
            new_armor = get_random_armor()
            print(f"You have found a {new_armor.name}! \n")
            player.inventory.append(new_armor)
        else:
            print("You have attracted a zombie! \n")
            confront_zombie(player)

    elif choice == "11":
        print("You decided to scavenge the church.")
        loot_chance = random.random()

        if loot_chance < 0.2:
            new_food = get_random_food()
            print(f"You have found {new_food.name}! \n")
            player.inventory.append(new_food)
        elif loot_chance < 0.3:
            new_weapon = get_random_weapon()
            print(f"You have found a {new_weapon.name}! \n")
            player.inventory.append(new_weapon)
        elif loot_chance < 0.6:
            new_first_aid = get_random_first_aid()
            print(f"You have found a {new_first_aid.name}! \n")
            player.inventory.append(new_first_aid)
        elif loot_chance < 0.8:
            new_armor = get_random_armor()
            print(f"You have found a {new_armor.name}! \n")
            player.inventory.append(new_armor)
        else:
            print("You have attracted a zombie! \n")
            confront_zombie(player)
def get_random_food():
    foods = [
        Food("Peanut Butter", 5),
        Food("Energy Bar", 3),
        Food("MRE", 15),
        Food("Canned Peaches", 5),
        Food("Canned Pears", 5),
        Food("Canned Pineapple", 5),
        Food("Canned Applesauce", 3),
        Food("Canned Cherries", 3),
        Food("Canned Grapes", 3),
        Food("Canned Green Beans", 4),
        Food("Canned Corn", 4),
        Food("Canned Peas", 3),
        Food("Canned Carrots", 3),
        Food("Canned Tomatoes", 4),
        Food("Canned Potatoes", 7),
        Food("Canned Mushrooms", 4),
        Food("Flatbread", 8),
        Food("Rye Bread", 8),
        Food("Sourdough Bread", 8),
        Food("Chocolate Bar", 3),
        Food("Bottled Watter", 5),
        Food("Water Jug", 10),
        Food("Soup", 12),
        Food("Protein Powder", 8),
        Food("Spam", 10),
        Food("Tuna", 13),
        Food("Canned Chicken", 13),
        Food("Canned Beef", 13),
        Food("Canned Pork", 13),
        Food("Canned Sardines", 10),
        Food("Canned Turkey", 13),
        Food("Canned Salmon", 13),
        Food("Soda", 2),
        Food("Energy Drink", 3)

    ]
    return random.choice(foods)

def get_random_first_aid():
    first_aid_kits = [
        FirstAid("Bandages", 8),
        FirstAid("Small First Aid Kit", 8),
        FirstAid("Medium First Aid Kit", 12),
        FirstAid("Large First Aid Kit", 15),
        FirstAid("Bandaid", 2),
        FirstAid("Pain Killers", 8),
        FirstAid("Antibiotics", 10),
        FirstAid("Vitamins", 5)

    ]
    return random.choice(first_aid_kits)

def get_random_weapon():
    weapons = [
        Weapon("Axe", 5, 1000000000000000),
        Weapon("Bat", 3, 1000000000000000),
        Weapon("Knife", 4, 1000000000000000),
        Weapon("Frying Pan", 2, 1000000000000000),
        Weapon("Machete", 6, 1000000000000000),
        Weapon("Sword", 7, 1000000000000000),
        Weapon("Sledge Hammer", 5, 1000000000000000),
        Weapon("Rifle", 20, 20),
        Weapon("Pistol", 10, 20),
        Weapon("Sub Machine Gun", 15, 50),
        Weapon("Throwing Knives", 5, 1000000000000000),
        Weapon("Molotov", 5, 1000000000000000),
        Weapon("Grenade", 40, 1000000000000000),
        Weapon("Flamethrower", 8, 500),
        Weapon("Taser", 2, 1000000000000000),
        Weapon("Chainsaw", 7, 1000000000000000)

    ]
    return random.choice(weapons)

def get_random_armor():
    armor = [
        Armor("Baseball Cap", 2),
        Armor("Leather Gloves", 2),
        Armor("Duct Tape Helmet", 3),
        Armor("Duct Tape Chest Plate", 3),
        Armor("Leather Jacket", 5),
        Armor("Motorcycle helmet", 6),
        Armor("Tactical Vest", 8),
        Armor("Knee Pads", 4),
        Armor("Elbow Pads", 4),
        Armor("Riot Shield", 10),
        Armor("Riot Helmet", 12),
        Armor("Kevlar Vest", 15),
        Armor("Combat Helmet", 13),
        Armor("Hockey Pads",25),
        Armor("Metal Sheet Armor", 18),
        Armor("Reinforced Boots", 8),

    ]
    return random.choice(armor)

# Function to eat from the inventory
def eat(player):
    print("\nInventory:")
    for i, item in enumerate(player.inventory, start=1):
        if isinstance(item, Food):
            print(f"[{i}] {item.name} (Health Bonus: {item.health_bonus})")

    choice = input("\nChoose a number to eat or press Enter to go back: ")
    if choice.isdigit() and 1 <= int(choice) <= len(player.inventory):
        selected_food = player.inventory.pop(int(choice) - 1)
        player.health += selected_food.health_bonus
        print(f"You have eaten {selected_food.name} and restored your health to {player.health}\n")
    elif choice:
        print("Invalid choice. \n")

def first_aid(player):
    print("\nInventory:")
    for i, item in enumerate(player.inventory, start=1):
        if isinstance(item, FirstAid):
            print(f"[{i}] {item.name} (Health Bonus: {item.health_bonus})")

    choice = input("\nChoose a number for first aid or press Enter to go back: ")
    if choice.isdigit() and 1 <= int(choice) <= len(player.inventory):
        selected_first_aid = player.inventory.pop(int(choice) - 1)
        player.health += selected_first_aid.health_bonus
        print(f"You used {selected_first_aid.name} and restored your health to {player.health}\n")
    elif choice:
        print("Invalid choice. \n")

# Function to initiate zombie confrontation
def confront_zombie(player):
    zombie_health = 77
    print(f"\nYou are confronting the zombie\nZombie health: {zombie_health}\n")

    while zombie_health > 0:
        print(f"Player's health: {player.health}")
        print("[1] Choose Weapon")
        print("[2] Run")

        choice = input("\nWhat would you like to do: ")

        if choice == "1":
            weapon = select_weapon(player)
            if weapon:
                fight(player, zombie_health, weapon)
                drop_loot(player)
                break
        elif choice == "2":
            run(player)
            break
        else:
            print("Invalid Choice.\n")

    print("You have defeated the zombie!")

def select_weapon(player):
    def select_weapon(player):
        print("\nSelect a weapon:")
        print("[0] None")

        for i, item in enumerate(player.inventory):
            if isinstance(item, Weapon):
                print(f"[{i + 1}] {item.name} [{item.ammo_count}]")

        weapon_index = input("Enter the number of the weapon to use (or press Enter to go back): ")

        if str(weapon_index).isdigit():
            weapon_index = int(weapon_index)
            if 0 <= weapon_index < len(player.inventory):
                if weapon_index == 0:
                    return None  # Choosing None
                weapon = player.inventory[weapon_index - 1]
                if isinstance(weapon, Weapon):
                    return weapon
                else:
                    print("Invalid selection. Not a weapon.")
            else:
                print("Invalid selection. Please enter a valid number.")
        else:
            print("Invalid selection. Please enter a valid number.")

        return None

# Function to select armor from inventory
def select_armor(player):
    print("\nSelect an armor:")
    for i, item in enumerate(player.inventory):
        if isinstance(item, Armor):
            print(f"[{i + 1}] {item.name} ")

    armor_index = input("Enter the number of the Armor to use (or press Enter to go back): ")

    if armor_index.isdigit():
        armor_index = int(armor_index) - 1
        if 0 <= armor_index < len(player.inventory):
            armor = player.inventory[armor_index]
            if isinstance(armor, Armor):
                return armor
            else:
                print("Invalid selection.")
    else:
        print("Invalid selection. Please enter a valid number.")

    return None

# Function for the player to fight the zombie
def fight(player, zombie_health, weapon):
    while zombie_health > 0 and player.health > 0:
        print("\nPlayer's health:", player.health)
        print("Zombie's health:", zombie_health, "\n")
        print("[1] Attack")

        choice = input("\nWhat would you like to do: ")

        if choice == "1":
            if weapon is not None:
                player_damage = weapon.attack()
                zombie_damage = random.randint(5, 15)

                print(f"You dealt {player_damage} damage to the zombie\n")
                zombie_health -= player_damage

                if zombie_health <= 0:
                    print("You defeated the zombie!\n")
                    print("Your health is now:", player.health, "\n")
                    break
                else:
                    print(f"The zombie attacks you and dealt {zombie_damage} damage.\n")
                    player.taken_damage(zombie_damage)

                    if player.health <= 0:
                        print("Game Over! The zombie got you.\n")
                        exit()


            else:

                # If the player has no weapon, deal a default damage

                default_damage = random.randint(5, 10)  # Adjust default damage as needed

                print(f"You attack the zombie and dealt {default_damage} damage.\n")

                zombie_health -= default_damage

                if zombie_health <= 0:

                    print("You defeated the zombie!\n")

                    print("Your health is now:", player.health, "\n")

                    break

                else:

                    zombie_damage = random.randint(5, 15)

                    print(f"The zombie attacks you and dealt {zombie_damage} damage.\n")

                    player.taken_damage(zombie_damage)

                    if player.health <= 0:
                        print("Game Over! The zombie got you.\n")

                        exit()


# Function for the player to run from the zombie
def run(player):
    print("You have decided to run from the zombie. \n")

    while True:
        # Add a chance for the zombie to catch up
        catch_chance = random.random()
        if catch_chance < 0.3:
            print("You couldn't escape! The zombie catches up to you.")
            # Force the player to fight
            confront_zombie(player)
            break
        else:
            print("You successfully escaped from the zombie!\n")
            break

# Function to drop loot (food or weapon) after defeating the zombie
def drop_loot(player):
    loot_chance = random.random()

    if loot_chance < 0.5:
        new_food = get_random_food()
        print(f"The zombie dropped {new_food.name}! \n")
        player.inventory.append(new_food)
    else:
        new_weapon = get_random_weapon()
        print(f"The zombie dropped a {new_weapon.name}! \n")
        choice = input("Do you want to pick it up? [1 for yes, 2 for no]: ")
        if choice == "1":
            player.inventory.append(new_weapon)

def save_game(player):
    with open("savegame.dat", "wb") as save_file:
        pickle.dump(player, save_file)
    print("Game saved.")

def load_game():
    try:
        with open("savegame.dat", "rb") as save_file:
            player = pickle.load(save_file)
        print("Game loaded.")
        return player
    except FileNotFoundError:
        print("No saved game found.")
        return None

def main():
    player_name = input("Enter your name: ")
    player = Player(player_name)
    intro()
    explore_town(player)

if __name__ == "__main__":
    main()