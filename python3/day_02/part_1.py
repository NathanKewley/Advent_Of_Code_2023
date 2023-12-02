import repackage
repackage.up()

from lib.tools import AdventInput


games = AdventInput.input_to_list(None, "input.txt")
result = 0

max = {
    "red": 12,
    "green": 13,
    "blue": 14
}

for game in games:
    game_valid = True
    game_id, cubes = game.split(": ")
    game_id = game_id.split(" ")[1]

    sets = cubes.split("; ")
    for set in sets:
        dice = set.split(", ")
        for die in dice:
            number, colour = die.split(" ")
            if int(number) > max[colour]:
                game_valid = False

    if game_valid:
        result = result + int(game_id)
print(result)
