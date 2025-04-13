def dfs(maze, x, y, end, path):
    # Если мы вышли за пределы лабиринта или уперлись в стену
    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or maze[x][y] == '#' or (x, y) in path:
        return False

    # Добавляем текущую позицию в путь
    path.append((x, y))

    # Если мы достигли конечной точки
    if (x, y) == end:
        return True

    # Рекурсивно проверяем соседей (вверх, вниз, влево, вправо)
    if (dfs(maze, x + 1, y, end, path) or  # вниз
        dfs(maze, x - 1, y, end, path) or  # вверх
        dfs(maze, x, y + 1, end, path) or  # вправо
        dfs(maze, x, y - 1, end, path)):   # влево
        return True

    # Если нет пути, удаляем текущую позицию из пути
    path.pop()
    return False