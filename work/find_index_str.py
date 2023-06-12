# 最初に出現したインデックスを返却
# 一致しない場合は-1

# 入力: haystack = "sadbutsad"、needle = "sad"
# 出力: 0

# 入力: haystack = "leetcode"、needle = "leeto"
# 出力: -1


def strStr(haystack: str, needle: str) -> int:
    if needle in haystack:
        return haystack.index(needle)
    return -1


print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "leeto"))
