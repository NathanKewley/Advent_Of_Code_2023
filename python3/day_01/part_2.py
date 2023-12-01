import repackage
repackage.up()

from lib.tools import AdventInput


instructions = AdventInput.input_to_list(None, "input.txt")
result = 0

replacements = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}
replacement_list = ["one","two","three","four","five","six","seven","eight","nine"]

for instruction in instructions:
    # set the numbers to digits but cant clear the word out as words overlap
    for replacement in replacement_list:
        instruction = instruction.replace(replacement, f"{replacement[0]}{replacements[replacement]}{replacement}")

    first = None
    last = None
    for item in instruction:
        if item.isdigit():
            if first == None:
                first = item
            last = item
    result = result + int(f"{first}{last}")

print(result)
