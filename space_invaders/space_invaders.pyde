class Bullet():
    def __init__(self,player.positionX,player.positionY):
        rect(player.positionX,player.positionY,5,10)
        self.positionX=player.positionX
        self.positionY=player.positionY
    def update(self):
        self.positionY+=3
