from abc import ABCMeta, abstractmethod

class Sprite():
    __metaclass__=ABCMeta
    @abstractmethod
    def __init__(self, image):
        self.image = image

class MenuOptions():
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.startBtnPos = 290
        self.restartBtnPos = 390
        self.stopBtnPos = 490
        self.btnGridLineStarts = 10

    def sketchBtn(self, x, y, colorR, colorG, colorB):
        self.x = x
        self.y = y
        fill(colorR, colorG, colorB)
        rect(self.x, self.y, self.width, self.height)

    def sketchText(self, label, labelX, labelY, colorR, colorG, colorB):
        fill(colorR, colorG, colorB)
        textSize(20)
        text(label, labelX, labelY)
        
    def sketchMenu(self):
        self.sketchBtn(self.startBtnPos, self.btnGridLineStarts, 0, 255, 0)
        self.sketchText("START", self.startBtnPos + 15, self.btnGridLineStarts + 25, 255, 255, 255)

        self.sketchBtn(self.restartBtnPos, self.btnGridLineStarts, 0, 0, 255)
        self.sketchText("RESTART", self.restartBtnPos + 5, self.btnGridLineStarts + 25, 255, 255, 255)

        self.sketchBtn(self.stopBtnPos, self.btnGridLineStarts, 255, 0, 0)
        self.sketchText("STOP", self.stopBtnPos + 25, self.btnGridLineStarts + 25, 255, 255, 255)
        
    def react(self):
        if mousePressed:       
            if mouseX>self.stopBtnPos and mouseX<self.stopBtnPos+self.width \
                and mouseY>self.btnGridLineStarts and mouseY<self.btnGridLineStarts+self.height:
                    stop()  
            if mouseX>self.startBtnPos and mouseX<self.startBtnPos+self.width \
                and mouseY>self.btnGridLineStarts and mouseY<self.btnGridLineStarts+self.height:
                    start() 
            if mouseX>self.restartBtnPos and mouseX<self.restartBtnPos+self.width \
                and mouseY>self.btnGridLineStarts and mouseY<self.btnGridLineStarts+self.height:
                    restart()

class Bullet():
    
    def __init__(self, shooter_positionX, shooter_positionY):
        self.positionX = shooter_positionX
        self.positionY = shooter_positionY
        
    def show(self):
        img = loadImage("Pocisk 1.png")
        image(img, self.positionX, self.positionY)            
        
    def update(self, shooter_positionY):
        if shooter_positionY <= 600 and shooter_positionY >= 200: #przykładowy zakres pozycji gracza
            self.positionY -= 5 #szybkość lotu
        if shooter_positionY < 200: #przykładowy zakres pozycji wroga
            self.positionY += 5 #szybkość lotu
            
    def is_out_of_bounds(self, shooter_positionX, shooter_positionY):  #obsługa pocisku poza obszarem gry
        if self.positionY > height + 50 or self.positionY < 0 - 50: #powrot pocisku do obiektu strzelajacego
            self.positionX = shooter_positionX
            self.positionY = shooter_positionY


class Barrier():
    def __init__(self):
        self.positionX=height*25/60
        self.positionY=height*5/6
        
    def show(self):
        rect(self.positionX,self.positionY,100,10) #tymczasowa bariera jedna
        
    def destroy_part(self):        
        pass    
        
        
class Player():
    COOLDOWN = 30
    
    def __init__(self):
        self.speed = 3 #zmienić wartość na prędkość statku
        self.h = 20 #zmienić wartość na wysokość statku
        self.w = 20 #zmienić wartość na długość statku
        self.x = width/2
        self.y = height - self.h #wartość taka aby statek znajdował się na dole planszy
        self.goes_right = False # czy aktualnie ruch w prawo
        self.goes_left = False #czy aktualnie ruch w lewo
        self.lasers = []
        self.cool_down_counter = 0

    def show(self):
        fill(0)#usunąć kiedy będzie już model statku
        rect(self.x,self.y,self.w,self.h) #zamienić później na model statku
        
    def update(self):
        self.x = self.x + (self.goes_right - self.goes_left)*self.speed #ruch statku gracza
        if not (self.x >= 0): #statek nie może wyjść z lewej
            self.x = 0 + self.w
        if not (self.x <= width): #statek nie może wyjść z prawej
            self.x = (width - self.w)
                
    def shoot(self):
        if self.cool_down_counter == 0:
                laser = Laser(self.x, self.y)
                self.lasers.append(laser)
                self.cool_down_counter = 1
                print("strzelono") # tu trzebaby narysować strzałę?
                
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
                self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
                self.cool_down_counter += 1
                
                
class Laser:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        
    def move(self, vel):
        self.y += vel
        
    def off_screen(self, height):
        return self.y <= height and self.y >= 0
    
    def collision(self, obj):
        return collide(obj, self)
    
    def collide(obj1,obj2):
        offset_x = obj2.x - obj1.x
        offset_y = obj2.y - obj1.y
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) !=None


