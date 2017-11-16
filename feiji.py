#coding=utf-8
import pygame
import time
import random

n=0                 #计算更换图片的时间
na=0
m=False             #是否击中己方飞机
ma=False            #是否击中敌方飞机
positionx=0
positiony=0         #己方飞机
enemyplanepositionx=0
enemyplanepositiony=0       #敌方飞机
stop=False          #停止对己方飞机的操作
class baseplane(object):
    def __init__(self,screen_temp,x,y,image_name):
        self.x=x
        self.y=y
        self.screen=screen_temp
        self.image=pygame.image.load(image_name)
        self.bullet_list=[]
class heroplane(baseplane):
    def __init__(self,screen_temp):
        baseplane.__init__(self,screen_temp,210,550,"./feiji/hero1.png")
        self.bullet_remove_list=[]
        #self.n=0

    def display(self):
        #screen.blit(hero,(x,y))
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():
                #self.bullet_list.remove(bullet)
                self.bullet_remove_list.append(bullet)
        for i in self.bullet_list:
            if i in self.bullet_remove_list:                        #mark
                self.bullet_list.remove(i)
    def move_left(self):
        self.x-=5
    def move_right(self):
        self.x+=5
    def fire(self):
        self.bullet_list.append(bullet(self.screen,self.x,self.y))
    def changephoto(self):
        global stop
        stop=True
        global n
        image1="./feiji/hero_blowup_n1.png"
        image2="./feiji/hero_blowup_n2.png"
        image3="./feiji/hero_blowup_n3.png"
        image4="./feiji/hero_blowup_n4.png"
        n=n+1
        print(n)
        if n==10:
            self.image=pygame.image.load(image1)
            self.screen.blit(self.image,(self.x,self.y))
        elif n==20:
            self.image=pygame.image.load(image2)
            self.screen.blit(self.image,(self.x,self.y))
        elif n==30:
            self.image=pygame.image.load(image3)
            self.screen.blit(self.image,(self.x,self.y))
        elif n==40:
            self.image=pygame.image.load(image4)
            self.screen.blit(self.image,(self.x,self.y))
        elif n==50:
            exit()

    '''def planeifdied(self):
        if((self.x<=positionx and positionx<=self.x+100) and (positiony>=self.y and positiony<=self.y+124)):
            global m                            #判断敌机子弹是否击中飞机
            m=True
            print(self.x)
            print(self.y)
            print(positionx)
            print(positiony)
    '''
class enemyplane(baseplane):
    def __init__(self,screen_temp):
        baseplane.__init__(self,screen_temp,0,0,"./feiji/enemy0.png")
        self.direction="right"
        self.screen=screen_temp
    def display(self):
        #screen.blit(hero,(x,y))
        self.screen.blit(self.image,(self.x,self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
    def move(self):
        if self.direction=="right":
            self.x+=5
        elif self.direction=="left":
            self.x-=5
        if self.x>429:
            self.direction="left"
        elif self.x<0:
            self.direction="right"
    def fire(self):
        num=random.randint(1,50)
        if num==12 or num==20:
            self.bullet_list.append(enemybullet(self.screen,self.x,self.y))
    def changephoto(self):             #击中敌机后
        global na
        image1="./feiji/enemy0_down1.png"
        image2="./feiji/enemy0_down2.png"
        image3="./feiji/enemy0_down3.png"
        image4="./feiji/enemy0_down4.png"
        na=na+1
        print(na)
        if na==10:
            self.image=pygame.image.load(image1)
            self.screen.blit(self.image,(self.x,self.y))
        elif na==20:
            self.image=pygame.image.load(image2)
            self.screen.blit(self.image,(self.x,self.y))
        elif na==30:
            self.image=pygame.image.load(image3) 
            self.screen.blit(self.image,(self.x,self.y))
        elif na==40:
            self.image=pygame.image.load(image4)
            self.screen.blit(self.image,(self.x,self.y))
        elif na==50:
            exit()



class basebullet(object):
    def __init__(self,screen_temp,x,y,imagename):
        self.x=x
        self.y=y
        self.screen=screen_temp
        self.image=pygame.image.load(imagename)

class bullet(basebullet):
    def __init__(self,screen_temp,x,y):
        basebullet.__init__(self,screen_temp,x+40,y-20,"./feiji/bullet.png")
        self.screen=screen_temp

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y-=5
        if((self.x>=enemyplanepositionx and self.x<=enemyplanepositionx+51) and (self.y>=0 and self.y<=39)):
            global ma
            ma=True
    def judge(self):
        if self.y<0:
            return True
        else:
            return False

class enemybullet(basebullet):
    def __init__(self,screen_temp,x,y):
        basebullet.__init__(self,screen_temp,x+25,y+40,"./feiji/bullet1.png")
        self.screen=screen_temp
        global positionx
        global positiony
        positionx=self.x
        positiony=self.y
    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    def move(self):
        self.y+=5
        if((self.x>=positionx and self.x<=positionx+100) and (self.y>=positiony and self.y<=positiony+124)):
            global m
            m=True
    def judge(self):
        if self.y>852:
            return True
        else:
            return False

    

    
def key_control(hero_temp):
#获取事件，比如按键等
    
    for event in pygame.event.get():
        global stop
        if stop:
            break
        #判断是否是点击了退出按钮
        if event.type == pygame.QUIT:
            print("exit")
            exit()
        #判断是否是按下了键
        elif event.type == pygame.KEYDOWN:
            #检测按键是否是a或者left
            if  event.key == pygame.K_LEFT:
                print('left')
                hero_temp.move_left()
            #检测按键是否是d或者right
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                print('right')
                hero_temp.move_right()
            #检测按键是否是空格键
            elif event.key == pygame.K_SPACE:
                print('space')
            #按空格键模拟飞机爆炸
                print("b")
                hero_temp.fire()
            elif event.key == pygame.K_UP:
                hero_temp.y-=5
                print('up')
            elif event.key == pygame.K_DOWN:
                hero_temp.y+=5
                print('down')

def main():
    screen=pygame.display.set_mode((480,700),0,32)
    background=pygame.image.load("./feiji/background.png")
    hero=heroplane(screen)
    emeny=enemyplane(screen)
    while True:
        screen.blit(background,(0,0))
        hero.display()
        global positionx
        global positiony
        emeny.display()
        emeny.move()
        emeny.fire()
        pygame.display.update()

        key_control(hero)
        positionx=hero.x
        positiony=hero.y
        global enemyplanepositionx
        global enemyplanepositiony
        enemyplanepositionx=emeny.x
        enemyplanepositiony=emeny.y
        #hero.planeifdied()
        if m:
            hero.changephoto()
            #print("changephoto")            #己方飞机爆炸
        if ma:
            emeny.changephoto()
        time.sleep(0.001)
if __name__=="__main__":
    main()