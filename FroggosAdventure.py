import pygame                                                                                                                                                                                                                                                                                                                                                                                                                                                   #Made by SmellyFrog
import random
import time
from pygame.locals import *
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.init()

screenWidth = 320 #112
screenHeight = 304 #116

crack = pygame.mixer.Sound("audios/knock.wav")
coinCollect = pygame.mixer.Sound("audios/coin.wav")
jigsawCollect = pygame.mixer.Sound("audios/collected.wav")
blockSound = pygame.mixer.Sound("audios/hit.wav")
gulp = pygame.mixer.Sound("audios/gulp.wav")

window = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption("Froggo's adventure")
pygame.mouse.set_visible(0)

notEdibleObj = ["flipblock", "goalsign", "flower", "beanstalktip"]

grasstile = [
    pygame.image.load("assets/grass TL1.png").convert_alpha(), pygame.image.load("assets/grass TL2.png").convert_alpha(), pygame.image.load("assets/grass TL3.png").convert_alpha(), pygame.image.load("assets/grass TL4.png").convert_alpha(), pygame.image.load("assets/grass TL5.png").convert_alpha(),
    pygame.image.load("assets/grass BL1.png").convert_alpha(), pygame.image.load("assets/grass BL2.png").convert_alpha(), pygame.image.load("assets/grass BL3.png").convert_alpha(), pygame.image.load("assets/grass BL4.png").convert_alpha(), pygame.image.load("assets/grass BL5.png").convert_alpha(),
    pygame.image.load("assets/grass TR1.png").convert_alpha(), pygame.image.load("assets/grass TR2.png").convert_alpha(), pygame.image.load("assets/grass TR3.png").convert_alpha(), pygame.image.load("assets/grass TR4.png").convert_alpha(), pygame.image.load("assets/grass TR5.png").convert_alpha(),
    pygame.image.load("assets/grass BR1.png").convert_alpha(), pygame.image.load("assets/grass BR2.png").convert_alpha(), pygame.image.load("assets/grass BR3.png").convert_alpha(), pygame.image.load("assets/grass BR4.png").convert_alpha(), pygame.image.load("assets/grass BR5.png")
    ]
woodtile = [
    pygame.image.load("assets/wood TL1.png").convert_alpha(), pygame.image.load("assets/wood TL2.png").convert_alpha(), pygame.image.load("assets/wood TL3.png").convert_alpha(), pygame.image.load("assets/wood TL4.png").convert_alpha(), pygame.image.load("assets/wood TL5.png").convert_alpha(),
    pygame.image.load("assets/wood BL1.png").convert_alpha(), pygame.image.load("assets/wood BL2.png").convert_alpha(), pygame.image.load("assets/wood BL3.png").convert_alpha(), pygame.image.load("assets/wood BL4.png").convert_alpha(), pygame.image.load("assets/wood BL5.png").convert_alpha(),
    pygame.image.load("assets/wood TR1.png").convert_alpha(), pygame.image.load("assets/wood TR2.png").convert_alpha(), pygame.image.load("assets/wood TR3.png").convert_alpha(), pygame.image.load("assets/wood TR4.png").convert_alpha(), pygame.image.load("assets/wood TR5.png").convert_alpha(),
    pygame.image.load("assets/wood BR1.png").convert_alpha(), pygame.image.load("assets/wood BR2.png").convert_alpha(), pygame.image.load("assets/wood BR3.png").convert_alpha(), pygame.image.load("assets/wood BR4.png").convert_alpha(), pygame.image.load("assets/wood BR5.png")
    ]
cloudtile = [
    pygame.image.load("assets/cloud TL1.png").convert_alpha(), pygame.image.load("assets/cloud TL2.png").convert_alpha(), pygame.image.load("assets/cloud TL3.png").convert_alpha(), pygame.image.load("assets/cloud TL4.png").convert_alpha(), pygame.image.load("assets/cloud TL5.png").convert_alpha(),
    pygame.image.load("assets/cloud BL1.png").convert_alpha(), pygame.image.load("assets/cloud BL2.png").convert_alpha(), pygame.image.load("assets/cloud BL3.png").convert_alpha(), pygame.image.load("assets/cloud BL4.png").convert_alpha(), pygame.image.load("assets/cloud BL5.png").convert_alpha(),
    pygame.image.load("assets/cloud TR1.png").convert_alpha(), pygame.image.load("assets/cloud TR2.png").convert_alpha(), pygame.image.load("assets/cloud TR3.png").convert_alpha(), pygame.image.load("assets/cloud TR4.png").convert_alpha(), pygame.image.load("assets/cloud TR5.png").convert_alpha(),
    pygame.image.load("assets/cloud BR1.png").convert_alpha(), pygame.image.load("assets/cloud BR2.png").convert_alpha(), pygame.image.load("assets/cloud BR3.png").convert_alpha(), pygame.image.load("assets/cloud BR4.png").convert_alpha(), pygame.image.load("assets/cloud BR5.png")
    ]
castletile = [
    pygame.image.load("assets/castle TL1.png").convert_alpha(), pygame.image.load("assets/castle TL2.png").convert_alpha(), pygame.image.load("assets/castle TL3.png").convert_alpha(), pygame.image.load("assets/castle TL4.png").convert_alpha(), pygame.image.load("assets/castle TL5.png").convert_alpha(),
    pygame.image.load("assets/castle BL1.png").convert_alpha(), pygame.image.load("assets/castle BL2.png").convert_alpha(), pygame.image.load("assets/castle BL3.png").convert_alpha(), pygame.image.load("assets/castle BL4.png").convert_alpha(), pygame.image.load("assets/castle BL5.png").convert_alpha(),
    pygame.image.load("assets/castle TR1.png").convert_alpha(), pygame.image.load("assets/castle TR2.png").convert_alpha(), pygame.image.load("assets/castle TR3.png").convert_alpha(), pygame.image.load("assets/castle TR4.png").convert_alpha(), pygame.image.load("assets/castle TR5.png").convert_alpha(),
    pygame.image.load("assets/castle BR1.png").convert_alpha(), pygame.image.load("assets/castle BR2.png").convert_alpha(), pygame.image.load("assets/castle BR3.png").convert_alpha(), pygame.image.load("assets/castle BR4.png").convert_alpha(), pygame.image.load("assets/castle BR5.png")
    ]
autumntile = [
    pygame.image.load("assets/autumn TL1.png").convert_alpha(), pygame.image.load("assets/autumn TL2.png").convert_alpha(), pygame.image.load("assets/autumn TL3.png").convert_alpha(), pygame.image.load("assets/autumn TL4.png").convert_alpha(), pygame.image.load("assets/autumn TL5.png").convert_alpha(),
    pygame.image.load("assets/autumn BL1.png").convert_alpha(), pygame.image.load("assets/autumn BL2.png").convert_alpha(), pygame.image.load("assets/autumn BL3.png").convert_alpha(), pygame.image.load("assets/autumn BL4.png").convert_alpha(), pygame.image.load("assets/autumn BL5.png").convert_alpha(),
    pygame.image.load("assets/autumn TR1.png").convert_alpha(), pygame.image.load("assets/autumn TR2.png").convert_alpha(), pygame.image.load("assets/autumn TR3.png").convert_alpha(), pygame.image.load("assets/autumn TR4.png").convert_alpha(), pygame.image.load("assets/autumn TR5.png").convert_alpha(),
    pygame.image.load("assets/autumn BR1.png").convert_alpha(), pygame.image.load("assets/autumn BR2.png").convert_alpha(), pygame.image.load("assets/autumn BR3.png").convert_alpha(), pygame.image.load("assets/autumn BR4.png").convert_alpha(), pygame.image.load("assets/autumn BR5.png")
    ]
ruinstile = [
    pygame.image.load("assets/ruins TL1.png").convert_alpha(), pygame.image.load("assets/ruins TL2.png").convert_alpha(), pygame.image.load("assets/ruins TL3.png").convert_alpha(), pygame.image.load("assets/ruins TL4.png").convert_alpha(), pygame.image.load("assets/ruins TL5.png").convert_alpha(),
    pygame.image.load("assets/ruins BL1.png").convert_alpha(), pygame.image.load("assets/ruins BL2.png").convert_alpha(), pygame.image.load("assets/ruins BL3.png").convert_alpha(), pygame.image.load("assets/ruins BL4.png").convert_alpha(), pygame.image.load("assets/ruins BL5.png").convert_alpha(),
    pygame.image.load("assets/ruins TR1.png").convert_alpha(), pygame.image.load("assets/ruins TR2.png").convert_alpha(), pygame.image.load("assets/ruins TR3.png").convert_alpha(), pygame.image.load("assets/ruins TR4.png").convert_alpha(), pygame.image.load("assets/ruins TR5.png").convert_alpha(),
    pygame.image.load("assets/ruins BR1.png").convert_alpha(), pygame.image.load("assets/ruins BR2.png").convert_alpha(), pygame.image.load("assets/ruins BR3.png").convert_alpha(), pygame.image.load("assets/ruins BR4.png").convert_alpha(), pygame.image.load("assets/ruins BR5.png")
    ]
beanstalktile = [
    pygame.image.load("assets/beanstalk TL1.png").convert_alpha(), pygame.image.load("assets/beanstalk TL2.png").convert_alpha(), pygame.image.load("assets/beanstalk TL3.png").convert_alpha(), pygame.image.load("assets/beanstalk TL4.png").convert_alpha(), pygame.image.load("assets/beanstalk TL5.png").convert_alpha(),
    pygame.image.load("assets/beanstalk BL1.png").convert_alpha(), pygame.image.load("assets/beanstalk BL2.png").convert_alpha(), pygame.image.load("assets/beanstalk BL3.png").convert_alpha(), pygame.image.load("assets/beanstalk BL4.png").convert_alpha(), pygame.image.load("assets/beanstalk BL5.png").convert_alpha(),
    pygame.image.load("assets/beanstalk TR1.png").convert_alpha(), pygame.image.load("assets/beanstalk TR2.png").convert_alpha(), pygame.image.load("assets/beanstalk TR3.png").convert_alpha(), pygame.image.load("assets/beanstalk TR4.png").convert_alpha(), pygame.image.load("assets/beanstalk TR5.png").convert_alpha(),
    pygame.image.load("assets/beanstalk BR1.png").convert_alpha(), pygame.image.load("assets/beanstalk BR2.png").convert_alpha(), pygame.image.load("assets/beanstalk BR3.png").convert_alpha(), pygame.image.load("assets/beanstalk BR4.png").convert_alpha(), pygame.image.load("assets/beanstalk BR5.png")
    ]
