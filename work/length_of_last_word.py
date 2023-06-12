# 最後のワードの文字数を判定

# Input: s = "Hello World"
# Output: 5

# Input: s = "   fly me   to   the moon  "
# Output: 4

# Input: s = "luffy is still joyboy"
# Output: 6


def last_word(s: str) -> int:
    data = s.split(" ")
    tmp = " ".join(data).split()
    print(len(tmp[-1]))
    return len(tmp.pop(-1))


last_word("   fly me   to   the moon  ")
