def calculate_structure_sum(data_structure):
    total_sum = 0

    def inner_calculate(structure):
        nonlocal total_sum
        if isinstance(structure, int):
            total_sum += structure
        elif isinstance(structure, str):
            total_sum += len(structure)
        elif isinstance(structure, (list, tuple, set)):
            for item in structure:
                inner_calculate(item)
        elif isinstance(structure, dict):
            for key, value in structure.items():
                inner_calculate(key)
                inner_calculate(value)

    inner_calculate(data_structure)
    return total_sum


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)

print(result)
