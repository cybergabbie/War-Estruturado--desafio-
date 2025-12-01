import random

class Unit:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)

class WarGame:
    def __init__(self):
        self.map_size = 5
        self.map = [['.' for _ in range(self.map_size)] for _ in range(self.map_size)]
        self.units = {
            'player': [Unit('Soldier', 100, 20, 10) for _ in range(3)],
            'enemy': [Unit('Soldier', 100, 20, 10) for _ in range(3)]
        }
        self.current_turn = 'player'

    def move_unit(self, unit_index, dx, dy):
        # Simples movimento (não implementado totalmente)
        pass

    def attack(self, attacker_index, target_index, target_team):
        attacker = self.units[self.current_turn][attacker_index]
        target = self.units[target_team][target_index]
        if attacker.is_alive() and target.is_alive():
            damage = attacker.attack
            target.take_damage(damage)
            if not target.is_alive():
                self.units[target_team].pop(target_index)

    def check_win(self):
        if not self.units['enemy']:
            return 'player'
        if not self.units['player']:
            return 'enemy'
        return None

    def run(self):
        while not self.check_win():
            print(f"Turno: {self.current_turn}")
            # Simular ações aleatórias para demo
            if self.units[self.current_turn]:
                attacker_idx = random.randint(0, len(self.units[self.current_turn]) - 1)
                target_team = 'enemy' if self.current_turn == 'player' else 'player'
                if self.units[target_team]:
                    target_idx = random.randint(0, len(self.units[target_team]) - 1)
                    self.attack(attacker_idx, target_idx, target_team)
            self.current_turn = 'enemy' if self.current_turn == 'player' else 'player'
        print(f"Vencedor: {self.check_win()}")

game = WarGame()
game.run()
