import sys
import math

class Factory:
    def __init__(self, id, owner=None, cyborgs=None, production=None):
        self.id = id
        self.owner = owner
        self.cyborgs = cyborgs
        self.production = production
        self.link = {}

    def __str__(self) -> str:
        return "Factory {} {} {} {}".format(self.id, self.owner, self.cyborgs, self.production)

    def update(self, owner, cyborgs, prod) -> None:
        self.owner = owner
        self.cyborgs = cyborgs
        self.production = prod

class Troop:
    def __init__(self, id, owner, source, target, cyborgs, turns) -> None:
        self.id = id
        self.owner = owner
        self.source = source
        self.target = target
        self.cyborgs = cyborgs
        self.turns_left = turns

class Map:
    def __init__(self):
        self.factory_count = int(input())  # the number of factories
        self.factory_dict = {fact_id: Factory(fact_id) for fact_id in range(self.factory_count)}
        self.link_count = int(input())  # the number of links between factories
        self.lap_counter = 0
        for i in range(self.link_count):
            factory_1, factory_2, distance = [int(j) for j in input().split()]
            self.factory_dict[factory_1].link[factory_2] = distance
            self.factory_dict[factory_2].link[factory_1] = distance
        self.troop_dict = {}

    def reset_dicts(self) -> dict:
        self.lap_counter += 1
        self.troop_dict.clear()

    def make_decision(self):
        to_print = []

        for fact_id, fact in self.factory_dict.items():
            if fact.owner == 1:
                min_dist = math.inf
                closest_enemy = None
                for enemy_id, dist in fact.link.items():
                    if dist < min_dist and self.factory_dict[enemy_id].owner != 1:
                        min_dist = dist
                        closest_enemy = enemy_id
                
                print(closest_enemy, file=sys.stderr)
                if closest_enemy is not None:
                    to_print.append(f"MOVE {fact_id} {closest_enemy} {fact.cyborgs}")
        
        if self.lap_counter == 10 or self.lap_counter == 20:
            max_prod = -1
            destination = None
            for fact_id, fact in self.factory_dict.items():
                if fact.owner == -1 and fact.production > max_prod:
                    max_prod = fact.production
                    destination = fact_id
            
            if destination is not None:
                min_dist = math.inf
                source = None
                for source_id, dist in self.factory_dict[destination].link.items():
                    if dist < min_dist and self.factory_dict[source_id].owner == 1:
                        min_dist = dist
                        source = source_id
                
                if source is not None:
                    to_print.append(f"BOMB {source} {destination}")

        if len(to_print) > 0:
            print(";".join(to_print))
        else:
            print("WAIT")


the_map = Map() 
# game loop
while True:
    the_map.reset_dicts()
    entity_count = int(input())  # the number of entities (e.g. factories and troops)
    for i in range(entity_count):
        inputs = input().split()
        entity_id = int(inputs[0])
        entity_type = inputs[1]
        arg_1 = int(inputs[2])
        arg_2 = int(inputs[3])
        arg_3 = int(inputs[4])
        arg_4 = int(inputs[5])
        arg_5 = int(inputs[6])
        
        if entity_type == 'FACTORY':
            the_map.factory_dict[entity_id].update(arg_1, arg_2, arg_3)
            print(the_map.factory_dict[entity_id], file=sys.stderr, flush=True)
        elif entity_type == 'TROOP':
            curr_troop = Troop(entity_id, arg_1, arg_2, arg_3, arg_4, arg_5)
            the_map.troop_dict[entity_id] = curr_troop

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    the_map.make_decision()
    # Any valid action, such as "WAIT" or "MOVE source destination cyborgs"
