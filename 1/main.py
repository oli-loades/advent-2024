INPUT_FILENAME = "input.txt"

def get_input(): 
    with open(INPUT_FILENAME, "r", encoding="utf-8") as f:
        left, right = [], []
        for line in f:
            values = line.split()
            left.append(int(values[0]))
            right.append(int(values[1]))
        return (sorted(left), sorted(right))

def find_diff(first_list, second_list):
    diff_sum = 0
    for i, x in enumerate(first_list):
        diff_sum += abs(x - second_list[i])
    return diff_sum

def find_sim(first_list, second_list):
    sim_sum = 0
    for x in first_list:
        sim_sum += second_list.count(x)*x
    return sim_sum

lists = get_input()

diff = find_diff(lists[0], lists[1])
print(diff)

sim = find_sim(lists[0], lists[1])
print(sim)
