class Rendere:
    CHARACTER = "."
    VECTOR_SCHEMA = "*"
    def __init__(self,x,y):
        self.x = x
        self.y = y
        raw = self.CHARACTER * self.x
        self.screenT =""
        for _ in range(y):
            self.screenT +="\n"
            self.screenT += raw
        self.screen = self.screenT

    def render(self):
        print(self.screen)
    
    def draw_vector(self,vector):
        temp = []
        list_y = self.screenT.split('\n')
        list_y[vector.y] = list_y[vector.y][:vector.x-1] + self.VECTOR_SCHEMA+list_y[vector.y][vector.x:]
        self.screen=""
        for i in list_y:
            self.screen+=f'{i}\n'
        # list_y[vector.y]
        # for i in list_y:
        #     if
        #     list_y[vector.y][vector.x] = self.VECTOR_SCHEMA
        