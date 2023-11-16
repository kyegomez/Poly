

class Poly:
    attribute: str

class Mutable(Poly):
    def __init__(self):
        super().__init__()
        self.attribute = "Amazing!"

Mutable().attribute
        
abra: int =  1

kadabra: str = "alakazam"

abra = kadabra

print(abra)