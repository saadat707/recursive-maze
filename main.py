from maze_generator import generate_maze, print_maze

def dfs(maze, x, y, end, path):
    if (x, y) == end:
        path.append((x, y))
        return True

    if maze[x][y] == '#' or maze[x][y] == '.':
        return False

    maze[x][y] = '.'  # Помечаем как посещённую

    path.append((x, y))

    # Направления для поиска пути: вниз, вверх, вправо, влево
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]):
            if dfs(maze, nx, ny, end, path):
                return True

    path.pop()  # Возврат (обратный отсчёт)
    return False


def mark_path(maze, path):
    for x, y in path:
        if maze[x][y] == ' ':
            maze[x][y] = '.'


def main():
    while True:
        try:
            width = int(input("Введите ширину лабиринта (не менее 5): "))
            height = int(input("Введите высоту лабиринта (не менее 5): "))
            if width >= 5 and height >= 5:
                break
            else:
                print("Ошибка: ширина и высота должны быть не менее 5.")
        except ValueError:
            print("Ошибка: введите целые числа.")

    maze, start, end = generate_maze(width, height)
    
    print("\nСгенерированный лабиринт:")
    print_maze(maze)
    
    path = []
    if dfs(maze, start[0], start[1], end, path):
        print("\nПуть найден.")
        path_without_start = [pos for pos in path if pos != start]
        mark_path(maze, path_without_start)
        print("\nЛабиринт с отмеченным путём:")
        print_maze(maze)
    else:
        print("\nПуть не найден.")


if __name__ == "__main__":
    main()