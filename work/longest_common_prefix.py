# 最も長い接頭辞文字列を見つける

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


def find_common(strs: list[str]) -> None:
    result = ""
    if strs[0] == "":
        print(result)
        return

    splist_first = list(strs.pop(0))
    first_str = splist_first.pop(0)

    if len(strs) != len([s for s in strs if s.startswith(first_str)]):
        print(result)
        return

    result = first_str
    for val in splist_first:
        tmp = result + val
        if len(strs) != len([s for s in strs if s.startswith(tmp)]):
            print(result)
            return
        result = tmp


find_common(["reflower", "flow", "flight"])
find_common(["c", "acc", "ccc"])
find_common(["flower", "flow", "flight"])
find_common(["dog", "racecar", "car"])