skytile = [
    pygame.image.load("assets/sky TL1.png").convert_alpha(), pygame.image.load("assets/sky TL2.png").convert_alpha(), pygame.image.load("assets/sky TL3.png").convert_alpha(), pygame.image.load("assets/sky TL4.png").convert_alpha(), pygame.image.load("assets/sky TL5.png").convert_alpha(),
    pygame.image.load("assets/sky BL1.png").convert_alpha(), pygame.image.load("assets/sky BL2.png").convert_alpha(), pygame.image.load("assets/sky BL3.png").convert_alpha(), pygame.image.load("assets/sky BL4.png").convert_alpha(), pygame.image.load("assets/sky BL5.png").convert_alpha(),
    pygame.image.load("assets/sky TR1.png").convert_alpha(), pygame.image.load("assets/sky TR2.png").convert_alpha(), pygame.image.load("assets/sky TR3.png").convert_alpha(), pygame.image.load("assets/sky TR4.png").convert_alpha(), pygame.image.load("assets/sky TR5.png").convert_alpha(),
    pygame.image.load("assets/sky BR1.png").convert_alpha(), pygame.image.load("assets/sky BR2.png").convert_alpha(), pygame.image.load("assets/sky BR3.png").convert_alpha(), pygame.image.load("assets/sky BR4.png").convert_alpha(), pygame.image.load("assets/sky BR5.png")
    ]
tiles = [grasstile, woodtile, cloudtile, castletile, autumntile, ruinstile, skytile]
tile2 = [pygame.image.load("assets/tile0.png").convert_alpha(), pygame.image.load("assets/tile5.png").convert_alpha(), pygame.image.load("assets/tile6.png").convert_alpha(), pygame.image.load("assets/tile1.png").convert_alpha(), pygame.image.load("assets/tile2.png").convert_alpha(), pygame.image.load("assets/tile3.png").convert_alpha(), pygame.image.load("assets/tile4.png").convert()]


frogAnimation = [pygame.image.load("assets/froggy2.png").convert_alpha(), pygame.image.load("assets/froggy1.png").convert_alpha(), pygame.image.load("assets/froggy4.png").convert_alpha(), pygame.image.load("assets/froggy3.png").convert_alpha(), pygame.image.load("assets/froggy8.png").convert_alpha(), pygame.image.load("assets/froggy7.png").convert_alpha()]
legAnimation = [pygame.image.load("assets/Leg0.png").convert_alpha(), pygame.image.load("assets/Leg1.png").convert_alpha(), pygame.image.load("assets/Leg2.png").convert_alpha(), pygame.image.load("assets/Leg3.png").convert_alpha(),]
tongueTexture = pygame.image.load("assets/tongue.png").convert_alpha()
flipBlockAnimation = [pygame.image.load("assets/flipblock0.png").convert_alpha(), pygame.image.load("assets/flipblock1.png").convert_alpha(), pygame.image.load("assets/flipblock2.png").convert_alpha(), pygame.image.load("assets/flipblock3.png").convert_alpha(), pygame.image.load("assets/flipblock4.png").convert_alpha(), pygame.image.load("assets/flipblock5.png").convert_alpha()]
coinAnimation = [pygame.image.load("assets/coin0.png").convert_alpha(), pygame.image.load("assets/coin1.png").convert_alpha(), pygame.image.load("assets/coin2.png").convert_alpha(), pygame.image.load("assets/coin3.png").convert_alpha(), pygame.image.load("assets/coin4.png").convert_alpha(), pygame.image.load("assets/coin5.png").convert_alpha()]
fruitAnimation = [pygame.image.load("assets/fruit0.png").convert_alpha(), pygame.image.load("assets/fruit1.png").convert_alpha(), pygame.image.load("assets/fruit0.png").convert_alpha(), pygame.image.load("assets/fruit2.png").convert_alpha()]
platformSprite = pygame.image.load("assets/platform.png").convert_alpha()
greenBlockAnimation = [pygame.image.load("assets/greenblock.png").convert_alpha(), pygame.image.load("assets/greenblock1.png").convert_alpha()]
popAnimation = [pygame.image.load("assets/pop0.png").convert_alpha(), pygame.image.load("assets/pop1.png").convert_alpha(), pygame.image.load("assets/pop2.png").convert_alpha(), pygame.image.load("assets/pop3.png").convert_alpha()]
jimAnimation = [pygame.image.load("assets/jim0.png").convert_alpha(), pygame.image.load("assets/jim1.png").convert_alpha()]
spikeJimAnimation = [pygame.image.load("assets/spikejim0.png").convert_alpha(), pygame.image.load("assets/spikejim1.png").convert_alpha()]
goalSignAnimation = [pygame.image.load("assets/goalsign0.png").convert_alpha(), pygame.image.load("assets/goalsign1.png").convert_alpha(), pygame.image.load("assets/goalsign2.png").convert_alpha(), pygame.image.load("assets/goalsign1.png").convert_alpha()]
goalSignFlippingAnimation = [pygame.image.load("assets/goalsign0.png").convert_alpha(), pygame.image.load("assets/goalsign3.png").convert_alpha(), pygame.image.load("assets/goalsign4.png").convert_alpha(), pygame.image.load("assets/goalsign5.png").convert_alpha(), pygame.image.load("assets/goalsign6.png").convert_alpha(), pygame.image.load("assets/goalsign7.png").convert_alpha()]
spinJimAnimation = [pygame.image.load("assets/spinjim0.png").convert_alpha(), pygame.image.load("assets/spinjim1.png").convert_alpha(), pygame.image.load("assets/spinjim2.png").convert_alpha(), pygame.image.load("assets/spinjim3.png").convert_alpha()]
flowerAnimation = [pygame.image.load("assets/flower0.png").convert_alpha(), pygame.image.load("assets/flower1.png").convert_alpha(), pygame.image.load("assets/flower2.png").convert_alpha(), pygame.image.load("assets/flower3.png").convert_alpha()]
invisibleBlockAnimation = [pygame.image.load("assets/invisibleblock0.png").convert_alpha(), pygame.image.load("assets/invisibleblock1.png").convert_alpha(), pygame.image.load("assets/invisibleblock2.png").convert_alpha()]
ironBlockAnimation = [pygame.image.load("assets/gearblock2.png").convert_alpha(), pygame.image.load("assets/gearblock3.png").convert_alpha()]
gearBlockAnimation = [pygame.image.load("assets/gearblock0.png").convert_alpha(), pygame.image.load("assets/gearblock1.png").convert_alpha()]
NumFont = [pygame.image.load("assets/Num 0.png").convert_alpha(), pygame.image.load("assets/Num 1.png").convert_alpha(), pygame.image.load("assets/Num 2.png").convert_alpha(), pygame.image.load("assets/Num 3.png").convert_alpha(), pygame.image.load("assets/Num 4.png").convert_alpha(), pygame.image.load("assets/Num 5.png").convert_alpha(), pygame.image.load("assets/Num 6.png").convert_alpha(), pygame.image.load("assets/Num 7.png").convert_alpha(), pygame.image.load("assets/Num 8.png").convert_alpha(), pygame.image.load("assets/Num 9.png").convert_alpha()]
leafAnimation = [pygame.image.load("assets/leaf0.png").convert_alpha(), pygame.image.load("assets/leaf1.png").convert_alpha(), pygame.image.load("assets/leaf2.png").convert_alpha(), pygame.image.load("assets/beanstalkleaf0.png").convert_alpha(), pygame.image.load("assets/beanstalkleaf1.png").convert_alpha(), pygame.image.load("assets/beanstalkleaf2.png").convert_alpha()]
jigsawAnimation = [pygame.image.load("assets/jigsaw0.png").convert_alpha(), pygame.image.load("assets/jigsaw1.png").convert_alpha(), pygame.image.load("assets/jigsaw2.png").convert_alpha(), pygame.image.load("assets/jigsaw3.png").convert_alpha()]
flowerAnimation2 = [pygame.image.load("assets/flower4.png").convert_alpha(), pygame.image.load("assets/flower5.png").convert_alpha()]
stoneBlockAnimation = [pygame.image.load("assets/stoneblock0.png").convert_alpha(), pygame.image.load("assets/stoneblock1.png").convert_alpha(), pygame.image.load("assets/stoneblock2.png").convert_alpha(), pygame.image.load("assets/stoneblock3.png.png").convert_alpha()]
jigsawAnimation = [pygame.image.load("assets/jigsaw0.png").convert_alpha(), pygame.image.load("assets/jigsaw1.png").convert_alpha(), pygame.image.load("assets/jigsaw2.png").convert_alpha(), pygame.image.load("assets/jigsaw3.png").convert_alpha(),]
yellowBlockAnimation = [pygame.image.load("assets/yellowblock0.png").convert_alpha(), pygame.image.load("assets/yellowblock1.png").convert_alpha(), pygame.image.load("assets/yellowblock2.png").convert_alpha()]
beanStalkAnimation = [pygame.image.load("assets/beanstalk.png").convert_alpha()]
fruitBlockAnimation = [pygame.image.load("assets/fruitblock.png").convert_alpha()]
stageEaterAnimation = [pygame.image.load("assets/stageeater0.png").convert_alpha(), pygame.image.load("assets/stageeater1.png").convert_alpha()]
particalAnimation = [pygame.image.load("assets/particle0.png").convert_alpha(), pygame.image.load("assets/particle1.png").convert_alpha(), pygame.image.load("assets/particle2.png").convert_alpha(), pygame.image.load("assets/particle3.png").convert_alpha(), pygame.image.load("assets/beanstalk TL5.png").convert_alpha()]
froggoDeathAnimation = pygame.image.load("assets/froggy hurt.png").convert_alpha()
portalAnimation = [pygame.image.load("assets/portal0.png").convert_alpha(), pygame.image.load("assets/portal1.png").convert_alpha(), pygame.image.load("assets/portal2.png").convert_alpha(), pygame.image.load("assets/portal3.png").convert_alpha(), pygame.image.load("assets/portal4.png").convert_alpha()]

cloudBG = pygame.image.load("assets/background1.png").convert()
castleBG = pygame.image.load("assets/background2.png").convert()
skyBG = pygame.image.load("assets/background3.png").convert()
plainsBG = pygame.image.load("assets/background4.png").convert()
forestBG = pygame.image.load("assets/background5.png").convert()
tallForestBG = pygame.image.load("assets/background6.png").convert()
autumnBG = pygame.image.load("assets/background8.png").convert()
ruinsBG = pygame.image.load("assets/background7.png").convert()
titleBG = pygame.image.load("assets/Title.png").convert_alpha()

