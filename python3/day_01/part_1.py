import repackage
repackage.up()

from lib.tools import AdventInput


instructions = AdventInput.input_to_list(None, "input.txt")
result = 0

for instruction in instructions:
    first = None
    last = None
    for item in instruction:
        if item.isdigit():
            if first == None:
                first = item
            last = item
    result = result + int(f"{first}{last}")

print(result)