class Enemy(): #klasa Przeciwnik
    
    def usun(self):
        self.x=99999
        self.hidden=True
        
    def __init__(self):
        self.position = 0
        self.hidden=False
        self.x = 50
        self.y = 50
        self.down = 0
        self.speed = 3
        self.w=20
        self.h= 20
        self.img = loadImage("Przeciwnik_{}.png".format(int(random(4))))
        # Atakowanie
        self.lastAttackTime = 0
        self.delayBetweenAttacks = 1000 - random(300) # czas w milisekundach
        
        #wróg
    def show(self, offset):
        fill(0)#usunąć kiedy będzie już model wroga
        self.position = offset
        rect(self.x+self.position ,self.y, self.w, self.h)#zamienić później
        image(self.img, self.x+self.position, self.y, self.w, self.h) #wyświetlanie grafiki przeciwnika na wyzej ustalona pozycje

    def update(self): #poruszania w prawo, lewo i w dół
        if self.hidden:
            return
        self.x += self.speed
        if not (self.x+self.position <= width-self.w/2):
            self.down = self.y
            self.y += 20
            self.speed *= -1
        if not (self.x+self.position >= 0+self.w/2):
            self.down = self.y
            self.y += 20
            self.speed *= -1
    
    def attack(self):
        currentTime = millis()
        delayBetweenAttacksPassed = (currentTime - self.lastAttackTime) > self.delayBetweenAttacks
        if(delayBetweenAttacksPassed):
            self.lastAttackTime = millis()
            # tutaj dodać funkcję wystrzeliwującą pocisk
            rect(100, 100, 100, 100) # do usunięcia, gdy pojawi się pocisk (kwadrat pojawia się w momencie, gdy mają strzelić)

class HeartPlayer():
    
    def __init__(self): 
        self.player_heart = 3
         
    def loss_heart(self):
        self.player_heart -= 1
        if self.player_heart == 0:
            text("GAME OVER", height/2,width/4)
            #tutaj wstawić okno końca gry    
 
    def show(self):
        text(self.player_heart, 30, 50)
        
class Gwiazdy():
    def __init__(self, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
            
    def ruch(self):
        fill(255, 255, 255)
        square(self.x, self.y, 5)
        self.y = self.y + self.speed #jak szbko lecą w dol
        self.x = self.x + 1 #co ile przesuwaja sie w prawo
        if(frameCount % 2 == 0): #if(frameCount % (tu wpisujemy co ile klatek ) == 0)
            if (self.y > height) or self.x > width :
                self.y = 0
                self.x = int(random(600))
      
            
def setup():
    global gamePlay
    #frameRate(10)
    gamePlay = 0
    size(600, 600)
    global player, bullets, przeciwnik, bullet, player_heart,enemies, barrier, menuButton, gwiazda
    player = Player()
    enemy1 = Enemy()# póżniej można zamienić na listę przeciwników
    enemy2 = Enemy()
    enemy3 = Enemy()
    enemy4 = Enemy()
    bullet = Bullet(player.x, player.y) #tymczasowy pocisk gracza
    bullets = []
    enemies = [enemy1, enemy2, enemy3, enemy4]
    barrier=Barrier()
    player_heart = HeartPlayer()
    textSize(30)
    menuButton = MenuOptions(30, 100)
    gwiazda = Gwiazdy(50, 100, 2)

def draw():
    global player, bullets, enemy, bullet, player_heart, enemies, menuButton, gamePlay, gwiazda
    background(100)
    gwiazda.ruch()
    
    if gamePlay: 
        player.show()
        player.update()
        bullet.show() #tymczasowy pocisk
        bullet.update(player.y)
        bullet.is_out_of_bounds(player.x, player.y) #sprawdzanie czy pocisk jest poza obszarem gry
        player_heart.show()
        barrier.show()
        for offset, enemy in enumerate(enemies):
            enemy.show(offset * 100)
            enemy.update()
            enemy.attack()
            if bullet.positionX-(enemy.x+enemy.position) < 20 \
                and (bullet.positionX-(enemy.x+enemy.position) > -20) \
                and (bullet.positionY-enemy.y) < 20 and (bullet.positionY-enemy.y > -20):
                enemy.usun()
            if (enemy.y >= player.y and enemy.x+enemy.position == player.x):#wykrywanie sytuacji, gdy przeciwnicy zeszli do poziomu gracza i zakańcza grę
                stop();
                # tu wyświetlenie końca gry, gdy ktoś go już stworzy
        player.cooldown()
                
    menuButton.sketchMenu()
    menuButton.react()

def keyPressed(): #ruch statku przy kliknięciu strzałek
    if keyCode == LEFT:
        player.goes_left = True
    if keyCode == RIGHT:
        player.goes_right = True
    if key == ' ':
        player.shoot()
        
def keyReleased(): #bezruch statku przy puszczeniu strzałek
    if keyCode == LEFT:
        player.goes_left = False
    if keyCode == RIGHT:
        player.goes_right = False

def start():
    global gamePlay
    gamePlay = 1

def stop():
    global gamePlay
    gamePlay = 0
    
def restart():
    global gamePlay
    setup()
    gamePlay = 1
