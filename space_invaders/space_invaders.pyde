
class Bullet():
    def __init__(self,player_positionX,player_positionY):
        rect(player_positionX,player_positionY,5,10)
        self.positionX=player_positionX
        self.positionY=player_positionY
    def update(self):
        self.positionY+=3
        
class Player():
    def __init__(self):
        self.speed = 3 #zmienić wartość na prędkość statku
        self.h = 20 #zmienić wartość na wysokość statku
        self.w = 20 #zmienić wartość na długość statku
        self.x = width/2
        self.y = height - self.h #wartość taka aby statek znajdował się na dole planszy
        self.goes_right = False # czy aktualnie ruch w prawo
        self.goes_left = False #czy aktualnie ruch w lewo

    def show(self):
        fill(0)#usunąć kiedy będzie już model statku
        rect(self.x,self.y,self.w,self.h) #zamienić później na model statku
    def update(self):
        self.x = self.x + (self.goes_right - self.goes_left)*self.speed #ruch statku gracza
        if not (self.x >= 0): #statek nie może wyjść z lewej
            self.x = 0 + self.w
        if not (self.x <= width): #statek nie może wyjść z prawej
            self.x = (width - self.w)

class Przeciwnik(): #klasa Przeciwnik
    def __init__(self, pozycja):
        self.pozycja = pozycja
        self.x = 50 + pozycja
        self.y = 50
        self.left = 0
        self.right = 0
        self.down = 0
        self.speed = 10
    def update(self): #poruszania w prawo, lewo i w dół
        self.right = self.x + 1
        self.x += self.speed
        if not (self.x <= 600):
            self.down = self.y
            self.y += 20
            self.x = 600
            self.speed *= -1
        if not (self.x >= 20):
            self.down = self.y
            self.y += 20
            self.x = 20
            self.speed *= -1
            
 def buttonsMenu(): #menu

    def buttonsMenu():
    global graStart = 0

    if mousePressed:
        if mouseX>y and mouseX<y+100 and mouseY>x and mouseY<x+100:
            graStart = 1

        if mouseX>y and mouseX<y+100 and mouseY>x+150 and mouseY<x+250:
            exit()        
        
def setup():
    size(600, 600)
    global player
    player = Player()
    
def draw():
    background(100)
    player.show()
    player.update()
    
def keyPressed(): #ruch statku przy kliknięciu strzałek
    if keyCode == LEFT:
        player.goes_left = True
    if keyCode == RIGHT:
        player.goes_right = True
def keyReleased(): #bezruch statku przy puszczeniu strzałek
    if keyCode == LEFT:
        player.goes_left = False
    if keyCode == RIGHT:
        player.goes_right = False

        
