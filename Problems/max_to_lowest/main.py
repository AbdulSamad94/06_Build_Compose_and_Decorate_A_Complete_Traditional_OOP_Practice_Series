from typing import List


def max_to_lowest(nums: List[int]):
    arr = []

    for i in range(len(nums)):
        max_value = nums[0]
        for j in nums:
            if j > max_value:
                max_value = j
        arr.append(max_value)
        nums.remove(max_value)
    return arr


values = max_to_lowest([1, 58, 59, 13, 79])
print(values)
