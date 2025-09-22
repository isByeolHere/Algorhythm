def solution(array):
    answer = 0
    cnt = [0] * (max(array)+1)
    for i in array:
        cnt[i] += 1
    max_count = max(cnt)
    if cnt.count(max_count) > 1:     # 같은 횟수가 여러 개면 -1
        return -1
    else:
        return cnt.index(max_count)  # 최빈값