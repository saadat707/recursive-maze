from maze_generator import generate_maze, print_maze
from pathfinder import dfs

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
        mark_path(maze, path)
        print("\nЛабиринт с отмеченным путём:")
        print_maze(maze)
    else:
        print("\nПуть не найден.")

if name == "__main__":
    main()