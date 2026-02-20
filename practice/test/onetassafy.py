import math

while True:

    balls = [
        [30, 30],
        [-1, -1],
        [-1, -1],
        [15, 30],
        [-1, -1],
        [-1, -1],
    ]

    whiteBall_y = balls[0][0]   # whiteBall_x
    whiteBall_x = balls[0][1]   # whiteBall_y

    for i in range(1, 6):
        if balls[i][0] >= 0:
            targetBall_y = balls[i][0]
            targetBall_x = balls[i][1]
            break
    
    
    math.atan2(targetBall_y - whiteBall_y, targetBall_x - whiteBall_x)  # 라디안
    angle = math.degrees(radian)
    power = 100
    print(angle)