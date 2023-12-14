class Controller:
    def __init__(self,vector):
        self.vector = vector

    def top(self):
        self.vector.y -= 1
    def bottom(self):
        self.vector.y += 1
    def right(self):
        self.vector.x -= 1
    def left(self):
        self.vector.x += 1
    
    # def move(self,char):
    #     if char=='w':
    #         self._top()
    #     if char=='s':
    #         self._bottom()
    #     if char=='d':
    #         self._left()
    #     if char=='a':
    #         self._right()

    