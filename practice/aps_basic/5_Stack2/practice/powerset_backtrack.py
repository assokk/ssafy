numbers = [1, 2, 3]
pick_idx = [0, 0, 0]  # [0] * len(numbers)

def subset(count):

    # 다 골랐을 때
    if count == len(numbers):
        for i in range(len(numbers)):
            if pick_idx[i]:
                print(numbers[i], end=" ")
        print()
        return
    
    # 아직 다 안 골랐을 때
    pick_idx[count] = 0
    subset(count+1)
    pick_idx[count] = 1
    subset(count+1)



# 조합 코드와 비교
# 시간복잡도는 비슷하지만 노드 수가 좀 줄어듦.
# (idx : 탐색 범위의 첫 인덱스)
def comb(count, idx):
    print(pick_numbers)
    if count == len(numbers):
        return
    
    for i in range(idx, len(numbers)):
        pick_numbers.append(numbers[i])
        comb(count+1, i+1)
        pick_numbers.pop()
        
comb(0, 0)