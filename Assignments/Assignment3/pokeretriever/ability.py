from pokedexobject import PokedexObject


class Ability(PokedexObject):

    def __init__(self, name, id, generation, effect, shorteffect, pokemon):
        super(Ability, self).__init__(name, id)
        self.generation = generation
        self.effect = effect
        self.short_effect = shorteffect
        self.pokemon = pokemon

    def __str__(self):
        return f"Ability: Name: {self.name}, ID: {self.id}" \
               f", Generation: {self.generation}, Effect: {self.effect}, " \
               f", Short Effect: {self.short_effect}, Pokemon: {self.pokemon}"
