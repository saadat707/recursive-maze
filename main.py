from maze_generator import generate_maze, print_maze
from pathfinder import dfs

def main():
    width, height = 10, 10  # Размер лабиринта
    maze, start, end = generate_maze(width, height)
    
    print("Сгенерированный лабиринт:")
    print_maze(maze)
    
    path = []
    if dfs(maze, start[0], start[1], end, path):
        print("\nПуть найден:")
        print(path)

        # Отметить путь в лабиринте точками
for x, y in path:
    if (x, y) != start and (x, y) != end:  # Убедимся, что старт и финиш не заменяются
        maze[y][x] = '.'  # Помечаем путь точками

# Выводим лабиринт с помеченным путём
print("\nЛабиринт с найденным путём:")
print_maze(maze)
    else:
        print("\nПуть не найден.")

if name == "__main__":
    main()