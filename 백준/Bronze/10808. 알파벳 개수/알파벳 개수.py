s = input()
s_cnt = [0] * 26

for ch in s:
    i = ord(ch) - ord('a')
    s_cnt[i] += 1

print(*s_cnt)