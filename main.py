from Stack import Stacks
class Maze:
    def __init__(self):
        self.maze = None
        self.exit_coords = {
            'column': None,
            'row': None,
        }
        self.mouse_coords = {
            'column': None,
            'row': None,
        }

    def showMaze(self):
        for row_number in range(len(self.maze)):
            print(self.maze[row_number])

    def mountMaze(self):
        maze_data = open('maze.txt', 'r')
        maze_stack = Stacks(100)
        
        for row in maze_data:
            wall = f'1{row}1'
            wall_array = []

            for character in wall:
                if not character == '\n':
                    wall_array.append(character)
            
            maze_stack.stackUp(wall_array)
        maze_data.close()

        self.maze = []
        wallUpAndDown1 = maze_stack.getColumnsLength()*['1']
        wallUpAndDown2 = maze_stack.getColumnsLength()*['1']

        for row in range(maze_stack.getRowLength()):
            self.maze.insert(0,maze_stack.unStack())
        self.maze.insert(0, wallUpAndDown1)
        self.maze.append(wallUpAndDown2)

        for row_number in range(len(self.maze)):
            find_exit = ''.join(self.maze[row_number]).find('e')
            if find_exit >= 0:
                self.exit_coords['column'] = find_exit
                self.exit_coords['row'] = row_number
                
        self.maze[self.exit_coords['row']][self.exit_coords['column']] = '0'
        
        if self.exit_coords['row'] == 1:
            self.exit_coords['row'] = self.exit_coords['row']-1
        elif self.exit_coords['row'] == len(self.maze) - 2:
            self.exit_coords['row'] = self.exit_coords['row']+1
        elif self.exit_coords['column'] == 1:
            self.exit_coords['column'] = self.exit_coords['column']-1
        elif self.exit_coords['column'] == len(self.maze[0])-2:
            self.exit_coords['column'] = self.exit_coords['column']+1
        else:
            print("Deus sabe")
        
        self.maze[self.exit_coords['row']][self.exit_coords['column']] = 'e'
        self.showMaze()
        print(self.exit_coords)

mazze = Maze()
mazze.mountMaze()