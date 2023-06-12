# 最初に出現したインデックスを返却
# 一致しない場合は-1

# 入力: haystack = "sadbutsad"、needle = "sad"
# 出力: 0

# 入力: haystack = "leetcode"、needle = "leeto"
# 出力: -1


def strStr(haystack: str, needle: str) -> int:
    print(haystack.find(needle))
    # 最初に見つかったインデックスを返却
    # 一致しなければ-1を返却する
    return haystack.find(needle)


strStr("sadbutsad", "sad")
strStr("leetcode", "leeto")
