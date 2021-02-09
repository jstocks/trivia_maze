import random


class Adventurer:
    """class creates an instance of an adventurer and holds attributes for
    inventory items and health points"""
    def __init__(self, name):
        self.__name = name
        self.__health_points = random.randint(75, 100)
        self.__healing_potions = []
        self.__vision_potions = 0
        self.__pillar_a = False
        self.__pillar_e = False
        self.__pillar_i = False
        self.__pillar_p = False
        self.__alive = True

    def get_player_name(self):
        """getter for player name"""
        return self.__name

    def set_player_name(self, player):
        """setter for player name"""
        self.__name = player

    def is_alive(self):
        """method to check for a heart beat"""
        return self.__alive

    def pick_up_healing_potion(self):
        """ picks up healing potion and adds it to inventory"""
        healing_potion_amount = random.randint(5, 15)
        self.__healing_potions.append(healing_potion_amount)
        self.__healing_potions.sort()
        print("Found a Healing Potion! It can restore " +
              str(healing_potion_amount) + " health points.\n")

    def pick_up_vision_potion(self):
        """ adds vision potion to inventory"""
        self.__vision_potions += 1
        print("Found a Vision Potion!\n")

    def pick_up_pillar(self, pillar):
        """adds a pillar to adventurer's inventory"""
        if pillar == "A" or pillar == "E" or pillar == "I" or pillar == "P":
            if pillar == "A":
                self.__pillar_a = True
            elif pillar == "E":
                self.__pillar_e = True
            elif pillar == "I":
                self.__pillar_i = True
            elif pillar == "P":
                self.__pillar_p = True
            print("You found pillar " + str(pillar).upper() + "!\n")
        else:
            raise ValueError("A pillar must be A, E, I, or P")

    def use_vision_potion(self):
        self.__vision_potions -= 1
        print("Used a Vision Potion!")

    def use_healing_potion(self):
        """checks if you have healing potion, then provides a menu to select
        which healing potion you want to use, if you have multiple"""
        # make a condition to keep asking user to enter proper input
        condition = False
        # check if player has any potions he can use
        potion_counter = 1
        if len(self.__healing_potions) > 0:
            while not condition:
                # display current health
                print("Current health: " + str(self.__health_points))
                print("Note: Max Health Points is 100\n")
                # display the available healing potions player has
                print("Healing potion inventory: ")
                print("Item Number \tPotion Strength")
                for potion in self.__healing_potions:
                    print(str(potion_counter) + ": \t \t \t \t" + str(potion))
                    potion_counter += 1
            # while not condition:
                # have player select the potion he wants to use
                potion_to_use = int(input("\nSelect the potion (item number) "
                                          "you would like to use, "
                                          "or enter 0 to cancel: "))
                if potion_to_use == 0:
                    condition = True
                    pass
                # check if input is an available index
                elif 0 < potion_to_use <= len(self.__healing_potions):
                    healing_amount = self.__healing_potions[potion_to_use - 1]
                    self.change_health_points(healing_amount)
                    del self.__healing_potions[potion_to_use - 1]
                    print("\nHealed " + str(healing_amount) +
                          " health!\nCurrent health is now " +
                          str(self.__health_points) + "\n")
                    if self.__health_points == 100:
                        print("You're at full health!")
                    condition = True
                else:
                    print("\nThat's not a proper selection!")

        else:
            print("You don't have any healing potions!")

    def change_health_points(self, amount):
        """modifies health points of adventurer if you fall into a pit with
        randomly generated value"""
        if amount < 0:
            self.__health_points += amount
            if self.__health_points < 0:
                self.__health_points = 0
            print("You fell into a pit! Took " + str(amount) + " damage.\n"
                  "Current health: " + str(self.__health_points))
        else:
            self.__health_points += amount
            if self.__health_points > 100:
                self.__health_points = 100

    def fell_into_pit(self):
        """sets the damage taken from falling into a pit, and checks for a
        heartbeat after you land"""
        damage = random.randint(-20, -1)
        self.change_health_points(damage)
        if self.__health_points <= 0:
            self.__alive = False

    def all_pillars_found(self):
        """getter for determining if you can win the gam upon exit"""
        return self.__pillar_a and self.__pillar_i and self.__pillar_e and \
            self.__pillar_p

    def has_healing_potion(self):
        """getter for ability to use healing potions"""
        return len(self.__healing_potions) > 0

    def has_vision_potion(self):
        """getter for ability to use vision potions"""
        return self.__vision_potions > 0

    def __str__(self):
        return self.__name + ":\n" \
               "HP: " + str(self.__health_points) + "\n" \
               "Healing Potions: " + str(self.__healing_potions) + "\n" \
               "Vision Potions: " + str(self.__vision_potions) + "\n" \
               "Pillars found: \n" \
               "A:\t{}\n" \
               "E:\t{}\n" \
               "I:\t{}\n" \
               "P:\t{}\n".format(self.__pillar_a, self.__pillar_e,
                                 self.__pillar_i, self.__pillar_p)
