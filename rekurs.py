#1

# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)
#
# print(factorial(5))
# print(factorial(6))

#2

# def remove_vowels(n):
#     glasn = "eyuioaEYUIOA"
#     if not n:
#         return ""
#     new_slovo = n[0]
#     if new_slovo in glasn:
#         return remove_vowels(n[1:])
#     else:
#         return new_slovo + remove_vowels(n[1:])
#
# print(remove_vowels('apple'))
# print(remove_vowels('banana'))


#3
#
# def pascal(n):
#     if n == 1:
#         return [1]
#
#     a = pascal(n - 1)
#     str = [1]
#
#     for i in range(len(a) - 1):
#         str.append(a[i] + a[i + 1])
#
#     str.append(1)
#     return str
#
# print(pascal(6))

# лабиринт
def solve(maze, x=None, y=None):
    if x == None and y == None:
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == 'S':
                    return solve([list(row) for row in maze], i, j)

    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]):
        return False
    if maze[x][y] == '#':
        return False
    if maze[x][y] == 'X':
        return []

    temp = maze[x][y]
    maze[x][y] = '#'
    p = solve(maze, x - 1, y)
    if p != False:
        return ["вверх"] + p
    p = solve(maze, x + 1, y)
    if p != False:
        return ["вниз"] + p
    p = solve(maze, x, y - 1)
    if p != False:
        return ["влево"] + p
    p = solve(maze, x, y + 1)
    if p != False:
        return ["вправо"] + p

    maze[x][y] = temp
    return False

maze = [
    'S----',
    '##---',
    '---##',
    '----X'
]

print(solve(maze))
