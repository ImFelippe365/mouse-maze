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

    def canMoveToDown(self):
        row = self.mouse_coords['row']
        column = self.mouse_coords['column']
        down_position = self.maze[row+1][column]
        if (down_position != '0'):
            return False
        if(down_position is None):
            return False
        
        return True
    
    def canMoveToUp(self):
        row = self.mouse_coords['row']
        column = self.mouse_coords['column']
        up_position = self.maze[row-1][column]
        if (up_position != '0'):
            return False
        if(up_position is None):
            return False
        
        return True

    def canMoveToRight(self):
        row = self.mouse_coords['row']
        column = self.mouse_coords['column']
        right_position = self.maze[row+1][column]
        
        if (right_position is None):
            return False
        if(right_position != '0'):
            return False
        
        return True
    
    def canMoveToLeft(self):
        row = self.mouse_coords['row']
        column = self.mouse_coords['column']
        left_position = self.maze[row][column-1]
        
        if (left_position is None):
            return False
        if(left_position != '0'):
            return False
        
        return True

    def moveToLeft(self):
        if not self.canMoveToLeft():
            return False
        
        row = self.mouse_coords['row']
        column = self.mouse_coords['column']
        self.moveMouse({
            'column': column-1,
            'row': row,
        })
    
    def moveToRight(self):
        if not self.canMoveToRight():
            return False
        
        row = self.mouse_coords['row']
        column = self.mouse_coords['column']
        self.moveMouse({
            'column': column+1,
            'row': row,
        })
    
    def moveToDown(self):
        if not self.canMoveToDown():
            return False
        
        row = self.mouse_coords['row']
        column = self.mouse_coords['column']
        self.moveMouse({
            'column': column,
            'row': row+1,
        })
    
    def moveToUp(self):
        if not self.canMoveToUp():
            return False

        row = self.mouse_coords['row']
        column = self.mouse_coords['column']
        
        self.moveMouse({
            'column': column,
            'row': row-1,
        })

    def showMaze(self):
        for row_number in range(len(self.maze)):
            print(self.maze[row_number])

    def findMousePosition(self):
        for row_number in range(len(self.maze)):
            find_mouse = ''.join(self.maze[row_number]).find('m')
            if find_mouse >= 0:
                self.mouse_coords['column'] = find_mouse
                self.mouse_coords['row'] = row_number
    
    def findExitPosition(self):
        for row_number in range(len(self.maze)):
            find_exit = ''.join(self.maze[row_number]).find('e')
            if find_exit >= 0:
                self.exit_coords['column'] = find_exit
                self.exit_coords['row'] = row_number
    
    def moveMouse(self, position_coords):
        self.maze[position_coords['row']][position_coords['column']] = 'm'
        self.maze[self.mouse_coords['row']][self.mouse_coords['column']] = '0'
        self.mouse_coords = position_coords
        print(position_coords)

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

        self.findExitPosition()
                
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
            print("(!) Erro inesperado ao montar o labirinto")
        
        self.maze[self.exit_coords['row']][self.exit_coords['column']] = 'e'
        self.findMousePosition()
        print()
        self.showMaze()
        print()
        self.moveToLeft()
        self.moveToLeft()
        self.moveToUp()
        self.moveToDown()
        self.showMaze()

mazze = Maze()
mazze.mountMaze()