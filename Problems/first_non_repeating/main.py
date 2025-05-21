from collections import Counter
from typing import List


def first_non_repeating(lst: List[int]) -> int:
    count = Counter(lst)

    for i in lst:
        if count[i] == 1:
            return i

    return None


output = first_non_repeating([4, 5, 1, 2, 0, 4, 1, 0])
print(output)
