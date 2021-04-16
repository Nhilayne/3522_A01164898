class PokedexObject:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f"PokedexObject: Name: {self.name}\nID: {self.id}"


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
        return f"\n\nMove: {self.name}\nID: {self.id}" \
               f"\nGeneration: {self.generation}\nAccuracy: {self.accuracy}" \
               f"\nPP: {self.pp}\nPower: {self.power}" \
               f"\nType: {self.type}\nDamage: {self.dmg}\nEffect: {self.effect}"


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
        stat_list = ""
        ability_list = ""
        moves_list = ""
        for stat in self.stats:
            stat_list += "-"
            stat_list += (str(stat))
            stat_list += "\n"
        for ability in self.abilities:
            ability_list += "-"
            ability_list += (str(ability))
            ability_list += "\n"
        for move in self.moves:
            moves_list += "-"
            moves_list += (str(move))
            moves_list += "\n"
        return f"\n***************\nPokemon: {self.name}\nID: {self.id}" \
               f"\nHeight: {self.height} decimetres\nWeight: {self.weight} hectograms" \
               f"\nStats: \n{stat_list}\nTypes: {self.types}" \
               f"\nAbilities: \n{ability_list}\nMoves: \n{moves_list}\n***************"


class Ability(PokedexObject):

    def __init__(self, name, id, generation, effect, shorteffect, pokemon):
        super(Ability, self).__init__(name, id)
        self.generation = generation
        self.effect = effect
        self.short_effect = shorteffect
        self.pokemon = pokemon

    def __str__(self):
        return f"\n\nAbility: {self.name}\nID: {self.id}" \
               f"\nGeneration: {self.generation}\nEffect: {self.effect}" \
               f"\nShort Effect: {self.short_effect}\nPokemon: {self.pokemon}"


class Stats(PokedexObject):
    def __init__(self, name, id, value,  battle):
        super(Stats, self).__init__(name, id)
        self.value = value
        self.is_battle_only = battle

    def __str__(self):
        return f"Stat: {self.name}, Value: {self.value}, ID: {self.id}, Battle Only: {self.is_battle_only}"