theendBG = pygame.image.load("assets/The end.png").convert_alpha()
magicalorb_bg = pygame.image.load("assets/magicalorb.png").convert_alpha()


def onScreen(self):
    return self.fx > -32 and self.fx < screenWidth and self.y > -32 and self.y < screenWidth
def ATouchingB(A, B):
    if A.Type == "frog" or A.Type == "Tongue":
        return A.x + A.width >= B.fx and A.x <= B.fx + B.width and A.y + A.height >= B.y and A.y <= B.y + B.width
    else:
        return A.fx + A.width >= B.fx and A.fx <= B.fx + B.width and A.y + A.height >= B.y and A.y <= B.y + B.width
    
class Frog():
    def __init__(self, x, y):
        self.x = x + 2
        self.y = y
        self.fx = x
        self.width = 28
        self.height = 28
        self.Type = "frog"
        self.speed = 2
        self.animation = 1
        self.legAnimation = 0
        self.Yspeed = 0
        self.walking = False
        self.onGround = False
        self.faceRight = True
        self.mouthOpen = False
        self.leftSolid = False
        self.rightSolid = False
        self.mouth = []
    def update(self):
        global cameraX
        global coinCount
        global spaceKeyCoolDown
        global alive
        window.blit(legAnimation[self.legAnimation], (self.x - 2, self.y -2))
        window.blit(frogAnimation[self.animation], (self.x - 2, self.y -2))
        self.y += self.Yspeed
        if self.Yspeed < 16 and timer % 4 == 0:        # Gravity
            self.Yspeed += 2
            
        if self.x > screenWidth // 2 and cameraX < levelLength - screenWidth + 32:
            cameraX += self.x - screenWidth // 2
            self.x = screenWidth // 2
        if self.x < screenWidth // 2 and cameraX > 0:  # Camera movement
            cameraX += self.x - screenWidth // 2
            self.x = screenWidth // 2
        if cameraX < 0:
            cameraX = 0
        if cameraX > levelLength - screenWidth + 32:
            cameraX = levelLength - screenWidth + 32

        if self.onGround:
            if self.walking:
                if timer % 4 == 0:
                    self.legAnimation += 1
                if self.legAnimation < 1 or self.legAnimation > 2:  # Walking animation
                    self.legAnimation = 1
            elif not timer & 4 == 0:
                self.legAnimation = 0
        else:
            self.legAnimation = 3
            
        if self.y > screenHeight: # Fall in a pit and die
            alive = False
            pygame.mixer.Sound.play(crack)
        if self.onGround:
            if keys[pygame.K_LSHIFT]:
                self.speed = 3
            else:
                self.speed = 2
    def detectEnemy(self, E):
        global alive
        if self.x <= E.fx + E.width and self.x + self.width >= E.fx and self.y <= E.y + E.height and self.y + self.height >= E.y:
            if self in level:
                FroggoDeath = froggoDeath(self.x + cameraX, self.y)
                level.append(FroggoDeath)
                Pop = pop(self.x + cameraX, self.y)
                level.append(Pop)
                level.remove(self)
                if Tongue in level:
                    level.remove(Tongue)
                del self
            
