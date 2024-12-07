INPUT_FILENAME = "input.txt"

def get_input():
    with open(INPUT_FILENAME, "r", encoding="utf-8") as f:
        inputs = {}
        for line in f:
            splits = line.split(":")
            target, number = int(splits[0]), [int(x) for x in splits[1].split()]
            inputs[target] = number
        return inputs

def is_valid(target, numbers):
    if len(numbers) == 0:
        return target == 0
    return is_valid(target-numbers[-1], numbers[:-1]) or (target%numbers[-1] == 0 and is_valid(target//numbers[-1], numbers[:-1]))

def part_one():
    result = 0
    for k, v in data.items():
        if is_valid(k, v):
            result += k
    print(result)

data = get_input()
part_one()
