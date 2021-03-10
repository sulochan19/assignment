# 9. Write a binary search function. It should take a sorted sequence and
# the item it is looking for. It should return the index of the item if found.
# It should return -1 if the item is not found.
import math


def binary_search(sorted_sequence,item):
    low=0
    high=len(sorted_sequence)-1
    mid_value=(0+(0+high)/2)
    if item==sorted_sequence[mid_value]:
        return sorted_sequence.index(mid_value)
    elif item > mid_value:
        low=mid_value+1
        mid_value = (0 + (0 + high) / 2)

    elif item <mid_value:
        return binary_search(sorted_sequence[0:mid_value],item)
    else:
        return -1


value_list=[x for x in range(1,5)]
value_list.sort(reverse=True)

print(binary_search(value_list,9))