class tongue():
    def __init__(self, x, y, Xspeed):
        self.x = x
        self.y = y
        self.distance = 0
        self.Xspeed = Xspeed
        self.width = 32
        self.height = 24
        self.Type = "tongue"
    def update(self):
        global spaceKeyCoolDown
        pygame.draw.rect(window, (255, 0, 0), (frog.x + frog.width // 2, self.y + 12, self.x - frog.x, 4))
        window.blit(tongueTexture, (self.x, self.y - 2))
        self.y = frog.y
        if self.distance > 0:
            self.Xspeed -= 1
        elif self.distance < 0:
            self.Xspeed += 1
        self.distance += self.Xspeed
        self.x = frog.x + self.distance
        if self.x - frog.x == 0 and spaceKeyCoolDown % 4 == 0:
            spaceKeyCoolDown = 12
            level.remove(self)
            frog.mouthOpen = False
    def tongueDetect(self, A):
        if len(frog.mouth) == 0 or (len(frog.mouth) == 1 and frog.mouth[0] == A):
            if self.x + self.width >= A.fx and self.x <= A.fx + A.width and self.y + self.height >= A.y and self.y <= A.y + A.width and A.Type not in notEdibleObj:
                if len(frog.mouth) == 0 and abs(self.x - frog.x) >= 12:
                    frog.mouth.append(A)
                if abs(self.x - frog.x) <= 16:
                    if len(frog.mouth) == 1 and spaceKeyCoolDown == 0:
                        level.remove(A)
                if len(frog.mouth) != 0:
                    if frog.mouth[0] == A: 
                            A.x = self.x + cameraX
                            A.y = self.y
        if A.Type in notEdibleObj:
            if self.x + self.width >= A.fx and self.x <= A.fx + A.width and self.y + self.height >= A.y and self.y <= A.y + A.width:
                A.touchingTongue = True
            else:
                A.touchingTongue = False
        else:
            if self.x + self.width >= A.fx and self.x <= A.fx + A.width and self.y + self.height >= A.y and self.y <= A.y + A.width and len(frog.mouth) == 1 and frog.mouth[0] == A:
                A.touchingTongue = True
            else:
                A.touchingTongue = False
                
class froggoDeath():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 0
        self.height = 0
        self.Type = "froggyhurt"
        self.Yspeed = -8
        pygame.mixer.Sound.play(crack)
    def update(self):
        global alive
        window.blit(froggoDeathAnimation, (self.fx, self.y))
        if levelProgress != 7:
            self.x += 2
            self.y += self.Yspeed
            if timer % 4 == 0:
                self.Yspeed += 2
            if self.y > screenHeight:
                alive = False
        
class pop():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.Type = "pop"
        self.animation = 0
        self.width = 0
        self.height = 0
    def update(self):
        window.blit(popAnimation[self.animation], (self.fx, self.y))
        if timer % 6 == 0:
            self.animation += 1
        if self.animation > 3:
            level.remove(self)
            del self

class particle():
    def __init__(self, x, y, Dir, mat):
        if Dir == "TL" or Dir == "BL":
            self.x = x
            self.fx = x
        else:
            self.x = x + 16
            self.fx = x + 16
        if Dir == "TL" or Dir == "TR":
            self.y = y
        else:
            self.y = y + 16
        self.width = 0
        self.height = 0
        self.Type = "particle"
        self.dir = Dir
        self.mat = mat
        if Dir == "TL" or Dir == "TR":
            self.Yspeed = -8
        if Dir == "BL" or Dir == "BR":
            self.Yspeed = -4
        if Dir == "TL" or Dir == "BL":
            self.Xspeed = -1
        if Dir == "TR" or Dir == "BR":
            self.Xspeed = 1
    def update(self):
        window.blit(particalAnimation[self.mat], (self.fx, self.y))
        self.y += self.Yspeed
        self.x += self.Xspeed
        if timer % 4 == 0:
            self.Yspeed += 2
        if self.Yspeed > 8:
            level.remove(self)

class coin():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 32
        self.animation = 0
        self.Type = "coin"
        self.touchingTongue = False
    def update(self):
        global coinCount
        window.blit(coinAnimation[self.animation], (self.fx, self.y))
        if timer % 4 == 0:
            self.animation += 1
            if self.animation >= 6:
                self.animation = 0
        if frog.x + frog.width >= self.fx and frog.x <= self.fx + self.width and frog.y + frog.height >= self.y and frog.y <= self.y + self.width:
            coinCount += 1
            level.remove(self)
            pygame.mixer.Sound.play(coinCollect)
            del self
class jigsaw():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 32
        self.animation = 0
        self.Type = "jigsaw"
    def update(self):
        global jigsawCount
        window.blit(jigsawAnimation[self.animation], (self.fx, self.y))
        if timer % 60 >= 44 and timer % 4 == 0:
            self.animation += 1
            if self.animation >= 4:
                self.animation = 0
        if frog.x + frog.width >= self.fx and frog.x <= self.fx + self.width and frog.y + frog.height >= self.y and frog.y <= self.y + self.width:
            jigsawCount += 1
            level.remove(self)
            pygame.mixer.Sound.play(jigsawCollect)
            del self
        
class fruit():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 32
        self.Type = "fruit"
        self.animation = 0
        self.touchingTongue = False
    def update(self):
        window.blit(fruitAnimation[self.animation], (self.fx, self.y))
        if Tongue in level:
            Tongue.tongueDetect(self)
        if timer % 8 == 0:
            self.animation += 1
        if self.animation > 3:
            self.animation = 0
class magicalOrb():
    def __init__(self, x ,y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 32
        self.Type = "magicalorb"
        self.animation = 0
        self.touchingTongue = False
        self.onGround = True
        self.Yspeed = 0
    def update(self):
        window.blit(magicalorb_bg, (self.fx, self.y))
        if Tongue in level:
            Tongue.tongueDetect(self)
        self.y += self.Yspeed
        if timer % 4 == 0 and self.Yspeed < 16:
            self.Yspeed += 2
        self.onGround = False
        for A in level:
            if not self.touchingTongue:
                if A.Type == "block" or A.Type == "decoBlock" or (A.Type == "fruitblock" and not A.touchingTongue) or (A.Type == "flipblock" and A.flippingTimer == 0) or (A.Type == "greenblock" and A.Solid) or (A.Type == "greenblock" and A.Solid) or A.Type == "platform" or A.Type == "invisibleblock" or (A.Type == "ironblock" and A.Solid):
                    if self.x < A.x + A.width and self.x + self.width > A.x:
                        if self.y + self.height > A.y and self.y < A.y:
                            self.Yspeed = 0
                            self.y = A.y - self.height
                        if self.y + self.height == A.y:
                            self.onGround = True
                    if self.y < A.y + A.height and self.y + self.height > A.y and A.Type != "platform":
                        if self.x < A.x and self.x + self.width > A.x:
                            self.x = A.x - self.width
                        if self.x < A.x + A.width and self.x + self.width > A.x + A.width:
                            self.x = A.x + A.width
class jim():
    def __init__(self, x ,y , helmet):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 32
        self.Type = "jim"
        self.animation = 0
        self.touchingTongue = False
        self.onGround = True
        self.Yspeed = 0
        self.helmet = helmet
    def update(self):
        if self.helmet:
            window.blit(spikeJimAnimation[self.animation], (self.fx, self.y))
        else:
            window.blit(jimAnimation[self.animation], (self.fx, self.y))
        if Tongue in level:
            Tongue.tongueDetect(self)
        if not self.touchingTongue:
            frog.detectEnemy(self)
        self.y += self.Yspeed
        if timer % 4 == 0 and self.Yspeed < 16:
            self.Yspeed += 2
        self.onGround = False
        if not self.touchingTongue:
            for A in level:
                if A.Type == "block" or A.Type == "decoBlock" or (A.Type == "fruitblock" and not A.touchingTongue) or (A.Type == "flipblock" and A.flippingTimer == 0) or (A.Type == "greenblock" and A.Solid) or (A.Type == "stoneblock" and A.Solid) or (A.Type == "yellowblock" and A.alive) or A.Type == "platform" or A.Type == "invisibleblock":
                    if self.x < A.x + A.width and self.x + self.width > A.x:
                        if self.y + self.height > A.y and self.y < A.y:
                            self.Yspeed = 0
                            self.y = A.y - self.height
                        if self.y + self.height == A.y:
                            self.onGround = True
                    if self.y < A.y + A.height and self.y + self.height > A.y and A.Type != "platform":
                        if self.x < A.x and self.x + self.width > A.x:
                            self.x = A.x - self.width
                        if self.x < A.x + A.width and self.x + self.width > A.x + A.width:
                            self.x = A.x + A.width
                if self.x < A.x + A.width and self.x + self.width > A.x and self.y < A.y + A.height and self.y > A.y and ((A.Type == "greenblock" and not A.Solid) or (A.Type == "stoneblock" and not A.Solid)):
                    if A.Yspeed > 0:
                            Pop = pop(self.x, self.y)
                            pygame.mixer.Sound.play(crack)
                            level.append(Pop)
                            level.remove(self)
        if timer % 128 == 0 and self.onGround:
            self.Yspeed = -8
        if self.onGround:
            self.animation = 0
        else:
            self.animation = 1
class spinJim():
    def __init__(self, x, y):
        self.x = x + 8
        self.y = y + 2
        self.fx = x
        self.width = 16
        self.height = 28
        self.Type = "spinjim"
        self.animation = 0
        self.touchingTongue = False
        self.faceRight = False
        self.Xspeed = -2
        self.Yspeed = 0
        self.onGround = True
    def update(self):
        window.blit(spinJimAnimation[self.animation], (self.fx - 8, self.y - 2))
        if timer % 4 == 0:
            self.animation += 1
        if self.animation > 3:
            self.animation = 0
            
        if Tongue in level:
            Tongue.tongueDetect(self)
        if not self.touchingTongue:
            frog.detectEnemy(self)
        self.y += self.Yspeed
        self.x += self.Xspeed
        if self.faceRight:
            self.Xspeed = 2
        else:
            self.Xspeed = -2
        if timer % 4 == 0 and self.Yspeed < 16:
            self.Yspeed += 2
        self.onGround = False
        if not self.touchingTongue:
            for A in level:
                if A.Type == "block" or A.Type == "decoBlock" or (A.Type == "fruitblock" and not A.touchingTongue) or (A.Type == "flipblock" and A.flippingTimer == 0) or (A.Type == "greenblock" and A.Solid) or (A.Type == "stoneblock" and A.Solid) or (A.Type == "yellowblock" and A.alive) or A.Type == "platform" or A.Type == "invisibleblock" or (A.Type == "ironblock" and A.Solid):
                    if self.x < A.x + A.width and self.x + self.width > A.x:
                        if self.y + self.height > A.y and self.y + 16 < A.y:
                            self.Yspeed = 0
                            self.y = A.y - self.height
                        if self.y + self.height == A.y:
                            self.onGround = True
                    if self.y < A.y + A.height and self.y + self.height > A.y and A.Type != "platform":
                        if self.x < A.x and self.x + self.width > A.x:
                            self.x = A.x - self.width - 2
                            self.faceRight = False
                            if A.Type == "flipblock":
                                A.flippingTimer = 32
                                pygame.mixer.Sound.play(blockSound)
                            elif A.Type == "yellowblock":
                                A.alive = False
                                pygame.mixer.Sound.play(crack)
                        if self.x < A.x + A.width and self.x + self.width > A.x + A.width:
                            self.x = A.x + A.width + 2
                            self.faceRight = True
                            if A.Type == "flipblock":
                                A.flippingTimer = 32
                                pygame.mixer.Sound.play(blockSound)
                            elif A.Type == "yellowblock":
                                A.alive = False
                                pygame.mixer.Sound.play(crack)
                if self.x < A.x + A.width and self.x + self.width > A.x and self.y < A.y + A.height and self.y > A.y and ((A.Type == "greenblock" and not A.Solid) or (A.Type == "stoneblock" and not A.Solid)):
                    if A.Yspeed > 0:
                            Pop = pop(self.x, self.y)
                            pygame.mixer.Sound.play(crack)
                            level.append(Pop)
                            level.remove(self)
class flower():
    def __init__(self, x ,y ,manualSpin):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 32
        self.Type = "flower"
        self.animation = 0
        self.manualSpin = manualSpin
        self.touchingTongue = False
        self.spinTimer = 0
    def update(self):
        window.blit(flowerAnimation[self.animation], (self.fx, self.y))
        self.animation = timer % 2
        if self.manualSpin:
            if self.spinTimer > 0:
                self.animation += 2
            else:
                self.animation = 2
        if Tongue in level:
            Tongue.tongueDetect(self)
            if self.touchingTongue and self.spinTimer == 0:
                self.spinTimer = 60
        if self.spinTimer > 0 and timer % 4 == 0:
            self.spinTimer -= 1
        if frog.x + frog.width > self.fx and frog.x < self.fx + self.width and frog.y < self.y and frog.y > self.y - 144:
            if self.manualSpin:
                if self.spinTimer > 0:
                    frog.Yspeed = -1
            else:
                frog.Yspeed = -1

class stageEater():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 32
        self.Type = "stageeater"
        self.animation = 0
    def update(self):
        window.blit(stageEaterAnimation[self.animation], (self.fx, self.y))
        if timer % 4 == 0:
            self.animation += 1
        if self.animation > 1:
            self.animation = 0
        if self.fx <= screenWidth:
            self.x -= 2
        frog.detectEnemy(self)
        for A in level:
            if self.x == A.x and self.y == A.y and A.Type != "frog" and A.Type != "stageeater" and A.Type != "particle":
                if A.Type == "block" or A.Type == "greenblock" or A.Type == "decoBlock":
                    Particle = particle(A.x, A.y, "TL", 2)
                    level.append(Particle)
                    Particle = particle(A.x, A.y, "TR", 2)
                    level.append(Particle)
                    Particle = particle(A.x, A.y, "BL", 2)
                    level.append(Particle)
                    Particle = particle(A.x, A.y, "BR", 2)
                    level.append(Particle)
                elif A.Type == "flipblock" or A.Type == "platform":
                    Particle = particle(A.x, A.y, "TL", 0)
                    level.append(Particle)
                    Particle = particle(A.x, A.y, "TR", 0)
                    level.append(Particle)
                    Particle = particle(A.x, A.y, "BL", 0)
                    level.append(Particle)
                    Particle = particle(A.x, A.y, "BR", 0)
                    level.append(Particle)
                elif A.Type == "yellowblock":
                    if theme == 5:
                        Particle = particle(A.x, A.y, "TL", 1)
                        level.append(Particle)
                        Particle = particle(A.x, A.y, "TR", 1)
                        level.append(Particle)
                        Particle = particle(A.x, A.y, "BL", 1)
                        level.append(Particle)
                        Particle = particle(A.x, A.y, "BR", 1)
                        level.append(Particle)
                    else:
                        Particle = particle(A.x, A.y, "TL", 3)
                        level.append(Particle)
                        Particle = particle(A.x, A.y, "TR", 3)
                        level.append(Particle)
                        Particle = particle(A.x, A.y, "BL", 3)
                        level.append(Particle)
                        Particle = particle(A.x, A.y, "BR", 3)
                        level.append(Particle)
                else:
                    Pop = pop(A.x, A.y)
                    level.insert(0, Pop)
                pygame.mixer.Sound.play(crack)
                level.remove(A)
        
def tileCollisionDetect(self):
    if self.fx < frog.x + frog.width and self.fx + self.width > frog.x:
        if self.y < frog.y + frog.height + frog.Yspeed and self.y > frog.y:   #top collided
            frog.Yspeed = 2
            frog.y -= frog.Yspeed
            frog.onGround = True
        elif self.y + self.height > frog.y - frog.Yspeed and self.y < frog.y:   #bottom collided
            frog.Yspeed = 0
            if frog.y - 4 > self.y:
                frog.y = self.y + self.height + 2
            if self.Type == "beanstalk":
                self.Solid = False
                Particle = particle(self.x, self.y, "TL", 4)
                level.append(Particle)
                Particle = particle(self.x, self.y, "TR", 4)
                level.append(Particle)
                Particle = particle(self.x, self.y, "BL", 4)
                level.append(Particle)
                Particle = particle(self.x, self.y, "BR", 4)
                level.append(Particle)
                level.remove(self)
                pygame.mixer.Sound.play(crack)
                
    if self.y < frog.y + frog.height and self.y + self.height > frog.y:
        if self.fx < frog.x + frog.width + frog.speed and self.fx >= frog.x:    #left collided
            frog.x -= frog.speed
        elif self.fx + self.width > frog.x - frog.speed and self.fx <= frog.x:    #right collided
            if self.Type == "block":
                if self.LeftSolid or (not self.LeftSolid and not self.RightSolid):
                    frog.x += frog.speed
            else:
                frog.x += frog.speed
        if frog.x - 2 == self.fx + self.width:
            frog.leftSolid = True
        elif frog.x + 2 == self.fx - frog.width:
            frog.rightSolid = True

class platform:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 2
        self.Type = "platform"
    def update(self):
        window.blit(platformSprite, (self.fx, self.y))
        if self.fx < frog.x + frog.width and self.fx + self.width > frog.x and self.y < frog.y + frog.height + frog.Yspeed and self.y > frog.y and frog.Yspeed >= 0:
            frog.Yspeed = 2
            frog.y -= frog.Yspeed
            frog.onGround = True 

class fruitBlock():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 32
        self.Type = "fruitblock"
        self.animation = 0
        self.touchingTongue = False
    def update(self):
        window.blit(fruitBlockAnimation[0], (self.fx, self.y))
        if Tongue in level:
            Tongue.tongueDetect(self)
        if not self.touchingTongue:
            tileCollisionDetect(self)
            
class greenBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 32
        self.Yspeed = 0
        self.Xspeed = 0
        self.Type = "greenblock"
        self.touchingTongue = False
        self.Solid = True
        self.animation = 0
        self.onGround = False
    def update(self):
        if self.Solid:
            self.animation = 0
        else:
            self.animation = 1
        window.blit(greenBlockAnimation[self.animation], (self.fx, self.y))
        
        if Tongue in level:
            Tongue.tongueDetect(self)
            if self.touchingTongue:
                self.Solid = False
        if self.Solid:
            tileCollisionDetect(self)
        elif not self.touchingTongue:
            self.y += self.Yspeed
            if self.Yspeed < 16 and timer % 4 == 0:
                self.Yspeed += 2     
            for A in level:
                if A.Type == "block" or A.Type == "decoBlock" or (A.Type == "fruitblock" and not A.touchinTongue) or (A.Type == "flipblock" and A.flippingTimer == 0) or (A.Type == "greenblock" and A.Solid) or (A.Type == "stoneblock" and A.Solid) or A.Type == "platform" or A.Type == "invisibleblock" or (A.Type == "ironblock" and A.Solid):
                    if self.x < A.x + A.width and self.x + self.width > A.x:
                        if self.y + self.height > A.y and self.y < A.y:
                            self.Yspeed = 0
                            self.y = A.y - self.height
                            self.Solid = True
                    if self.y < A.y + A.height and self.y + self.height > A.y and A.Type != "platform":
                        if self.x < A.x and self.x + self.width > A.x:
                            self.x = A.x - self.width
                        if self.x < A.x + A.width and self.x + self.width > A.x + A.width:
                            self.x = A.x + A.width
class stoneBlock:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 32
        self.Yspeed = 0
        self.Xspeed = 0
        self.Type = "stoneblock"
        self.touchingTongue = False
        self.Solid = True
        self.animation = 0
        self.onGround = False
        self.alive = True
        self.timer = 0
    def update(self):
        if self.alive:
            if self.Solid:
                if timer % 50 > 25:
                    self.animation = 0
                else:
                    self.animation = 3
                self.timer = 0
            else:
                self.animation = 1
                self.timer += 1
        else:
            self.animation = 2
            self.timer += 1
            if self.timer > 50:
                level.remove(self)

        window.blit(stoneBlockAnimation[self.animation], (self.fx, self.y))
        
        if Tongue in level and self.alive:
            Tongue.tongueDetect(self)
            if self.touchingTongue:
                self.Solid = False
        if self.Solid and self.alive:
            tileCollisionDetect(self)
        elif not self.touchingTongue:
            self.y += self.Yspeed
            if self.Yspeed < 16 and timer % 4 == 0:
                self.Yspeed += 2
            if self.alive:
                for A in level:
                    if A.Type == "block" or A.Type == "decoBlock" or (A.Type == "fruitblock" and not A.touchinTongue) or (A.Type == "flipblock" and A.flippingTimer == 0) or (A.Type == "greenblock" and A.Solid) or (A.Type == "stoneblock" and A.Solid) or A.Type == "platform" or A.Type == "invisibleblock" or (A.Type == "ironblock" and A.Solid):
                        if self.x < A.x + A.width and self.x + self.width > A.x:
                            if self.y + self.height > A.y and self.y < A.y:
                                self.Yspeed = 0
                                self.y = A.y - self.height
                                self.Solid = True
                                if self.timer > 30:
                                    self.alive = False
                                    pygame.mixer.Sound.play(crack)
                        if self.y < A.y + A.height and self.y + self.height > A.y and A.Type != "platform":
                            if self.x < A.x and self.x + self.width > A.x:
                                self.x = A.x - self.width
                            if self.x < A.x + A.width and self.x + self.width > A.x + A.width:
                                self.x = A.x + A.width
        
class ironBlock():
    def __init__(self, x, y, Solid):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 32
        self.Type = "ironblock"
        self.Solid = Solid
    def update(self):
        if self.Solid:
            window.blit(ironBlockAnimation[0], (self.fx, self.y))
            tileCollisionDetect(self)
        else:
            window.blit(ironBlockAnimation[1], (self.fx, self.y))
        if ATouchingB(self, frog) and frog.y < self.y:
            for A in level:
                if A.Type == "gearblock" and not A.activated:
                    A.activated = True

class gearBlock():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 32
        self.Type = "gearblock"
        self.animation = 0
        self.dir = "right"
        self.dirChanged = False
        self.activated = False
    def update(self):
        self.dirChanged = False
        window.blit(gearBlockAnimation[self.animation], (self.fx, self.y))
        if self.activated:
            if timer % 5 == 0:
                self.animation = timer % 2

            if self.dir == "right":
                self.x += 1
            elif self.dir == "left":
                self.x -= 1
            elif self.dir == "up":
                self.y -= 1
            elif self.dir == "down":
                self.y += 1
        for A in level:
            if A.Type == "ironblock":
                if self.x == A.x:
                    if self.y == A.y - 32 and self.dir != "up" and self.dirChanged == False:
                        self.dir = "down"
                        self.dirChanged = True
                    if self.y == A.y + 32 and self.dir != "down" and self.dirChanged == False:
                        self.dir = "up"
                        self.dirChanged = True
                elif self.y == A.y:
                    if self.x == A.x - 32 and self.dir != "left" and self.dirChanged == False:
                        self.dir = "right"
                        self.dirChanged = True
                    if self.x == A.x + 32 and self.dir != "right" and self.dirChanged == False:
                        self.dir = "left"
                        self.dirChanged = True
                if self.x == A.x and self.y == A.y:
                    if A.Solid == True:
                        A.Solid = False
                    else:
                        A.Solid = True
        if frog.x < self.fx + self.width and frog.x + frog.width > self.fx:
            if frog.y + frog.height > self.y and frog.y < self.y + self.height and self.dir == "up":
                frog.y = self.y - frog.height
                frog.onGround = True
        if ATouchingB(self, frog) and not self.activated:
            for A in level:
                if A.Type == "gearblock":
                    A.activated = True
        tileCollisionDetect(self)
        
class flipBlock():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 32
        self.Type = "flipblock"
        self.animation = 0
        self.touchingTongue = False
        self.flippingTimer = 0
    def update(self):
        window.blit(flipBlockAnimation[self.animation], (self.fx, self.y))

        if Tongue in level:
            Tongue.tongueDetect(self)
            
        if self.touchingTongue and self.flippingTimer == 0 and Tongue in level:
            self.flippingTimer = 64
            pygame.mixer.Sound.play(blockSound)
        if self.flippingTimer > 0 and timer % 4 == 0:
            self.flippingTimer -= 1
            self.animation = self.flippingTimer % 6
        elif self.flippingTimer <= 0:
            self.animation = 0
            tileCollisionDetect(self)
class invisibleBlock():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 32
        self.Type = "invisibleblock"
    def update(self):
        if len(frog.mouth) == 1 and frog.mouth[0].Type == "magicalorb":
            tileCollisionDetect(self)
            window.blit(invisibleBlockAnimation[1], (self.fx, self.y))
        else:
            if theme == 4:
                window.blit(invisibleBlockAnimation[2], (self.fx, self.y))
            else:
                window.blit(invisibleBlockAnimation[0], (self.fx, self.y))
class goalSign():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 32
        self.Type = "goalsign"
        self.animation = 0
        self.touchingTongue = False
        self.flippingTimer = 300
        self.goal = False
    def update(self):
        global levelProgress
        global alive
        global coinCountSave
        global jigsawCountSave
        if self.goal:
            window.blit(goalSignFlippingAnimation[self.animation], (self.fx, self.y))
            if timer % 4 == 0:
                self.animation += 1
                if self.animation > 5:
                    self.animation = 0
        else:
            window.blit(goalSignAnimation[self.animation], (self.fx, self.y))
            if timer % 12 == 0:
                self.animation += 1
                if self.animation > 3:
                    self.animation = 0

        if Tongue in level:
            Tongue.tongueDetect(self)
            
        if self.touchingTongue and self.flippingTimer == 300 and Tongue in level:
            self.goal = True
            pygame.mixer.Sound.play(blockSound)
        if self.flippingTimer == 250:
            pygame.mixer.music.stop()
            pygame.mixer.music.load("audios/Victory.wav")
            pygame.mixer.music.play(0)
        if self.flippingTimer > 0 and self.goal:
            self.flippingTimer -= 1
            self.animation = self.flippingTimer % 6
        if self.flippingTimer == 0:
            levelProgress += 1
            coinCountSave = coinCount
            jigsawCountSave = jigsawCount
            alive = False
class leaf():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.Type = "leaf"
        self.animation = random.randrange(0, 3)
        self.width = 0
        self.height = 0
        self.downSpeed = 1
        self.leftSpeed = 1
        self.green = False
        self.fall = False
    def update(self):
        if self.green:
            window.blit(leafAnimation[self.animation + 3], (self.fx, self.y))
        else:
            window.blit(leafAnimation[self.animation], (self.fx, self.y))
        self.x -= self.leftSpeed
        self.y += self.downSpeed
        if not self.green:
            if self.y > screenWidth:
                self.y = -32
            if self.fx < -32:
                self.x += 512
            if self.fx > screenWidth:
                self.x -= 512
            if timer % 4 == random.randrange(0, 20):
                if self.downSpeed == 1:
                    self.downSpeed = 2
                else:
                    self.downSpeed = 1
                self.animation = random.randrange(0, 3)
            if timer % 4 == random.randrange(0, 20):
                if self.leftSpeed == 1:
                    self.leftSpeed = 2
                else:
                    self.leftSpeed = 1
                self.animation = random.randrange(0, 3)
        elif timer % random.randrange(1, 1000) == 0 and self.fall:
            self.downSpeed = 1
            self.leftSpeed = 1
            
       
class block():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 32
        self.Type = "block"
        self.tile = [0,5,10,15]
        self.TopLeftSolid = False
        self.TopSolid = False
        self.TopRightSolid = False
        self.LeftSolid = False
        self.RightSolid = False
        self.BottomLeftSolid = False
        self.BottomSolid = False
        self.BottomRightSolid = False
                 
    def update(self):
        window.blit(tiles[theme][self.tile[0]], (self.fx, self.y))
        window.blit(tiles[theme][self.tile[1]], (self.fx, self.y + self.height // 2))
        window.blit(tiles[theme][self.tile[2]], (self.fx + self.width // 2, self.y))
        window.blit(tiles[theme][self.tile[3]], (self.fx + self.width // 2, self.y + self.height // 2))
        
        tileCollisionDetect(self)

    def connect(self):
        self.tile = [0,5,10,15]
        for N in level:
            if N.Type == "block" or N.Type == "decoBlock":
                if N.x == self.x - self.width and N.y == self.y - self.height:
                    self.TopLeftSolid = True
                if N.x == self.x              and N.y == self.y - self.height:
                    self.TopSolid = True
                if N.x == self.x + self.width and N.y == self.y - self.height:
                    self.TopRightSolid = True
                if N.x == self.x - self.width and N.y == self.y:
                    self.LeftSolid = True
                if N.x == self.x + self.width and N.y == self.y:
                    self.RightSolid = True
                if N.x == self.x - self.width and N.y == self.y + self.height:
                    self.BottomLeftSolid = True
                if N.x == self.x              and N.y == self.y + self.height:
                    self.BottomSolid = True
                if N.x == self.x + self.width and N.y == self.y + self.height:
                    self.BottomRightSolid = True
                if self.x == 0:
                    self.LeftSolid = True
                    if self.TopSolid:
                        self.TopLeftSolid = True
                    if self.BottomSolid:
                        self.BottomLeftSolid = True
                if self.y == screenHeight - self.height:
                    self.BottomSolid = True
                    if self.LeftSolid:
                        self.BottomLeftSolid = True
                    if self.RightSolid:
                        self.BottomRightSolid = True
        if self.TopSolid:         # self.tile[topleft, bottomleft, topright, buttomright]
            self.tile[0] += 2
            self.tile[2] += 2  # self.tile[0]    self.tile[2]
        if self.LeftSolid:     #
            self.tile[0] += 1  # self.tile[1]    self.tile[3]
            self.tile[1] += 1
        if self.BottomSolid:
            self.tile[1] += 2
            self.tile[3] += 2
        if self.RightSolid:
            self.tile[2] += 1
            self.tile[3] += 1
        if self.tile[0] == 3 and self.TopLeftSolid:
            self.tile[0] += 1
        if self.tile[1] == 8 and self.BottomLeftSolid:
            self.tile[1] += 1
        if self.tile[2] == 13 and self.TopRightSolid:
            self.tile[2] += 1
        if self.tile[3] == 18 and self.BottomRightSolid:
            self.tile[3] += 1
            
class decoBlock():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 32
        self.Type = "decoBlock"
    def update(self):
        window.blit(tile2[theme], (self.fx, self.y))
        tileCollisionDetect(self)
        
class beanstalk():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 32
        self.Type = "beanstalk"
        self.tile = [0,5,10,15]
        self.TopSolid = False
        self.LeftSolid = False
        self.RightSolid = False
        self.BottomSolid = False
        self.Solid = False
        self.connected = False
                 
    def update(self):
        if self.Solid:
            window.blit(beanstalktile[self.tile[0]], (self.fx, self.y))
            window.blit(beanstalktile[self.tile[1]], (self.fx, self.y + self.height // 2))
            window.blit(beanstalktile[self.tile[2]], (self.fx + self.width // 2, self.y))
            window.blit(beanstalktile[self.tile[3]], (self.fx + self.width // 2, self.y + self.height // 2))
                    
            tileCollisionDetect(self)

    def connect(self):
        self.connected = True
        self.tile = [0,5,10,15]
        self.TopSolid = False
        self.LeftSolid = False
        self.RightSolid = False
        self.BottomSolid = False
        for N in level:
            if N.Type == "beanstalk":
                if N.x == self.x              and N.y == self.y - self.height:
                    self.TopSolid = True
                if N.x == self.x - self.width and N.y == self.y:
                    self.LeftSolid = True
                if N.x == self.x + self.width and N.y == self.y:
                    self.RightSolid = True
                if N.x == self.x              and N.y == self.y + self.height:
                    self.BottomSolid = True
        if self.TopSolid:         # self.tile[topleft, bottomleft, topright, buttomright]
            self.tile[0] += 2
            self.tile[2] += 2  # self.tile[0]    self.tile[2]
        if self.LeftSolid:     #
            self.tile[0] += 1  # self.tile[1]    self.tile[3]
            self.tile[1] += 1
        if self.BottomSolid:
            self.tile[1] += 2
            self.tile[3] += 2
        if self.RightSolid:
            self.tile[2] += 1
            self.tile[3] += 1
            
class beanstalktip():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 32
        self.Type = "beanstalktip"
        self.animation = 0
        self.dir = "up"
        self.dirChanged = False
        self.touchingTongue = False
        self.watered = False
    def update(self):
        self.dirChanged = False
        if self.watered:
            window.blit(flowerAnimation2[self.animation], (self.fx, self.y))
        else:
            window.blit(beanStalkAnimation[0], (self.fx, self.y))
        if Tongue in level and not self.watered:
            Tongue.tongueDetect(self)
            if self.touchingTongue:
                self.watered = True
        if timer % 5 == 0:
            self.animation = timer % 2
        if self.watered:
            for A in level:
                if A.Type == "beanstalk" or A.Type == "yellowblock":
                    if self.x == A.x:
                        if self.y == A.y - 32 and self.dir != "up" and self.dirChanged == False:
                            self.dir = "down"
                            self.dirChanged = True
                            if A.Type == "yellowblock":
                                A.alive = False
                                Beanstalk = beanstalk(A.x, A.y)
                                level.insert(0, Beanstalk)
                                Beanstalk.connect()
                        if self.y == A.y + 32 and self.dir != "down" and self.dirChanged == False:
                            self.dir = "up"
                            self.dirChanged = True
                            if A.Type == "yellowblock":
                                A.alive = False
                                Beanstalk = beanstalk(A.x, A.y)
                                level.insert(0, Beanstalk)
                                Beanstalk.connect()
                    elif self.y == A.y:
                        if self.x == A.x - 32 and self.dir != "left" and self.dirChanged == False:
                            self.dir = "right"
                            self.dirChanged = True
                            if A.Type == "yellowblock":
                                A.alive = False
                                Beanstalk = beanstalk(A.x, A.y)
                                level.insert(0, Beanstalk)
                                Beanstalk.connect()
                        if self.x == A.x + 32 and self.dir != "right" and self.dirChanged == False:
                            self.dir = "left"
                            self.dirChanged = True
                            if A.Type == "yellowblock":
                                A.alive = False
                                Beanstalk = beanstalk(A.x, A.y)
                                level.insert(0, Beanstalk)
                                Beanstalk.connect()
                    if self.x == A.x and self.y == A.y:
                        if A.Type == "beanstalk":
                            A.Solid = True
                    if self.fx + self.width > A.fx and self.fx < A.fx + A.width and self.y + self.height > A.y and self.y < A.y + A.width and A.Type == "yellowblock":
                        A.alive = False
                    if A.Type == "beanstalk" and A.Solid and onScreen(A):
                        if abs(A.x - self.x) <= 32 and abs(A.y - self.y) <= 32:
                            A.connect()
            if self.dir == "right":
                self.x += 2
            elif self.dir == "left":
                self.x -= 2
            elif self.dir == "up":
                self.y -= 2
            elif self.dir == "down":
                self.y += 2
            if frog.x < self.fx + self.width and frog.x + frog.width > self.fx:
                if frog.y + frog.height > self.y and frog.y < self.y + self.height and self.dir == "up":
                    frog.y = self.y - frog.height
                    frog.onGround = True
        if (self.y > screenWidth or self.y < -32) and self in level:
            level.remove(self)
            del self
        tileCollisionDetect(self)

class yellowBlock():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 32
        self.height = 32
        self.Type = "yellowblock"
        self.alive = True
        self.timer = 0
    def update(self):
        if self.alive:
            if theme == 5:
                window.blit(yellowBlockAnimation[2], (self.fx, self.y))
            else:
                window.blit(yellowBlockAnimation[0], (self.fx, self.y))
            tileCollisionDetect(self)
        else:
            if theme == 5:
                Particle = particle(self.x, self.y, "TL", 3)
                level.append(Particle)
                Particle = particle(self.x, self.y, "TR", 3)
                level.append(Particle)
                Particle = particle(self.x, self.y, "BL", 3)
                level.append(Particle)
                Particle = particle(self.x, self.y, "BR", 3)
                level.append(Particle)
            else:
                Particle = particle(self.x, self.y, "TL", 1)
                level.append(Particle)
                Particle = particle(self.x, self.y, "TR", 1)
                level.append(Particle)
                Particle = particle(self.x, self.y, "BL", 1)
                level.append(Particle)
                Particle = particle(self.x, self.y, "BR", 1)
                level.append(Particle)
            level.remove(self)
            pygame.mixer.Sound.play(crack)
        for A in level:
            if self.x < A.x + A.width and self.x + self.width > A.x and self.y < A.y + A.height and self.y > A.y and ((A.Type == "greenblock" and not A.Solid) or (A.Type == "stoneblock" and not A.Solid)):
                if A.Yspeed > 0:
                        self.alive = False   
class portal():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 64
        self.height = 80
        self.Type = "portal"
        if levelProgress == 0:
            self.broke = False
            self.animation = 1
        else:
            self.broke = True
            self.animation = 0
    def update(self):
        global levelProgress
        global alive
        global jigsawCount
        if levelProgress == 0:
            if timer > 200 and timer < 220:
                window.blit(portalAnimation[self.animation], (self.fx + random.randrange(-3, 3), self.y + random.randrange(-3, 3)))
            else:
                window.blit(portalAnimation[self.animation], (self.fx, self.y))
            if self.broke:
                self.animation = 0
            else:
                if timer % 16 == 0:
                    self.animation += 1
                    if self.animation == 5:
                        self.animation = 1
            if timer > 100 and frog not in level:
                Pop = pop(frog.x, frog.y)
                level.append(Pop)
                level.append(frog)
            if timer == 200:
                obj = Jigsaw(self.x + 32, self.y + 32)
                level.append(obj)
                obj = Jigsaw(self.x + 64, self.y + 32)
                level.append(obj)
                obj = Jigsaw(self.x + 32, self.y + 64)
                level.append(obj)
                obj = Jigsaw(self.x + 64, self.y + 64)
                level.append(obj)
                obj = Jigsaw(self.x + 32, self.y + 96)
                level.append(obj)
                obj = Jigsaw(self.x + 64, self.y + 96)
                level.append(obj)
                self.broke = True
                pygame.mixer.Sound.play(crack)
            if timer > 400:
                levelProgress += 1
                alive = False
        else:
            if timer > 200 and timer < 220 and jigsawCountSave == 6:
                window.blit(portalAnimation[self.animation], (self.fx + random.randrange(-3, 3), self.y + random.randrange(-3, 3)))
            else:
                window.blit(portalAnimation[self.animation], (self.fx, self.y))
            if self.broke:
                self.animation = 0
            else:
                if timer % 16 == 0:
                    self.animation += 1
                    if self.animation == 5:
                        self.animation = 1
            if timer > 100:
                if jigsawCount > 0 and timer % 10 == 0:
                    jigsawCount -= 1
                    x = (jigsawCount % 2) + 1
                    y = (jigsawCount // 2) + 1
                    obj = Jigsaw(self.x + (32 * x), self.y + (32 * y))
                    level.append(obj)
                    pygame.mixer.Sound.play(jigsawCollect)
            if timer == 220 and jigsawCountSave == 6:
                self.broke = False
                pygame.mixer.Sound.play(crack)
            if timer > 300 and jigsawCountSave == 6:
                if frog in level:
                    if frog.x < self.x + 48:
                        frog.x += 3
                    if frog.y < self.y + 64:
                        frog.Yspeed += 1
                    if frog.x > self.x + 48:
                        frog.x -= 3
                    if frog.y > self.y + 64:
                        frog.Yspeed -= 2
                    if frog.x > self.x + 32 and frog.x < self.x + 64 and frog.y > self.y + 32 and frog.y < self.y + 96:
                        Pop = pop(frog.x, frog.y)
                        level.append(Pop)
                        level.remove(frog)
                        pygame.mixer.Sound(crack)
                if not frog in level:
                    window.blit(theendBG, (24, 32))
            elif timer > 300:
                window.blit(theendBG, (24, 32))
                
class Jigsaw():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fx = x
        self.width = 64
        self.height = 80
        self.Type = "Jigsaw"
        self.animation = 0
        self.Yspeed = 0
        self.Xspeed = random.randrange(-16, 16)
    def update(self):
        window.blit(jigsawAnimation[self.animation], (self.fx, self.y))
        if timer % 60 >= 44:
            if timer % 4 == 0:
                self.animation += 1
                if self.animation >= 4:
                    self.animation = 0
        else:
            self.animation = 0
        if levelProgress == 0:
            if timer > 250:
                self.x += self.Xspeed
                self.y += self.Yspeed
                if timer % 4 == 0:
                    self.Yspeed -= 2
        else:
            if timer > 220 and jigsawCountSave == 6:
                level.remove(self)
                del self
                
coinCount = 0
jigsawCount = 0
coinCountSave = 0
jigsawCountSave = 0
levelLength = 0
level = []
def redrawGameWindow():
        window.blit(BG, (0,0))

        for N in level:
            if N.Type != "frog" and N.Type != "tongue":
                N.fx = N.x - cameraX
                if onScreen(N):
                    N.update()
                elif N.Type == "leaf" or N.Type == "gearblock":
                    N.update()
            else:
                N.update()
            if N.Type == "greenblock" or N.Type == "stoneblock":
                N.onGround = False

        if levelProgress != 0:
            window.blit(coinAnimation[0], (16, 16))
            for N in range(0, len(str(coinCount))):
                window.blit(NumFont[int(str(coinCount)[N])], (40 + N * 16, 32))
            window.blit(jigsawAnimation[0], (16, 48))
            for N in range(0, len(str(jigsawCount))):
                window.blit(NumFont[int(str(jigsawCount)[N])], (40 + N * 16, 64))

        pygame.display.update()


run = True
keys = pygame.key.get_pressed()
while run and not keys[pygame.K_RETURN] and not keys[pygame.K_x]:          #Title screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.blit(skyBG, (0,0))
    window.blit(titleBG, (40, 48))
    keys = pygame.key.get_pressed()
    pygame.display.update()
    
tileObjs = ["f", "P", "@", "G", "-", "i", "g", "=", "I", "!", "+", "*", "%", "&", "Y"]
BG = skyBG
levelProgress = 0
theme = 1
while run:
    level = []
    Clevel = []
    timer = 0
    cameraX = 0
    spaceKeyCoolDown = 0
    fruitCountDown = 0
    coinCount = coinCountSave
    jigsawCount = jigsawCountSave
    run = True
    alive = True
    
    if levelProgress == 0:
        Lvl = ["               ",
               "               ",
               "               ",
               "     o         ",
               "               ",
               "               ",
               "               ",
               "               ",
               "++++++++++++++++",
               "++++++++++++++++",]
        BG = plainsBG
        theme = 0
        music = pygame.mixer.music.load("audios/plains.wav")
    elif levelProgress == 1:
        Lvl = ["                                                   ++++++       $$$          +++++++++++                                     ++++  ++                           ",
               "                                                    *++*        $$$          +*+     +*+                                     ++++  ++                           ",
               "        $$$      $                                   ++         $$$          +*+     +*+                                     ++++  ++                           ",
               "                 $                                   ++         PPP           =  $$$  =                                      ++++  ++    $$$                    ",
               "                 $        $$$$     $$$                        P     P         =       =                            PPPP+++   ++*+                          !    ",
               "        $$$              ======    PPP+++=====+++    $$                       =       =           ===                    *===*+*+                      PPP+++PPP",
               "   F   *+++*     *      ++++++++  $$$ +++     +++   $  $    $$$     $$$       =  $$$  =    *   ++P$$$P+++ === ++     PPPP+ $   =         $$$              +++   ",
               "+++++++++++++PPP+++PPP++++++++++++PPP +++     +++         **PPP     PPP**    +*+PPPPP+*+  +++  ++ $$$ +++P$$$P++         + $   =       *PPPPP=     PPP    +++   ",
               "+++++++++++++   +++   ++++++++++++    +++     +++*       ***    PPP    ***   +*+     +*+  +++  ++++++++++ $$$ ++PPPPPPP+++ $   =      ++  #  ++           +++   ",
               "+++++++++++++   +++   ++++++++++++    +++     +++++++  +++++           +++++++++     +++  +++  +++++++++++++++++       ++++++++*++++++++ +++ +++PPP       +++   "]
        BG = plainsBG
        theme = 0
        music = pygame.mixer.music.load("audios/plains.wav")
    elif levelProgress == 2:
        Lvl = ["    +++++++++                                                                                                                                        *********  ",
               "          ++                                                                                                  ++            +++                $$$    *******   ",
               "          ++       aaa                                           $$    *****                            ***   ++++      +++++++      $$$       ***    a === a   ",
               "          ++      P   P       *****           $          $            *******      j  $$$$       ***   *****  +++++++++++++++++               *****     ===  @@ ",
               "          ++                 *******          $          $            a  =  a      **PPPPPP+    *****  a = a   *@* $ @@@ $+++++               a = a @@  ===PP@@ ",
               "       +==++                 a  =  a                             $$     P=P      j **      ++   a = a    =      @  $ @@@ $ *@@     j $$$ j     P=P  @@PP===     ",
               "       +aa       **PPP**       P=P            j          j      *PP*     =       ****     a++     =      =      @  $ *** $ *@*     **PPP@*      =       ===     ",
               "   F   +aa      ***   ***       =           PPPPP      =PPP=   **  **   P=P      ****     a++     =   j  =     *@* $ *** $ @@*    ***   @**    P=P      ===  !  ",
               "+++++++++++++++++++   +++++    P=P   ++PP+++++++++++PP+++++++++++  ++++++++++++++++++     P++++++++++++++++++++++++++++++++++++++++++ # ++++++++++++++++++++++++",
               "+++++++++++++++++++   +++++++++++++++++  +++++++++++  +++++++++++  ++++++++++++++++++      ++++++++++++++++++++++++++++++++++++++++++PPP++++++++++++++++++++++++"]
        BG = forestBG
        theme = 0
        music = pygame.mixer.music.load("audios/plains.wav")
    elif levelProgress == 3:
        Lvl = ["                              +++++++                                                                                                               ++++++++++++",
               "                                   -*                                                                                                        +      ++          ",
               "                $$$                -*          $$                                          $$$ J $$$                                         +      ++ $$$   !  ",
               "         $$                    ++  ++                                                   ++++++++++++++++                %%%             %%%%%Y%     +Y%%%%%%YYYY",
               "        $           J         +++                               J                     %%YY++********++*                 & %  JJJ        %+++++%     +Y      ++++",
               "              j     P        ++++           -* J  -  J $$       *  $$$               %%  %++        ++      J     ++++++++% PPPPP    %%%%+    %     +Y $$$  ++++",
               "   F      ++++++++++++++++   **** J      +++++++++++++++ $   J= *  ++++++++++       %%   %++        ++     -- J    *****++Y          %+ ++  # %     +YY%%%%%YY++",
               "+++++++++ **++********++** P+++++ +++++  **++********++* ++++++++++******++*        &    %++        ++ ++++++++++       ++%          &+       %             +Y++",
               "*****++**   ++        ++    **++* *++**    ++        ++  *++*******      ++  ++++++++    %++        ++*******++***      ++%  $$$ %%Y+++++++++ Y+++          +&++",
               "     ++     ++        ++      ++   ++      ++        ++   ++             ++ **++***++*   %++        ++       ++         ++%%%%%%%% Y*++***++* Y++* +++++++++++++"]
               #======F======#
        BG = ruinsBG
        theme = 5
        music = pygame.mixer.music.load("audios/golucky.wav")
    elif levelProgress == 4:
        Lvl = ["                                                                                                            ++++++++++      +++++          S++                  ",
               "                                                                                                             *   SY +        +++          ++++ $$$$ +           ",
               "                   $                                                                                         +IIII+ +        +++         P  S+ $$$$ +           ",
               "                   $                                                                                         *               +S+        P  ++++++++++           ",
               "                         $$$                                      **                       P*YYSY*PPPPP+   J *            PPP+++          P  S++             !  ",
               "                   J             G    PP     **    $$           * **                  YS++  ******     +IIIII+               +++         P  +++          +++PPP+",
               "         *III*    ***           ***         +++                ++Y++++++PP+  $$$     Y +++  *    * $$$ *                      +            P           + +     +",
               "  F   P+++$$$+++ +++++ +PPPPP+ +++++    JYY +++             J P++Y  $$$$$$++PPPPP+P Y ++++  *    * $$$ *             ++++     +    *Y Y*  P            +Y    # +",
               "+++++P +++++++++  +++  +    S+ +++++  +++++ +++ J  YY  J   YY  ++Y+++$$$$$++    S+ Y +++++  Y    Y     Y        *****++++     Y  +P  YYY  *** *        +Y+++++++",
               "+++++  +++++++++  +++  +++++++ +++++  +++++ +++ +P++++P+ ++++  +++++++++++++++++++ +++++++II*++++*+++++++++++++++++++++++ ++++++++ ++++++++++ ++++++++++++++++++"]
                #======F======#
        BG = autumnBG
        theme = 4
        music = pygame.mixer.music.load("audios/TheForest.wav")
    elif levelProgress == 5:
        Lvl = ["                                  $$$$$$$           +*+       +*++++*++++*               *                       +                                               ",
               "                                 IIIIIIIII           +++++++++++         +               +                       +                                               ",
               "                                I         I                              +               +$$                    $$$                 $$$   $$$                    ",
               "      $$$                     J                                     +IIII+   $$$  II*    +$$                                   J                              !  ",
               "   a       a                 III                   +++II     II+++PP+    +   III    +IIII+PPP                    +             +                             +++ ",
               "                     $$$              j   ++++++++ +*+         +*+  + $  +          +    +                       +             +                     $$$$  +++*+ ",
               "       F     PP+++PP +++            +++++   ++*+   +m+   III   +m+  +  $        $$$ +    *   PPP    j          iiiii    j  iiiiiiiii1i1i1i111iiiiiii++++++ +*+++ ",
               "   +++++++++   +*+   +*+  ++*+++*++ +*+*+   ++++   +++         +++  + $         III +             +++++    +  ii   ii   +  i   +                   i+*++*+ ++++  ",
               "   ++*+++*++    +     +     ++ ++    +++    +*++   + ++   m   ++ +  +  $     m      +             ++*+g1111giii     ii  +  i   +           #       i ++++   + +  ",
               "     +++++                                   ++    +  +++++++++  +  *++++* *PPP*    *++++++++++++  ++++    +         iiiiiii              III      i        + +  ",]
                                                                                                             #======F======#
        BG = cloudBG
        theme = 6
        music = pygame.mixer.music.load("audios/8bitvictory.wav")
    elif levelProgress == 6:
        Lvl = ["                                                                  + +********+ +  +    s +                       +      s                                        ",
               "                                                                  ***        ***  +  S   +                       +      s          PPPPPP+ $$$                   ",
               "         ++++   s                                                   +             ********  s        $   ++++    +      s              s *******                 ",
               "                                         G                    S     +  *********                    $ PPP   +P $ +               ***** # + s   +         !       ",
               "                           J          $ +++ $                 **    +        + +                   $        + $  +           $$$ +   +   +     +        *** *YY* ",
               "                ++        ***         $*****$               S***    +   S +  + +                            +  $ +          +++++   s+ $ +     +        + + +$$+ ",
               "        $$  $$  ++        + +         $+   +$               ****    *******  + +             $$   *** *** s + $        $$$           + $ +     +    *** + +s+$$+ ",
               "   F    ++  ++  ++ J  $ $ + +    J   ***   ***   J  J      *****             + +    $$$$    ****  + + +++ s +         +++++   s      +   +   s +PP+ + + + + +  + ",
               "+++++++ ++  ++  ++ ++ * * + +   ***  + +   + + ++++++++PP+++++++  +++   S  +++ + P********  +  +  + +s        ******                 *****        + + + + + **** ",
               "+*+++*+ ++  ++  ++ ++ + + + +   + +  + +   + + ++++++++  +++++++s ++++++++++++ +  +      +  +  +  + +s        +    +                       ++++++++ + + + + +  + ",]
                                                                                         #======F======#
        BG = castleBG
        theme = 3
        music = pygame.mixer.music.load("audios/Mecha Collection.wav")
    elif levelProgress == 7:
        Lvl = ["               ",
               "               ",
               "               ",
               "      o        ",
               "               ",
               "               ",
               "               ",
               "   F           ",
               "++++++++++++++++",
               "++++++++++++++++",]
        BG = plainsBG
        theme = 0
        music = pygame.mixer.music.load("audios/plains.wav")
    Clevel.clear()             # Level loader
    for i in range(10):
        for j in range(len(Lvl[i])):
            y = i * 32
            x = j * 32
            if Lvl[i][j] == "+":
                obj = block(x, y)
            elif Lvl[i][j] == "F":
                frog = Frog(x, y)
            elif Lvl[i][j] == "$":
                obj = coin(x, y)
            elif Lvl[i][j] == "#":
                obj = jigsaw(x, y)
            elif Lvl[i][j] == "a":
                obj = fruit(x, y)
            elif Lvl[i][j] == "m":
                obj = magicalOrb(x, y)
            elif Lvl[i][j] == "J":
                obj = jim(x, y, True)
            elif Lvl[i][j] == "j":
                obj = jim(x, y, False)
            elif Lvl[i][j] == "S":
                obj = spinJim(x, y)
            elif Lvl[i][j] == "f":
                obj = flower(x, y)
            elif Lvl[i][j] == "s":
                obj = stageEater(x, y)
            elif Lvl[i][j] == "P":
                obj = platform(x, y)
            elif Lvl[i][j] == "@":
                obj = fruitBlock(x, y)
            elif Lvl[i][j] == "G":
                obj = greenBlock(x, y)
            elif Lvl[i][j] == "-":
                obj = stoneBlock(x, y)
            elif Lvl[i][j] == "i":
                obj = ironBlock(x, y, False)
            elif Lvl[i][j] == "1":
                obj = ironBlock(x, y, True)
            elif Lvl[i][j] == "g":                
                obj = gearBlock(x, y)
                Clevel.append(obj)
                obj = ironBlock(x, y, True)
            elif Lvl[i][j] == "=":
                obj = flipBlock(x, y)
            elif Lvl[i][j] == "I":
                obj = invisibleBlock(x, y)
            elif Lvl[i][j] == "!":
                obj = goalSign(x, y)
            elif Lvl[i][j] == "*":
                obj = decoBlock(x, y)
            elif Lvl[i][j] == "%":
                obj = beanstalk(x, y)
            elif Lvl[i][j] == "&":
                obj = beanstalktip(x, y)
                Clevel.append(obj)
                obj = beanstalk(x, y)
            elif Lvl[i][j] == "Y":
                obj = yellowBlock(x, y)
            elif Lvl[i][j] == "o":
                obj = portal(x, y)
                frog = Frog(x + 48, y + 80)
            
                
            
            if Lvl[i][j] != "F" and Lvl[i][j] != " ":
                level.append(obj)
            #elif Lvl[i][j] != "F" and Lvl[i][j] != " ":
            #    Clevel.append(obj)
    level += Clevel
    if levelProgress != 0:
        level.append(frog)
    
    

    if BG == autumnBG:
        for i in range(10, random.randrange(11,31)):
            Leaf = leaf(random.randrange(0, screenWidth + 1), random.randrange(0, screenHeight + 1))
            level.append(Leaf)

    levelLength = len(Lvl[0]) * 32 - 32
    for N in level:
        if N.Type == "block" or N.Type == "beanstalk":
            N.connect()

    if levelProgress != 0 and levelProgress != 7:
        pygame.mixer.music.play(-1)
    Tongue = tongue(frog.x, frog.y, 0)
    
    while run and alive:    # Main loop
        pygame.time.delay(17)

        timer += 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                run = False
            
        keys = pygame.key.get_pressed()

        frog.walking = False
        
        if frog in level:
            if keys[pygame.K_LEFT] and frog.x > 0:
                frog.x -= frog.speed
                frog.walking = True
                if not frog.mouthOpen:
                    frog.faceRight = False
            if keys[pygame.K_RIGHT] and frog.x < screenWidth - frog.width:
                frog.x += frog.speed
                frog.walking = True
                if not frog.mouthOpen:
                    frog.faceRight = True
            if (keys[pygame.K_LCTRL]) and frog.onGround:
                frog.Yspeed = -10
            if frog in level and (keys[pygame.K_SPACE] or keys[pygame.K_LALT]) and spaceKeyCoolDown == 0 and not frog.mouthOpen and Tongue not in level:
                spaceKeyCoolDown = 16
                if len(frog.mouth) == 0:
                    if Tongue not in level:
                        frog.mouthOpen = True
                        Tongue = tongue(frog.x, frog.y, 0)
                        level.append(Tongue)
                        if frog.faceRight:
                            Tongue.Xspeed = 12
                        else:
                            Tongue.Xspeed = -12
                else:
                    if not (frog.mouth[0].Type == "fruit" or (frog.mouth[0].Type == "jim" and not frog.mouth[0].helmet) or frog.mouth[0].Type == "fruitblock"):
                        frog.mouth[0].Solid = False
                        frog.mouth[0].Yspeed = 0
                        if frog.mouth[0] not in level and Tongue not in level:
                            level.insert(0, frog.mouth[0])
                        if frog.faceRight:
                            frog.mouth[0].x = frog.x + cameraX + frog.width + 6
                        else:
                            frog.mouth[0].x = frog.x + cameraX - frog.width - 8
                        frog.mouth[0].y = frog.y - 2
                        frog.mouthOpen = True
                        
                    if frog.mouth[0].Type == "greenblock" or (frog.mouth[0].Type == "jim" and frog.mouth[0].helmet) or frog.mouth[0].Type == "spinjim" or frog.mouth[0].Type == "magicalorb":
                        frog.mouth[0].Solid = False
                        frog.mouth[0].Yspeed = 0
                        if frog.leftSolid and not frog.faceRight:
                            frog.x += 32
                            frog.mouth[0].x = frog.x + cameraX - 34
                        if frog.rightSolid and frog.faceRight:
                            frog.x -= 32
                            frog.mouth[0].x = frog.x + cameraX + 30
                        if frog.mouth[0].Type == "spinjim":
                            frog.mouth[0].faceRight = frog.faceRight
                            
                    frog.mouth[0].touchingTongue = False
                    frog.mouth.clear()
                    
            if len(frog.mouth) == 1:
                if frog.mouth[0].Type == "fruit" or (frog.mouth[0].Type == "jim" and not frog.mouth[0].helmet) or frog.mouth[0].Type == "fruitblock":
                    if fruitCountDown == 0:
                        fruitCountDown = 30
                    else:
                        fruitCountDown -= 1
                        if fruitCountDown == 0:
                            coinCount += 1
                            pygame.mixer.Sound.play(gulp)
                            frog.mouth.clear()
                            
            if keys[pygame.K_DOWN]:
                pass
                    
            if spaceKeyCoolDown > 0:
                spaceKeyCoolDown -= 1
            elif Tongue not in level:
                frog.mouthOpen = False
                
            if frog.faceRight:
                if frog.mouthOpen:
                    frog.animation = 3
                else:
                    if len(frog.mouth) == 0:
                        frog.animation = 1
                    else:
                        frog.animation = 5
            else:
                if frog.mouthOpen:
                    frog.animation = 2
                else:
                    if len(frog.mouth) == 0:
                        frog.animation = 0
                    else:
                        frog.animation = 4
            
            frog.leftSolid = False
            frog.rightSolid = False
            frog.onGround = False
        redrawGameWindow()
    del level
    pygame.mixer.music.stop()

pygame.quit()
