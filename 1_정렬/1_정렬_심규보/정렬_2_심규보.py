# m = int(input())
# SGCard = list(map(int, input().split()))
# n = int(input())
# ExampleCard = list(map(int, input().split()))
# OutputList = []
#
# for i in range(n):
#     ListCount = SGCard.count(ExampleCard[i])
#     OutputList.append(ListCount)
#
# print(*OutputList)

#시간초과

n = input()
A = set(map(int, input().split()))
m = input()
B = list(map(int, input().split()))
for i in B:
    if i in A:
        print(1, end=' ')
    else:
        print(0, end=' ')
#리스트에 있으면 1로 변경, 없으면 0으로 변