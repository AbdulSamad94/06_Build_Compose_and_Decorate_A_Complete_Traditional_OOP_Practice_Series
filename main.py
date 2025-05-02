from typing import List
import random


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]


# output = Solution()
# return_value = output.twoSum([2, 7, 11, 15], 9)
# print(return_value)


# create a function that will take an array and return the max value to the lowest value


# def max_to_lowest(nums: List[int]):
#     arr = []

#     for i in range(len(nums)):
#         max_value = nums[0]
#         for j in nums:
#             if j > max_value:
#                 max_value = j
#         arr.append(max_value)
#         nums.remove(max_value)
#     return arr


# values = max_to_lowest([1, 58, 59, 13, 79])
# print(values)


# create a function that will take the max number from the list and then the lowest then the max then the lowest


# def max_to_lowest(nums: List[int]):
#     arr = []

#     for i in range(len(nums)):
#         max_value = nums[0]
#         for j in nums:
#             if i % 2 == 0:
#                 if j > max_value:
#                     max_value = j
#             else:
#                 if j < max_value:
#                     max_value = j
#         arr.append(max_value)
#         nums.remove(max_value)
#     return arr


# values = max_to_lowest([1, 58, 59, 13, 79, 101])
# print(values)


# create a function that will take an array and will sort according to the datatype like first all the numbers then all the strings


# def arr_num_to_str(arr: List):
#     num_arr = []
#     str_arr = []

#     for i in range(len(arr)):
#         for j in arr:
#             if type(j) == int:
#                 num_arr.append(j)
#                 arr.remove(j)
#             elif type(j) == str:
#                 str_arr.append(j)
#                 arr.remove(j)
#     final_arr = num_arr + str_arr
#     return final_arr

# output = arr_num_to_str(["samad", 1, 70, "hello world", "messi better", 10])
# print(output)


# find the dupplicate value from the arr


# def duplicate(arr: List[int]):
#     dupli_arr = set()
#     seen = set()
#     for i in arr:
#         if i in seen:
#             dupli_arr.add(i)
#         else:
#             seen.add(i)

#     return list(dupli_arr)


# output = duplicate([4, 5, 2, 9, 4, 5, 8, 0, 4])
# print(output)

# find the second largest element in the arr


# def second_max(arr: List[int]):
#     max_value = arr[0]
#     second_max_value = arr[0]
#     for i in arr:
#         if i > max_value:
#             max_value = i
#             arr.remove(max_value)

#     for i in arr:
#         if i > second_max_value:
#             second_max_value = i

#     return second_max_value


# output = second_max([4, 5, 2, 9, 4, 5, 8, 0, 4])
# print(output)


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
