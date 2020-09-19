#!/usr/bin/env python
# coding: utf-8

# In[1]:


T = int(input()) #케이스 수
count=1 #나중에 #1, #2 출력 쉽게


# In[ ]:


for i in range(T): 
    case=int(input()) #이름 개수
    name_list=[]
    for j in range(case): 
        name=str(input()) #이름 문자열로 불러오기
        name_list.append(name) #이름 리스트 생성
    name_set=list(set(name_list)) #중복 없앨려고 set 사용
    name_dict=[]
    for name in name_set: #이름, 이름 길이 저장해주려고 dict 사용
        name_dict.append([name,len(name)])
    name_dict=sorted(name_dict,key=lambda x:(x[1],x[0]))#이름길이로 먼저, 그 다음 이름 사전순
    print('#{}'.format(count)) # #1, #2 출력
    for k in range(len(name_dict)):
        print(name_dict[k][0]) #각자 이름만 출력
    count+=1

