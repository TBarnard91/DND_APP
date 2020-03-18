import random
"""
    Character - Default statistics for a new character (pc or npc)
"""


# Will accept input for HP, AC, initiative bonus, passive perception (saves + spell DC ToDo)
class Character(object):

    def __init__(self, name, max_health, armor_class, initiative_bonus, passive_perception):
        self.name = str(name)

        self.max_health = max_health
        self.current_health = max_health

        self.armor_class = armor_class

        self.initiative_bonus = initiative_bonus
        self.initiative = random.randint(1, 20) + self.initiative_bonus

        self.passive_perception = passive_perception

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def roll_initiative(self):
        self.initiative = random.randint(1, 21) + self.initiative_bonus
        return self.initiative

    def set_initiative(self, initiative):
        self.initiative = initiative

    def get_initiative(self):
        return self.initiative

    def take_damage(self, damage):
        self.current_health -= damage

    def heal(self, healing):
        self.current_health += healing

    def set_current_health(self, hp):
        self.current_health = hp

    def get_current_health(self):
        return self.current_health

    def set_max_health(self, max_health):
        self.max_health = max_health

    def get_max_health(self):
        return self.max_health

    def display_info(self):
        print('\n')
        print(f"Name:  {self.name}")
        print(f"Max HP:  {self.max_health}    Current HP: {self.current_health}")
        print(f"AC: {self.armor_class}")
        print(f"Passive Perception: {self.passive_perception}")
