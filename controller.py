from select import select
class Controller:
    def __init__(self):
        self.xv = 0
        self.yv = 0
        
        self.down = [0, 0, 0, 0]
        
    def keyDown(self, e):
        #print(e.unicode)
        #97: a, 100: d
        
        if(e.key == 119):
            self.down[0] = 1
            self.yv = -1
            
        if(e.key == 115):
            self.down[2] = 1
            self.yv = 1
            
        if(e.key == 97):
            self.down[1] = 1
            self.xv = -1
            
        if(e.key == 100):
            self.down[3] = 1
            self.xv = 1
        
        
    def keyUp(self, e):
        if(e.key == 119):
            if(self.down[2] == 1):
                self.yv = 1
            else:
                self.yv = 0
            
            self.down[0] = 0
            
        if(e.key == 115):
            if(self.down[0] == 1):
                self.yv = -1
            else:
                self.yv = 0
            
            self.down[2] = 0
            
        if(e.key == 97):
            if(self.down[3] == 1):
                self.xv = 1
            else:
                self.xv = 0
            
            self.down[1] = 0
            
        if(e.key == 100):
            if(self.down[1] == 1):
                self.xv = -1
            else:
                self.xv = 0
            
            self.down[3] = 0
            
        