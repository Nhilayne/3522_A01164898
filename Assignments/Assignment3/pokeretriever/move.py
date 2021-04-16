from pokedexobject import PokedexObject


class Move(PokedexObject):

    def __init__(self, name, id, generation, accuracy, pp, power, type, dmg, effect):
        super(Move, self).__init__(name, id)
        self.generation = generation
        self.accuracy = accuracy
        self.pp = pp
        self.power = power
        self.type = type
        self.dmg = dmg
        self.effect = effect

    def __str__(self):
        return f"Move: Name: {self.name}, ID: {self.id}" \
               f", Generation: {self.generation}, Accuracy: {self.accuracy}, " \
               f", PP: {self.pp}, Power: {self.power}, " \
               f", Type: {self.type}, Damage: {self.dmg}, Effect: {self.effect}"
