def dfs(maze, x, y, end, path):
    if (x, y) == end:
        path.append((x, y))
        return True

    if x < 0 or y < 0 or x >= len(maze) or y >= len(maze[0]) or maze[x][y] == '#' or maze[x][y] == '.':
        return False

    maze[x][y] = '.'  # Метка для посещенной клетки
    path.append((x, y))

    if (dfs(maze, x + 1, y, end, path) or  # Вниз
        dfs(maze, x - 1, y, end, path) or  # Вверх
        dfs(maze, x, y + 1, end, path) or  # Вправо
        dfs(maze, x, y - 1, end, path)):   # Влево
        return True

    path.pop()  # Откат, если путь не найден
    return False