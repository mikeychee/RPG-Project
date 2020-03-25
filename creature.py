import pygame


class Creature:
    def __init__(self, name, type, hp, base_attack, base_defend, base_speed):
        self.name = name
        self.type = type
        self.hp = hp
        self.max_hp = hp
        self.move_set = {}
        self.move_list = []

        self.stats = {'attack': base_attack, 'defence': base_defend, 'speed': base_speed}
        self.properties = {'name': name, 'type': type, 'hp': hp, 'moves': self.move_set, 'stats': self.stats}
        self.super_effective_charts = {'Water': 'Fire',
                                       'Fire': 'Grass',
                                       'Grass': 'Water',
                                       'Normal': '',
                                       'Dark': 'Psychic'}
        self.not_effective_charts = {'Fire': 'Water',
                                     'Water': 'Grass',
                                     'Grass': 'Fire',
                                     'Normal': 'Fighting'}

        self.same_type_charts = {'Fire': 'Fire',
                                 'Grass': 'Grass',
                                 'Water': 'Water',
                                 'Psychic': 'Psychic',
                                 'Dark': 'Dark',
                                 'Normal': None}

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
        return self.move_list[index]

    def take_dmg(self, power, type, creature_type):
        dmg_dealt = int((power * self.stats['attack']) ** (1/3))

        if creature_type == self.super_effective_charts[type]:
            dmg_dealt = dmg_dealt * 2
            self.hp -= int(dmg_dealt)

        elif creature_type == self.not_effective_charts[type] or creature_type == self.same_type_charts[type]:
            dmg_dealt = dmg_dealt / 2
            self.hp -= int(dmg_dealt)

        else:
            self.hp -= dmg_dealt

        return int(dmg_dealt)

    def get_effectiveness(self, type, creature_type):
        # effectiveness:
        # 0 = Normal
        # 1 = Super effective
        # 2 = Not very effective

        effectiveness = 0

        if creature_type == self.super_effective_charts[type]:
            print("It's super effective!")
            effectiveness = 1

        elif creature_type == self.not_effective_charts[type] or creature_type == self.same_type_charts[type]:
            print("Not very effective...")
            effectiveness = 2

        else:
            effectiveness = 0

        return effectiveness



class Wild_Creature(Creature):
    def __init__(self, name, type, hp, base_attack, base_defend, base_speed):
        super().__init__(name, type, hp, base_attack, base_defend, base_speed)

    def wild_creature_ai(self):
        pass


squirtle = Creature('Squirtle', 'Water', 45, 49, 49, 45)
squirtle.set_moves('Tackle', 40, 'Normal')

charmander = Creature('Charmander', 'Fire', 39, 52, 43, 65)
charmander.set_moves('Scratch', 40, 'Normal')
charmander.set_moves('Ember', 40, 'Fire')
charmander.set_moves('Vine Whip', 40, 'Grass')
charmander.set_moves('Water Gun', 40, 'Water')

bulbasaur = Creature('Bulbasaur', 'Grass', 45, 49, 49, 45)
bulbasaur.set_moves('Tackle', 40, 'Normal')

