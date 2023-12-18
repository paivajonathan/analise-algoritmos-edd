import random


SMALL_DATA_SIZE = 100
MEDIUM_DATA_SIZE = 1000
LARGE_DATA_SIZE = 10000


def turn_into_c_array(dataset: list) -> str:
    dataset_as_str: str = str(dataset)
    c_array: str = dataset_as_str.replace('[', '{').replace(']', '}')
    return c_array


with open('data.h', 'w') as f:
    f.write(f'extern int small_ordered_data[{SMALL_DATA_SIZE}];\n')
    f.write(f'extern int small_unordered_data[{SMALL_DATA_SIZE}];\n')
    f.write(f'extern int small_random_data[{SMALL_DATA_SIZE}];\n\n')

    f.write(f'extern int medium_ordered_data[{MEDIUM_DATA_SIZE}];\n')
    f.write(f'extern int medium_unordered_data[{MEDIUM_DATA_SIZE}];\n')
    f.write(f'extern int medium_random_data[{MEDIUM_DATA_SIZE}];\n\n')

    f.write(f'extern int large_ordered_data[{LARGE_DATA_SIZE}];\n')
    f.write(f'extern int large_unordered_data[{LARGE_DATA_SIZE}];\n')
    f.write(f'extern int large_random_data[{LARGE_DATA_SIZE}];\n')

    f.close()


with open('data.c', 'w') as f:
    small_ordered_data = turn_into_c_array([i for i in range(1, SMALL_DATA_SIZE + 1)])
    small_unordered_data = turn_into_c_array([i for i in range(SMALL_DATA_SIZE, 0, -1)])
    small_random_data = turn_into_c_array(random.sample(range(1, SMALL_DATA_SIZE + 1), SMALL_DATA_SIZE))

    f.write(f'int small_ordered_data[{SMALL_DATA_SIZE}] = {small_ordered_data};\n\n')
    f.write(f'int small_unordered_data[{SMALL_DATA_SIZE}] = {small_unordered_data};\n\n')
    f.write(f'int small_random_data[{SMALL_DATA_SIZE}] = {small_random_data};\n\n\n')

    medium_ordered_data = turn_into_c_array([i for i in range(1, MEDIUM_DATA_SIZE + 1)])
    medium_unordered_data = turn_into_c_array([i for i in range(MEDIUM_DATA_SIZE, 0, -1)])
    medium_random_data = turn_into_c_array(random.sample(range(1, MEDIUM_DATA_SIZE + 1), MEDIUM_DATA_SIZE))

    f.write(f'int medium_ordered_data[{MEDIUM_DATA_SIZE}] = {medium_ordered_data};\n\n')
    f.write(f'int medium_unordered_data[{MEDIUM_DATA_SIZE}] = {medium_unordered_data};\n\n')
    f.write(f'int medium_random_data[{MEDIUM_DATA_SIZE}] = {medium_random_data};\n\n\n')

    large_ordered_data = turn_into_c_array([i for i in range(1, LARGE_DATA_SIZE + 1)])
    large_unordered_data = turn_into_c_array([i for i in range(LARGE_DATA_SIZE, 0, -1)])
    large_random_data = turn_into_c_array(random.sample(range(1, LARGE_DATA_SIZE + 1), LARGE_DATA_SIZE))

    f.write(f'int large_ordered_data[{LARGE_DATA_SIZE}] = {large_ordered_data};\n\n')
    f.write(f'int large_unordered_data[{LARGE_DATA_SIZE}] = {large_unordered_data};\n\n')
    f.write(f'int large_random_data[{LARGE_DATA_SIZE}] = {large_random_data};\n')

    f.close()
