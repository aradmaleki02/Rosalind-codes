def choose_kth_char(current_str, k, alphabet):
    if k == 0:
        print(current_str)
        return
    for i in range(len(alphabet)):
        choose_kth_char(current_str + alphabet[i], k - 1, alphabet)
    return


alphabet = sorted(input().split())
n = int(input())
choose_kth_char("", n, alphabet)
