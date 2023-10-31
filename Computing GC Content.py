code = ""
score = 0
cur_code = ""
cur_str = " "
while True:
    s = input()
    if not s:
        if (cur_str.count('G') + cur_str.count('C')) / len(cur_str) > score:
            score = (cur_str.count('G') + cur_str.count('C')) / len(cur_str)
            code = cur_code
        break
    if s[0] == '>':
        if (cur_str.count('G') + cur_str.count('C')) / len(cur_str) > score:
            score = (cur_str.count('G') + cur_str.count('C')) / len(cur_str)
            code = cur_code
        cur_code = s[1:]
        cur_str = ""
    else:
        cur_str += s
print(code)
print(f'{score * 100:6f}')
