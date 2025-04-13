import random

def generate_maze(width, height):
    maze = [['#' for _ in range(width)] for _ in range(height)]

    # Начальная и конечная точки
    start = (0, 1)
    end = (height - 1, width - 2)

    # Сделаем начальную и конечную точку проходимыми
    maze[start[0]][start[1]] = ' '
    maze[end[0]][end[1]] = ' '

    def carve_path(x, y):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # направления (вверх, вниз, вправо, влево)
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 < nx < height - 1 and 0 < ny < width - 1 and maze[nx][ny] == '#':
                maze[nx][ny] = ' '
                carve_path(nx, ny)

    carve_path(start[0], start[1])

    return maze, start, end

def print_maze(maze):
    for row in maze:
        print(''.join(row))