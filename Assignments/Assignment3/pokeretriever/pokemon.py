from pokedexobject import PokedexObject


class Pokemon(PokedexObject):

    def __init__(self, name, id, height, weight, stats, types, abilities, moves):
        super(Pokemon, self).__init__(name, id)
        self.height = height
        self.weight = weight
        self.stats = stats
        self.types = types
        self.abilities = abilities
        self.moves = moves

    def __str__(self):
        return f"Pokemon: Name: {self.name}, ID: {self.id}" \
               f", Height: {self.height} decimetres, Weight: {self.weight} hectograms, " \
               f", Stats: {self.stats}, Types: {self.types}, " \
               f", Abilities: {self.abilities}, Moves: {self.moves}"
