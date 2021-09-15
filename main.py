import sys
import math

class Factory:
    def __init__(self, id, owner, cyborgs, production):
        self.id = id
        self.owner = owner
        self.cyborgs = cyborgs
        self.production = production

    def __str__(self) -> str:
        return "Factory {} {} {} {}".format(self.id, self.owner, self.cyborgs, self.production)

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
        self.link_count = int(input())  # the number of links between factories
        for i in range(self.link_count):
            factory_1, factory_2, distance = [int(j) for j in input().split()]
        self.factory_dict = {}
        self.troop_dict = {}

    def reset_dicts(self) -> dict:
        self.factory_dict.clear()
        self.troop_dict.clear()

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
            curr_factory = Factory(entity_id, arg_1, arg_2, arg_3)
            the_map.factory_dict[entity_id] = curr_factory
        elif entity_type == 'TROOP':
            curr_troop = Troop(entity_id, arg_1, arg_2, arg_3, arg_4, arg_5)
            the_map.troop_dict[entity_id] = curr_troop

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print(the_map.factory_dict, file=sys.stderr, flush=True)

    max_cyborg = 0
    max_cyborg_fact_id = None
    max_prod = 0
    max_prod_fact_id = None
    min_def = math.inf
    for factory in the_map.factory_dict.values():
        if factory.owner == 1:
            if factory.cyborgs > max_cyborg:
                max_cyborg = factory.cyborgs
                max_cyborg_fact_id = factory.id
        if factory.owner == 0:
            if factory.production > max_prod:
                max_prod = factory.production
                max_prod_fact_id = factory.id
                min_def = factory.cyborgs
            elif factory.production == max_prod and factory.cyborgs < min_def:
                max_prod_fact_id = factory.id
                min_def = factory.cyborgs

    if max_prod_fact_id is None:
        
        for factory in the_map.factory_dict.values():
            if factory.owner == -1:
                if factory.production > max_prod:
                    max_prod = factory.production
                    max_prod_fact_id = factory.id
                    min_def = factory.cyborgs
                elif factory.production == max_prod and factory.cyborgs < min_def:
                    max_prod_fact_id = factory.id
                    min_def = factory.cyborgs

    source = max_cyborg_fact_id
    destination = max_prod_fact_id
    cyborgCount = min_def + 1
    if source and destination:
        print(f"MOVE {source} {destination} {cyborgCount}")
    else:
        print("WAIT")

    # Any valid action, such as "WAIT" or "MOVE source destination cyborgs"
