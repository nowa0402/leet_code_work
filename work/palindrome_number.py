# 与えられた引数xが回文だったらTrueを返却する

# Example 1:
# Input: x = 121
# Output: true

# Example 2:
# Input: x = -121
# Output: false


x = 121

y = 124


def is_palindrome(target: int) -> bool:
    tmp = str(target)
    # [start: end: step] [::-1]で逆から取り出す
    # stringの場合逆から1ステップずつ取り出してくれる
    reverse_list = tmp[::-1]
    return tmp == reverse_list


print(is_palindrome(x))
print(is_palindrome(y))
