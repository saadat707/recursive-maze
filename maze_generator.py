import random

def generate_maze(width, height):
    # Обеспечиваем нечётные размеры для корректной генерации (чередование стен и проходов)
    if width % 2 == 0:
        width += 1
    if height % 2 == 0:
        height += 1

    # Инициализируем лабиринт стенами
    maze = [['#' for _ in range(width)] for _ in range(height)]

    # Рекурсивная генерация пути
    def carve_passages(x, y):
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]  # Направления для срезания стен
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < height - 1 and 1 <= ny < width - 1 and maze[nx][ny] == '#':
                maze[nx - dx // 2][ny - dy // 2] = ' '  # промежуточная ячейка
                maze[nx][ny] = ' '
                carve_passages(nx, ny)

    # Стартовая точка — внутренняя (всегда нечётная)
    start_x, start_y = 1, 1
    maze[start_x][start_y] = ' '
    carve_passages(start_x, start_y)

    # Установка начальной и конечной точек
    maze[start_x][start_y] = 'S'
    end_x, end_y = height - 2, width - 2
    maze[end_x][end_y] = 'E'

    return maze, (start_x, start_y), (end_x, end_y)

# Функция для отображения лабиринта
def print_maze(maze):
    for row in maze:
        print(''.join(row))