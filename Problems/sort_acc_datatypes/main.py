from typing import List


def arr_num_to_str(arr: List):
    num_arr = []
    str_arr = []

    for i in range(len(arr)):
        for j in arr:
            if type(j) == int:
                num_arr.append(j)
                arr.remove(j)
            elif type(j) == str:
                str_arr.append(j)
                arr.remove(j)
    final_arr = num_arr + str_arr
    return final_arr


output = arr_num_to_str(["samad", 1, 70, "hello world", "messi better", 10])
print(output)
