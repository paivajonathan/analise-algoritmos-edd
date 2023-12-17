import random


def turn_into_c_array(dataset: list) -> str:
    print(f'MAX: {max(dataset)}, MIN: {min(dataset)}, LEN: {len(dataset)}')
    return dataset.__str__().replace('[', '{').replace(']', '}')


with open('data.c', 'w') as f:
    SMALL_DATA_SIZE = 100

    small_ordered_data = turn_into_c_array([i for i in range(1, SMALL_DATA_SIZE + 1)])
    small_reversed_data = turn_into_c_array([i for i in range(SMALL_DATA_SIZE, 0, -1)])
    small_unordered_data = turn_into_c_array(random.sample(range(1, SMALL_DATA_SIZE + 1), SMALL_DATA_SIZE))
    small_random_data = turn_into_c_array([random.randint(1, 1_000_000) for _ in range(1, SMALL_DATA_SIZE + 1)])

    f.write('const int SMALL_DATA_SIZE = ' + str(SMALL_DATA_SIZE) + ';\n\n')
    f.write(f'int small_ordered_data[] = {small_ordered_data};\n\n')
    f.write(f'int small_reversed_data[] = {small_reversed_data};\n\n')
    f.write(f'int small_unordered_data[] = {small_unordered_data};\n\n')
    f.write(f'int small_random_data[] = {small_random_data};\n\n\n')

    MEDIUM_DATA_SIZE = 1000

    medium_ordered_data = turn_into_c_array([i for i in range(1, MEDIUM_DATA_SIZE + 1)])
    medium_reversed_data = turn_into_c_array([i for i in range(MEDIUM_DATA_SIZE, 0, -1)])
    medium_unordered_data = turn_into_c_array(random.sample(range(1, MEDIUM_DATA_SIZE + 1), MEDIUM_DATA_SIZE))
    medium_random_data = turn_into_c_array([random.randint(1, 1_000_000) for _ in range(1, MEDIUM_DATA_SIZE + 1)])

    f.write('const int MEDIUM_DATA_SIZE = ' + str(MEDIUM_DATA_SIZE) + ';\n\n')
    f.write(f'int medium_ordered_data[] = {medium_ordered_data};\n\n')
    f.write(f'int medium_reversed_data[] = {medium_reversed_data};\n\n')
    f.write(f'int medium_unordered_data[] = {medium_unordered_data};\n\n')
    f.write(f'int medium_random_data[] = {medium_random_data};\n\n\n')

    LARGE_DATA_SIZE = 10000

    large_ordered_data = turn_into_c_array([i for i in range(1, LARGE_DATA_SIZE + 1)])
    large_reversed_data = turn_into_c_array([i for i in range(LARGE_DATA_SIZE, 0, -1)])
    large_unordered_data = turn_into_c_array(random.sample(range(1, LARGE_DATA_SIZE + 1), LARGE_DATA_SIZE))
    large_random_data = turn_into_c_array([random.randint(1, 1_000_000) for _ in range(1, LARGE_DATA_SIZE + 1)])

    f.write('const int LARGE_DATA_SIZE = ' + str(LARGE_DATA_SIZE) + ';\n\n')
    f.write(f'int large_ordered_data[] = {large_ordered_data};\n\n')
    f.write(f'int large_reversed_data[] = {large_reversed_data};\n\n')
    f.write(f'int large_unordered_data[] = {large_unordered_data};\n\n')
    f.write(f'int large_random_data[] = {large_random_data};\n\n\n')

    f.close()