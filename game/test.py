import itertools

def list_all_combinations():
    combinations = []

    # 3 different items
    for combo in itertools.combinations(range(5), 3):
        combination = [0] * 5
        for i in combo:
            combination[i] = 1
        combinations.append(combination)

    # 2 of one type and 1 of another type
    for i in range(5):
        for j in range(5):
            if i != j:
                combination = [0] * 5
                combination[i] = 2
                combination[j] = 1
                combinations.append(combination)

    # 3 of the same type
    for i in range(5):
        combination = [0] * 5
        combination[i] = 3
        combinations.append(combination)

    return combinations

# Generate and print all combinations
combinations = list_all_combinations()
for combination in combinations:
    print(combination)
print("Total number of combinations:", len(combinations))
