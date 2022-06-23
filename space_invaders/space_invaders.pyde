global size_X
global size_Y
plansza_X = 600 #zmienić wartość na rozmiar planszy(size) w osi X
plansza_Y = 600 #zmienić wartość na rozmiar planszy(size) w osi Y

class Bullet():
    def __init__(self,player_positionX,player_positionY):
        rect(player_positionX,player_positionY,5,10)
        self.positionX=player_positionX
        self.positionY=player_positionY
    def update(self):
        self.positionY+=3
        
class player(object):
    def __init__(self):
        self.speed = 3 #zmienić wartość na prędkość statku
        self.h = 20 #zmienić wartość na wysokość statku
        self.w = 20 #zmienić wartość na długość statku
        self.x = 300 #zmienić wartość 300 tak aby statek rozpoczynał grę na środku
        self.y = plansza_X - self.h #wartość tak aby statek znajdował się na dole planszy
        self.right = 0 #ruch w prawo
        self.left = 0 #ruch w lewo

    def show(self):
        fill(0)#usunąć kiedy będzie już model statku
        rect(self.x,self.y,self.w,self.h) #zamienić później na model statku
    def update(self):
        self.x = self.x + (self.right - self.left)*self.speed #ruch statku
        if not (self.x >= 0): #statek nie może wyjść z lewej
            self.x = 0
        if not (self.x <= plansza_X): #statek nie może wyjść z prawej
            self.x = (plansza_X - self.h)
        
        
def setup():
    size(plansza_X, plansza_Y)
    global p
    p = player()
    
def draw():
    background(100)
    p.show()
    p.update()
    
def keyPressed(): #ruch statku przy kliknięciu strzałek
    if keyCode == LEFT:
        p.left=1
    if keyCode == RIGHT:
        p.right=1
def keyReleased(): #bezruch statku przy puszczeniu strzałek
    if keyCode == LEFT:
        p.left=0
    if keyCode == RIGHT:
        p.right=0
