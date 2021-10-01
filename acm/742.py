import sys

sys.stdin, sys.stdout = open('input.txt', 'r'), open('output.txt', 'w')

n, m, s = map(int, input().split())
maze = [[char for char in list(input())] for _ in range(n)]

directions = ['right', 'down', 'left', 'up']
current_direction = directions[0]
i, j = 0, 0

while s != 0:

    if current_direction == directions[0]:
        if j + 1 < m and maze[i][j + 1] == '.':
            i, j = i, j + 1
            s -= 1
        else:
            current_direction = directions[1]
        continue

    if current_direction == directions[1]:
        if i + 1 < n and maze[i + 1][j] == '.':
            i, j = i + 1, j
            s -= 1
        else:
            current_direction = directions[2]
        continue

    if current_direction == directions[2]:
        if j - 1 >= 0 and maze[i][j - 1] == '.':
            i, j = i, j - 1
            s -= 1
        else:
            current_direction = directions[3]
        continue

    if current_direction == directions[3]:
        if i - 1 >= 0 and maze[i - 1][j] == '.':
            i, j = i - 1, j
            s -= 1
        else:
            current_direction = directions[0]
        continue

print(i + 1, j + 1)
