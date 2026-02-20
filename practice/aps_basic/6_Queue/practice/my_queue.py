n = 3
que = [0] * n
front = rear = -1

# enqueue()
rear += 1
que[rear] = 1   # enqueue(1)
rear += 1
que[rear] = 2   # enqueue(2)
rear += 1
que[rear] = 3   # enqueue(3)

while front != rear:
    front += 1
    tmp = que[front]
    print(tmp)


q = []
q.append(1)
q.append(2)
print(q.pop(0))
print(q.pop(0))
