# from collections import Counter


# def count_num_letters(str: str):
#     arr = list(str)
#     count = Counter(arr)

#     return dict(count)


# output = count_num_letters("abdulsamad")
# print(output)


def count_num_letters(str: str):
    arr = list(str)
    count = {}
    seen = []
    sorted_dic = {}
    highest_to_lowest = []

    for i in arr:
        if i in seen:
            count[i] += 1

        else:
            seen.append(i)
            count[i] = 1

    keys = list(count.values())

    for i in range(len(keys)):
        max_val = keys[0]
        for j in keys:
            if j > max_val:
                max_val = j

        highest_to_lowest.append(max_val)
        keys.remove(max_val)

    used_keys = []

    for i in highest_to_lowest:
        for j in count:
            if count[j] == i and j not in used_keys:
                sorted_dic[j] = i
                used_keys.append(j)
                break

    return sorted_dic


output = count_num_letters(
    "you are going to be succesfull one day inshallah abdul samad "
)
print(output)


# LETSSSSSSSSS GOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
