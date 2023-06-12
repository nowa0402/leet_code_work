# 要素の何番目に入るか

# Input: nums = [1,3,5,6], target = 5
# Output: 2

# Input: nums = [1,3,5,6], target = 2
# Output: 1

# Input: nums = [1,3,5,6], target = 7
# Output: 4


def sort_index(nums: list[int], target: int) -> int:
    nums.append(target)
    nums.sort()
    print(nums.index(target))
    return nums.index(target)


sort_index([1, 3, 5, 6], 7)
