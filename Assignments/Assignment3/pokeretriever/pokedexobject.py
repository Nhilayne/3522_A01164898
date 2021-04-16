class PokedexObject:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f"PokedexObject: Name: {self.name}, ID: {self.id}"
