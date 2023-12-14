class Vector:
    
    def __init__ (self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def move(self,vector):
        self.x += vector.x
        self.y += vector.y
        self.z += vector.z

    def print(self):
        print(f'({self.x},{self.y},{self.z})')