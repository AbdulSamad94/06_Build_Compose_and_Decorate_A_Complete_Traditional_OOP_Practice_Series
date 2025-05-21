from typing import List


def second_max(arr: List[int]):
    max_value = arr[0]
    second_max_value = arr[0]
    for i in arr:
        if i > max_value:
            max_value = i
            arr.remove(max_value)

    for i in arr:
        if i > second_max_value:
            second_max_value = i

    return second_max_value


output = second_max([4, 5, 2, 9, 4, 5, 8, 0, 4])
print(output)


# that is my solution after chatgpt now my solution is:


def second_max(arr: List[int]):
    max_value = float("-inf")
    second_max_value = float("-inf")

    for i in arr:
        if i > max_value:
            second_max_value = max_value
            max_value = i

        elif max_value > i > second_max_value:
            second_max_value = i

    return int(second_max_value)


print("done")
output = second_max([4, 5, 2, 9, 4, 5, 8, 0, 4])
print(output)
