from bisect import bisect_left, bisect_right

n = int(input())
card_sorted = sorted(list(map(int, input().split())))
m = int(input())
int_list = list(map(int, input().split()))

def count_by_range(array, integer):
    left_index = bisect_left(array, integer) #이진탐색으로 왼쪽 Index 찾기
    right_index = bisect_right(array, integer)
    return right_index - left_index

for item in int_list:
    if count_by_range(card_sorted, item): # 카운트가 1 이상이면 1 출력
        print(1, end = " ")
    else:
        print(0, end = " ")