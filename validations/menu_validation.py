from functions.base import Base

from functions.addition import Addition
from functions.subtraction import Subtraction
from functions.multiplication import Multiplication
from functions.division import Division

class Menu:
    def process_validation(self, process):
        while process == 's' or process == 'S':
            return True
        return False

    def show_menu(self):
        print('-'*50)
        print('1 - Addition.\n2 - Subtraction.\n3 - Multiplication.\n4 - Division.')
        print('-'*50)

    def option_validation(self, option):
        if option == 1:
            operation = Addition()
            self.load_values(operation)
        elif(option == 2):
            operation = Subtraction()
            self.load_values(operation)
        elif(option == 3):
            operation = Multiplication()
            self.load_values(operation)
        elif(option == 4):
            operation = Division()
            self.load_values(operation)

    def load_values(self, operation):
            x = float(input('Informe o primeiro número: '))
            y = float(input('Informe o segundo número: '))
            operation.setX(x)
            operation.setY(y)
            result = operation.result()
            print(result)