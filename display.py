def display_maze_with_path(maze, path):
    maze_copy = [row[:] for row in maze]  # Создаём копию, чтобы не менять оригинал

    for x, y in path:
        if maze_copy[x][y] == ' ':
            maze_copy[x][y] = '.'  # Помечаем путь

    for row in maze_copy:
        print(''.join(row))