# 引数にnums targetを受け取る
# numsの各要素を計算し、targetに一致するインデックスを返却する

# 例1
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# 例2
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

nums = [2, 7, 11, 15]
target = 9

for i in range(len(nums)):
    # 自分の要素番号より後しか計算対象がいないのでi + 1で良い
    for j in range(i + 1, len(nums)):
        if (nums[i] + nums[j]) == target:
            print([i, j])
