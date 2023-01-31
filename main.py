from stack import Stacks
from tkinter import *
import time

class Maze:
    def __init__(self, master):
        self.master = master 
        

        self.maze = None
        self.exit_coords = {
            'column': None,
            'row': None,
        }
        self.mouse_coords = {
            'column': None,
            'row': None,
        }
        self.counter = 0
        
        self.mountMaze()
    
    def create(self): 
        self.showMaze()
        self.canvas = Canvas(self.master) 

        squareSize = 30

        for row in range(0, len(self.maze)):
            y2RowRange = (row+1)*squareSize
            for column in range(len(self.maze[row])):
                column_value = self.maze[row][column]

                x1ColumnRange = (column+1)*squareSize
                x2ColumnRange = x1ColumnRange - squareSize if not column == 0 else 0
                y1RowRange = y2RowRange - squareSize if not row == 0 else 0

                print(y1RowRange, y2RowRange)
                if (column_value == '1'):
                    self.canvas.create_rectangle(
                    x1ColumnRange, y1RowRange, x2ColumnRange, y2RowRange,
                outline="blue", fill = "blue", width = 1)
                elif (column_value == 'e'):
                    self.canvas.create_rectangle(
                    x1ColumnRange, y1RowRange, x2ColumnRange, y2RowRange,
                outline="green", fill = "green", width = 1)
                elif (column_value == 'm'):
                    # img = PhotoImage(name="mouse", file='.\mouse.png')
                    # self.label = Label(self.master, image=img, bd=5, relief=SUNKEN)
                    # self.label.pack(side=RIGHT)
                    self.mouseForm = self.canvas.create_rectangle(
                    x1ColumnRange, y1RowRange, x2ColumnRange, y2RowRange,
                outline="brown", fill = "brown", width = 1)

        self.canvas.pack(fill = BOTH, expand = 1) 
        
        self.findExit()

    def animateMouse(self):
        self.showMaze()
        self.canvas = Canvas(self.master) 

        squareSize = 30

        for row in range(0, len(self.maze)):
            y2RowRange = (row+1)*squareSize
            for column in range(len(self.maze[row])):
                column_value = self.maze[row][column]

                x1ColumnRange = (column+1)*squareSize
                x2ColumnRange = x1ColumnRange - squareSize if not column == 0 else 0
                y1RowRange = y2RowRange - squareSize if not row == 0 else 0

                if (column_value == 'm'):
                    # img = PhotoImage(name="mouse", file='.\mouse.png')
                    # self.label = Label(self.master, image=img, bd=5, relief=SUNKEN)
                    # self.label.pack(side=RIGHT)
                    self.canvas.create_rectangle(
                    x1ColumnRange-15, y1RowRange-15, x2ColumnRange-15, y2RowRange-15,
                outline="white", fill = "white", width = 1)

                    self.canvas.create_rectangle(
                    x1ColumnRange, y1RowRange, x2ColumnRange, y2RowRange,
                outline="brown", fill = "brown", width = 1)

        self.canvas.pack(fill = BOTH, expand = 1) 

    def canMoveToDown(self):
        row = self.mouse_coords['row']
        column = self.mouse_coords['column']
        down_position = self.maze[row+1][column]
        if (down_position == 'e'):
            return True
        if (down_position != '0'):
            return False
        if(down_position is None):
            return False
        
        return True
    
    def canMoveToUp(self):
        row = self.mouse_coords['row']
        column = self.mouse_coords['column']
        up_position = self.maze[row-1][column]
        if (up_position == 'e'):
            return True
        if (up_position != '0'):
            return False
        if(up_position is None):
            return False
        
        return True

    def canMoveToRight(self):
        row = self.mouse_coords['row']
        column = self.mouse_coords['column']
        right_position = self.maze[row][column+1]
        if (right_position == 'e'):
            return True
        if (right_position is None):
            return False
        if(right_position != '0' or right_position == 'e'):
            return False
        
        return True
    
    def canMoveToLeft(self):
        row = self.mouse_coords['row']
        column = self.mouse_coords['column']
        left_position = self.maze[row][column-1]
        if (left_position == 'e'):
            return True
        if (left_position is None):
            return False
        if(left_position != '0' or left_position == 'e'):
            return False
        
        return True

    def moveToLeft(self):
        if not self.canMoveToLeft():
            return False
        
        row = self.mouse_coords['row']
        column = self.mouse_coords['column']
        position = {
            'column': column-1,
            'row': row,
        }
        self.moveMouse(position)

        return position
    
    def moveToRight(self):
        if not self.canMoveToRight():
            return False
        
        row = self.mouse_coords['row']
        column = self.mouse_coords['column']
        position = {
            'column': column+1,
            'row': row,
        }
        self.moveMouse(position)

        return position
    
    def moveToDown(self):
        if not self.canMoveToDown():
            return False
        
        row = self.mouse_coords['row']
        column = self.mouse_coords['column']
        position = {
            'column': column,
            'row': row+1,
        }
        self.moveMouse(position)
        return position

    def moveToUp(self):
        if not self.canMoveToUp():
            return False

        row = self.mouse_coords['row']
        column = self.mouse_coords['column']
        
        position = {
            'column': column,
            'row': row-1,
        }
        self.moveMouse(position)

        return position

    def showMaze(self):
        for row_number in range(len(self.maze)):
            print(self.maze[row_number])

    def saveMousePosition(self):
        for row_number in range(len(self.maze)):
            find_mouse = ''.join(self.maze[row_number]).find('m')
            if find_mouse >= 0:
                self.mouse_coords['column'] = find_mouse
                self.mouse_coords['row'] = row_number
    
    def saveExitPosition(self):
        for row_number in range(len(self.maze)):
            find_exit = ''.join(self.maze[row_number]).find('e')
            if find_exit >= 0:
                self.exit_coords['column'] = find_exit
                self.exit_coords['row'] = row_number
    
    def moveMouse(self, position_coords):
        self.maze[position_coords['row']][position_coords['column']] = 'm'
        self.maze[self.mouse_coords['row']][self.mouse_coords['column']] = '.'
        self.mouse_coords = position_coords

    def __findingExit(self, tries):
        # Função recursiva para encontrar a saída
        # 1º Direita 2º Esquerda 3º Baixo 4º Cima
        exit_row, exit_column = self.exit_coords['row'], self.exit_coords['column']
        mouse_row, mouse_column = self.mouse_coords['row'], self.mouse_coords['column']
        self.showMaze()
        self.counter += 1
        print()
        
        if (exit_row == mouse_row and exit_column == mouse_column):
            return tries
        if self.canMoveToRight():
            right = self.moveToRight()
            self.canvas.move(self.mouseForm, 30, 0)
            tries.stackUp(right)
        elif self.canMoveToLeft():
            left = self.moveToLeft()
            self.canvas.move(self.mouseForm, -30, 0)
            tries.stackUp(left)
        elif self.canMoveToDown():
            down = self.moveToDown()
            self.canvas.move(self.mouseForm, 0, 30)
            tries.stackUp(down)
        elif self.canMoveToUp():
            up = self.moveToUp()
            self.canvas.move(self.mouseForm, 0, -30)
            tries.stackUp(up)
        else:
            # ROW POSITIVO SOBE, NEGATIVO DESCE
            # COLUNA NEGATIVA DIREITA, POSITIVO ESQUERDA
            oldCoords = tries.getTop()
            tries.unStack()
            newCoords = tries.getTop()
            coordsDiff = {
                'column': oldCoords['column']-newCoords['column'],
                'row': oldCoords['row'] - newCoords['row']
            }
            if (coordsDiff['column'] < 0 and coordsDiff['row'] == 0):
                self.canvas.move(self.mouseForm, 30, 0)
            if (coordsDiff['column'] > 0 and coordsDiff['row'] == 0):
                self.canvas.move(self.mouseForm, -30, 0)
            if (coordsDiff['column'] == 0 and coordsDiff['row'] > 0):
                self.canvas.move(self.mouseForm, 0, -30)
            if (coordsDiff['column'] == 0 and coordsDiff['row'] < 0):
                self.canvas.move(self.mouseForm, 0, 30)
            print("NEW COORDS", coordsDiff)
            self.moveMouse(newCoords)
        
        # self.animateMouse()
        self.master.update()        
        time.sleep(0.5)
        return self.__findingExit(tries)

    def findExit(self):
        # Função para tentar as possibilidades com pilha e encontrar saída
        tries = Stacks(10000)
        tries.stackUp(self.mouse_coords)
        result = self.__findingExit(tries)
        print(self.counter)

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

        self.saveExitPosition()
                
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
        self.saveMousePosition()
        
        self.create()
        # self.findExit()

root = Tk()
mazze = Maze(root)
root.mainloop()

# FALTA ARRUMAR A CAPACIDADE DO TAMANHO DA PILHA