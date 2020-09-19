def solution(array, commands):
    answer = []
    if len(str(commands[0])) == 1: #commands에 한가지 케이스만 들어갈 때 
        commands = [commands]
    for item in commands:
        array_list = []
        for j in range(item[0] - 1, item[1]):
            array_list.append(array[j])
        array_list.sort()
        answer.append(array_list[item[2] - 1])
    return answer