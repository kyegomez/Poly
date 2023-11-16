# Use Poly Morphism Anytime With This New Library!

Everything is mutable in python so just assign types normally. Its built into the language. No need to do anything!

## See it in action!

```
class Poly:
    attribute: str

class Mutable(Poly):
    def __init__(self):
        super().__init__()
        self.attribute = "Amazing!"
```

## Mutable variables!

```
abra: int =  1

kadabra: str = "alakazam"

abra = kadabra

print(abra)
```
stdout "alakazam"