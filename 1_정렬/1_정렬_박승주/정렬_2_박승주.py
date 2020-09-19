#!/usr/bin/env python
# coding: utf-8

# input이 가지고 있는 카드개수 + 카드 숫자들
#         비교할 숫자 개수 + 숫자들

# 비교할 숫자가 가지고 있는 카드에 있으면 1 없으면 0 으로 출력
# ex) 0 1 0 1 1

# In[1]:


card_num=int(input()) # 가지고 있는 카드 개수
card_list=set(map(int, input().split())) # 카드 숫자들
m=int(input()) # 비교할 숫자 개수
m_list=list(map(int, input().split())) # 비교할 숫자들


# In[2]:


ans_list=[0 for i in range(m)] # 0xm 0리스트 만들기
for i in range(m):
    if m_list[i] in card_list:
        ans_list[i]=1 #존재한다면 1
for i in range(m):
    print(ans_list[i], end=' ') #리스트 요소들 프린트 공백으로 나눠서


# In[ ]:




