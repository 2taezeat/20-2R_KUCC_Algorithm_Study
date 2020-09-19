# Array = list(map(int, input().split()))
# Commands = list(map(int, input().split()))
# Answer = []
#
# for i in range(Commands[0]-1, Commands[1]):
#     Answer.append(Array[i])
#
# Answer.sort()
#
# print(Answer[Commands[2]-1])
# 대략적인 스케

def solution(array, commands):
    answer = []

    for command in commands:
        List = array[command[0]-1: command[1]]
        # 지정한 범위내의 리스트 생성.
        List.sort()
        answer.append(List[command[2]-1])
        # answer 리스트에 추가.
    return answer

solution([1, 5, 2, 6, 3, 7, 4],	[[2, 5, 3], [4, 4, 1], [1, 7, 3]])