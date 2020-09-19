#!/usr/bin/env python
# coding: utf-8

# K번째 수 찾기
# array , command[[i,j,k], [ ]]형태로 주어짐
# array에서 i~j번째 자르고 정렬 후 k 번째 수 찾기

# In[ ]:


def solution(array, commands):
    answer = []
    for command in commands: #command 하나씩 확인
        i=command[0]
        j=command[1]
        k=command[2]
        array_1=array[i-1:j] #i번째 index는 i-1
        array_2=sorted(array_1) #정렬
        answer.append(array_2[k-1]) #k번째 index는 k-1
    return answer

