class Position():
    '''Position in the map fro the generals io
        Coridinate system begin from top left
    '''

    def __init__(self,y=0,x=0):

        self.y=y
        self.x = x

    def get_turple(self):
        return (self.x,self.y)