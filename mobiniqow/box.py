class Box:
    def __init__(self,*args):
        self.args = args
        self.objects = {}

    def init(self):
        for i in self.args:
            self.objects[i.x]=i
    
    def is_items(self,vector):
        # print(dir(vector))
        return vector.x in self.objects