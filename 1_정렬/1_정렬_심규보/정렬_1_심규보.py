TestCase = int(input())

for i in range(TestCase):
    List = []
    NumberInput = int(input())

    for j in range(NumberInput):
        NameInput = input()
        List.append(NameInput)

    SetList = set(List)
    NewList = list(SetList)

    print("#", i+1, sep='')
    for i in range(len(NewList)):
        print(NewList[i])

#오류 확인중.