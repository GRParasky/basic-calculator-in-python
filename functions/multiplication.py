from functions.base import Base

class Multiplication(Base):
    def result(self):
        result = self.x * self.y
        return result
