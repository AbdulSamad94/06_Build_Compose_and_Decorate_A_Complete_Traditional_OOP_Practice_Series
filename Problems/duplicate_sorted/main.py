from typing import List


def find_duplicate_value(list: List):
    initial_arr = []
    duplicate_arr = []
    sorted_arr = []

    for i in list:
        if i in initial_arr:
            duplicate_arr.append(i)
        else:
            initial_arr.append(i)

    for i in range(len(duplicate_arr)):
        lowest_val = duplicate_arr[0]
        for j in duplicate_arr:
            if j <= lowest_val:
                lowest_val = j

        sorted_arr.append(lowest_val)
        duplicate_arr.remove(lowest_val)

    return sorted_arr


output = find_duplicate_value([1, 3, 1, 4, 5, 6, 3, 5, 4])
print(output)
