T = int(input())

for tc in range(1, T+1):
    N = int(input())
    before_row = []
    
    print(f'#{tc}')
    # i : 지금 몇 번째 줄인지
    for i in range(1, N+1):
        current_row = []
        for j in range(i):
            if j == 0 or j == i-1:
                current_row.append(1)
                print(1, end = ' ')
            else:
                current_row.append(before_row[j] + before_row[j-1])
                print(before_row[j] + before_row[j-1], end = ' ')
        print()
        before_row = current_row
