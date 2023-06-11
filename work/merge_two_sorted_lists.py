# 2つのリストをマージして小さい順にソートする

# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]

# Input: list1 = [], list2 = []
# Output: []

# Input: list1 = [], list2 = [0]
# Output: [0]


list1 = [2, 5, 1, 0]
list2 = [3, 8, 0, -1]


def merge_list(list_one: list, list_two: list) -> list:
    list_one.extend(list_two)
    result = sorted(list_one)
    print(result)
    return result


merge_list(list1, list2)
