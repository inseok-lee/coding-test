def solution(array):
    answer = 0
    dic = {}
    
    # 딕셔너리에 넣기
    while len(array) != 0:
        x = array.pop()
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1
        
    
    sorted_dic = sorted(dic.items(), key=lambda x:x[1], reverse=True)
    
    # print(sorted_dic[0][0])
    
    if len(sorted_dic) == 1:
        answer = sorted_dic[0][0]
    else:
        if sorted_dic[0][1] != sorted_dic[1][1]:
            answer = sorted_dic[0][0]
        else:
            answer = -1
    
    return answer



# best
# def solution(array):
#     while len(array) != 0:
#         for i, a in enumerate(set(array)):
#             array.remove(a)
#         if i == 0: return a
#     return -1

# second
# def solution(array):
#     keys = set(array)
#     dict = {}
#     max_freq = []
#     for key in keys:
#         dict[key] = array.count(key)
#     for key in keys:
#         if dict[key] == max(dict.values()):
#             max_freq.append(key)
#     if len(max_freq) > 1:
#         answer = -1
#     else:
#         answer = max_freq[0]
#     return answer

# third
# from collections import Counter

# def solution(array):
#     a = Counter(array).most_common(2)
#     if len(a) == 1:
#         return a[0][0]
#     if a[0][1] == a[1][1]:
#         return -1
#     return a[0][0]