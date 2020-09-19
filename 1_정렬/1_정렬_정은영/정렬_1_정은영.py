t = int(input())
for i in range(t):
    n = int(input())
    dic = dict()
    for _ in range(n): #n 길이만큼 인풋 받기
        name = input()
        dic[name] = len(name) #딕셔너리에 이름과 이름길이 저장
    print('#', end = '')
    print(i + 1)
    dic_sorted = sorted(sorted(dic.items(), key = lambda x: x[0]), key = lambda x: x[1]) #딕셔너리 키로 우선 정렬 후 벨류로 정렬
    for item in dic_sorted: #정렬된 리스트의 첫번째 값만 출력
        print(item[0])