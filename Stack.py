import numpy

class Stacks:

    def __init__(self, capacity):
        self.__capacity = capacity
        self.__top = -1
        self.__values = numpy.empty(self.__capacity, dtype=list)

    def getRowLength(self):
        return self.__top+1

    def getColumnsLength(self):
        return len(self.__values[self.__top]) if not self.__isEmpty() else None
    
    def __isEmpty(self):
        return self.__top == -1

    def __isFull(self):
        return self.__capacity-1 == self.__top

    def stackUp(self, valueToStackUp):
        if (self.__isFull()):
            print('(!) A pilha está cheia')
        else:
            self.__top += 1
            self.__values[int(self.__top)] = valueToStackUp
    
    def unStack(self):
        if (self.__isEmpty()):
            print('(!) A pilha está vazia')
            return None
        else:
            self.__top -= 1
            return self.__values[self.__top+1]
            # print(f'(✓) Valor removido: {self.__values[self.__top+1]}')

    def showTop(self):
        if (self.__isEmpty()):
            print('(!) A pilha está vazia')
        else:
            print(f'(✓) Topo da pilha: {self.__values[self.__top]}')

    def showFullStack(self):
        if (self.__isEmpty()):
            print('(!) A pilha está vazia')
        else:
            for index in range(self.__top+1):
                print(self.__values[index], end=', ')