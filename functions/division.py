from functions.base import Base

class Division(Base):
    def result(self):
        result = self.x / self.y
        return result
