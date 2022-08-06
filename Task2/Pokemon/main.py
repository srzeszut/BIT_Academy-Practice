from pokemon import Pokemon
from Electric.electric import *
from Fire.fire import *
from Water.water import *
from Grass.grass import *

print(Pokemon.origin)
print(Water.origin)
print(Fire.origin)
print(Grass.origin)
print(Electric.origin)
print(Pikachu.origin)

pokemon_A = Pikachu()
pokemon_B = Charmander()

Pokemon.Fight(pokemon_A, pokemon_B)

# print(pokemon_A)
# print(pokemon_B)
