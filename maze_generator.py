import random

def generate_maze(width, height):
    maze = [['#' for _ in range(width)] for _ in range(height)]
    
    for y in range(1, height - 1, 2):
        for x in range(1, width - 1, 2):
            maze[y][x] = ' '  # Делает клетки пустыми (проходимыми)
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = y + dy, x + dx
                if 0 < ny < height and 0 < nx < width:
                    maze[ny][nx] = ' '  # Разрешаем проходы вокруг этих клеток
    
    start = (1, 1)  # Стартовая точка
    end = (height - 2, width - 2)  # Конечная точка
    
    maze[start[0]][start[1]] = 'S'  # Старт
    maze[end[0]][end[1]] = 'E'  # Конец
    
    return maze, start, end

def print_maze(maze):
    for row in maze:
        print("".join(row))