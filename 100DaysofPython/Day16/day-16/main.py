from turtle import Turtle, Screen
from prettytable import PrettyTable

pokemon = {"Pikchu": "Electric", "Squirtle": "Water", "Charmander": "Fire"}

x = PrettyTable()
x.add_column("Pokemon Name", list(pokemon.keys()))
x.add_column("Type", list(pokemon.values()))
x.align = "l"

print(x)
