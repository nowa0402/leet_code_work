#  '(', ')', '{', '}', '[' ']'の組み合わせ判定
# MEMO: スタックで考える


# Input: s = "()"
# Output: true

# Input: s = "()[]{}"
# Output: true

# Input: s = "(]"
# Output: false


def is_valid(s: str) -> bool:
    data = list(s[::])
    if len(data) % 2 != 0:
        return False

    tmp_list = []
    for val in data:
        if val in ["(", "{", "["]:
            tmp_list.append(val)
            continue

        if tmp_list == []:
            return False

        tmp = f"{tmp_list.pop(-1)}{val}"
        if tmp not in ["{}", "()", "[]"]:
            return False

    return True if tmp_list == [] else False


print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
print(is_valid("{[]}"))
print(is_valid("([)]"))
print(is_valid("(("))
