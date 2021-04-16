from Assignments.Assignment3.pokeretriever.pokedexobject import PokedexObject


class Stats(PokedexObject):
    def __init__(self, name, id, battle):
        super(Stats, self).__init__(name, id)
        self.is_battle_only = battle

    def __str__(self):
        return f"PokedexObject: Name: {self.name}, ID: {self.id}, Battle Only: {self.is_battle_only}"
