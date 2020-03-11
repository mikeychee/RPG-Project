import pygame


class Creature:
    def __init__(self, name, type, hp, base_attack, base_defend, base_speed):
        self.name = name
        self.type = type
        self.hp = hp
        self.move_set = {}
        self.move_list = []


        self.stats = {'attack': base_attack, 'defence': base_defend, 'speed': base_speed}
        self.properties = {'name': name, 'type': type, 'hp': hp, 'moves': self.move_set, 'stats': self.stats}

    def set_moves(self, move, power, move_type):
        self.move_set[move] = (power, move_type)
        self.move_list.append(move)


    def set_stats(self, d_attack, d_defend, d_speed):
        self.stats['attack'] += d_attack
        self.stats['defence'] += d_defend
        self.stats['speed'] += d_speed

    def set_properties(self):
        self.properties['name'] = self.name
        self.properties['type'] = self.type
        self.properties['hp'] = self.hp

    def get_move(self, index):
        return self.move_list


class Wild_Creature(Creature):
    def __init__(self, name, type, hp, base_attack, base_defend, base_speed):
        super().__init__(name, type, hp, base_attack, base_defend, base_speed)

    def wild_creature_ai(self):
        pass


squirtle = Creature('Squirtle', 'Water', 45, 49, 49, 45)
squirtle.set_moves('Tackle', 40, 'Normal')

charmander = Creature('Charmander', 'Fire', 39, 52, 43, 65)
charmander.set_moves('Scratch', 40, 'Normal')

bulbasaur = Creature('Bulbasaur', 'Grass', 45, 49, 49, 45)
bulbasaur.set_moves('Tackle', 40, 'Normal')
