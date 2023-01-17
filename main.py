from Stack import Stacks
class Maze:
    def __init__(self):
        pass

    def mountMaze(self):
        maze_data = open('mazze.txt', 'r')
        maze_stack = Stacks(100)
        
        for row in maze_data:
            wall = f'1{row}1'
            wall_array = []

            for character in wall:
                if not character == '\n':
                    wall_array.append(character)
            
            maze_stack.stackUp(wall_array)
        maze_data.close()

        maze = []
        wallUpAndDown = maze_stack.getColumnsLength()*['1']

        maze.insert(0, wallUpAndDown)
        for row in range(maze_stack.getRowLength()):
            maze.append(maze_stack.unStack())
        maze.append(wallUpAndDown)

        exit_coords = {
            'row': None,
            'column': None,
        }
        for row_number in range(len(maze)):
            find_exit = ''.join(maze[row_number]).find('e')
            if find_exit >= 0:
                exit_coords['column'] = find_exit
                exit_coords['row'] = row_number
                
            print(maze[row_number])
        maze[exit_coords['row']][exit_coords['column']] = 0
        print(exit_coords)

mazze = Maze()
mazze.mountMaze()