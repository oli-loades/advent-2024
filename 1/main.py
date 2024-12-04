INPUT_FILENAME = "input.txt"

def get_input():
    left, right = [], []
    f = open(INPUT_FILENAME, "r")
    for line in f:
        values = line.split()
        left.append(int(values[0]))
        right.append(int(values[1]))

    return (sorted(left), sorted(right))

def find_diff(first_list, second_list):
    diff_sum = 0
    for x in range(len(first_list)):
        diff_sum += abs(first_list[x] - second_list[x])
    return diff_sum

input = get_input()
diff = find_diff(input[0], input[1])
print(diff)