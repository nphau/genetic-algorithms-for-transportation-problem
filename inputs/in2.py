ITERATION_NUM = 500
MAX_POPULATION = 500
CROSSOVER_RATE = 0.5
MUTATION_RATE = 0.75

supplies = {
    'S1': 27,
    'S2': 28,
    'S3': 25,
    'S4': 20,
    'S5': 20,
    'S6': 20,
    'S7': 20
}

demands = {
    'D1': 20,
    'D2': 20,
    'D3': 20,
    'D4': 23,
    'D5': 26,
    'D6': 25,
    'D7': 26
}

cost = [
    [0, 21, 50, 62, 93, 77, 1000],
    [21, 0, 17, 54, 67, 1000, 48],
    [50, 17, 0, 60, 98, 67, 25],
    [62, 54, 60, 0, 27, 1000, 38],
    [93, 67, 98, 27, 0, 47, 42],
    [77, 1000, 67, 1000, 47, 0, 35],
    [1000, 48, 25, 38, 42, 35, 0]
]
