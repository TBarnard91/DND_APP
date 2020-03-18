from character import Character


class CharacterFunctions(object):
    def __init__(self, char_list):
        self.character_list = char_list

    # Sorts the characters by current initiative and displays it.
    def display_list(self):
        print('\n')
        for item in sorted(self.character_list, key=lambda x: x.get_initiative(), reverse=True):
            print(f"{item.get_name()}: {item.get_initiative()}")

    # Rolls a new initiative for each character.
    def reroll_initiatives(self):
        for item in self.character_list:
            item.roll_initiative()

    # Deletes a character from the list
    def remove_character(self):
        temp_name = input("\nEnter the name of character to be removed: ")
        check = True

        while check:
            for item in self.character_list:
                if item.get_name() == temp_name:
                    self.character_list.remove(item)
                    check = False
        if check:
            print("Character not found.")

    """
    Adds a new character from the list
    """

    def add_character(self):
        temp_name = str(input("\nEnter name:"))
        temp_max_health = int(input("Enter max health: "))
        temp_armor_class = int(input("Enter armor class: "))
        temp_initiative_bonus = int(input("Enter initiative bonus: "))
        temp_passive_perception = int(input("Enter passive perception: "))

        new_character = Character(temp_name, temp_max_health, temp_armor_class, temp_initiative_bonus,
                                  temp_passive_perception)
        self.character_list.append(new_character)