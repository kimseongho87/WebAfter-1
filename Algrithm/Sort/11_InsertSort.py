score=[['선미', 88], ['초아', 99], ['화사', 71], ['영탁', 78], ['영웅', 67], ['민호', 92]]
print("정렬 전 %s"%score)

idx=len(score)
for end in range(1, idx):
    for cur in range(end, 0, -1):
        if score[cur-1][1] > score[cur][1]:
            score[cur-1], score[cur]=score[cur], score[cur-1]
print("정렬 전 %s"%score)

for i in range(idx//2):
    # print(i)                 # 0  1 2
    # print(len(score)-1-i)   # 5 4 3
    print(score[i][0], ":", score[len(score)-1-i][0])
