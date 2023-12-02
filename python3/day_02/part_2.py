import repackage
repackage.up()

from lib.tools import AdventInput


games = AdventInput.input_to_list(None, "input.txt")
result = 0

for game in games:
    min = {
        "red": 0,
        "green": 0,
        "blue": 0
    }  
    game_id, cubes = game.split(": ")
    game_id = game_id.split(" ")[1]

    sets = cubes.split("; ")
    for set in sets:
        dice = set.split(", ")
        for die in dice:
            number, colour = die.split(" ")
            if int(number) > min[colour]:
                min[colour] = int(number)
    print(min)
    result = result + (min["red"] * min["green"] * min["blue"])
print(result)
