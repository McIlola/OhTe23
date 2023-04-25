import sys
import pygame

class Pong:
    def __init__(self) -> None:
        pygame.init()

        self.width=640
        self.height=480
        self.surface=pygame.display.set_mode((self.width,self.height))
        
        self.mode1=False
        self.mode2=False
        self.start_screen()
        
        self.x_player1=0
        self.y_player1=0
        self.up_player1 = False
        self.down_player1 = False
        self.player1=pygame.Rect(self.x_player1,self.y_player1,20,100)

        self.x_player2=self.width-20
        self.y_player2=0
        self.up_player2 = False
        self.down_player2 = False
        self.player2=pygame.Rect(self.x_player2,self.y_player2,20,100)
        
        self.x_ball=320
        self.y_ball=240
        self.ballsize=20
        self.ball=pygame.Rect(self.x_ball,self.y_ball,self.ballsize,self.ballsize)
        self.speed_x=2
        self.speed_y=2

        self.clock=pygame.time.Clock()
        self.loop()
        
    def loop(self):
        while True:
            self.search_events()
            self.draw_screen()
    
    def start_screen(self):
        while True:
            self.surface.fill((0, 0, 0))
            self.modebutton1=pygame.Rect(self.width/2-75,50,150,50)
            pygame.draw.rect(self.surface,(255,0,0),self.modebutton1)
            self.modebutton2=pygame.Rect(self.width/2-75,150,150,50)
            pygame.draw.rect(self.surface,(255,0,0),self.modebutton2)
            font=pygame.font.SysFont("Arial",24)
            text1=font.render("Normal mode",True,(0,0,0))
            self.surface.blit(text1,(self.modebutton1.centerx-text1.get_width()/2,self.modebutton1.centery-text1.get_height()/2))
            text2=font.render("Hard mode",True,(0,0,0))
            self.surface.blit(text2,(self.modebutton2.centerx-text2.get_width()/2,self.modebutton2.centery-text2.get_height()/2))
            for event in pygame.event.get():
                if event.type==pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect.collidepoint(self.modebutton1,event.pos):
                        self.mode1=True
                        break
                    if pygame.Rect.collidepoint(self.modebutton2,event.pos):
                        self.mode2=True
                        break                
                if event.type == pygame.QUIT: 
                    sys.exit()
                if self.mode1 or self.mode2: 
                    break       
            pygame.display.flip()
            if self.mode1 or self.mode2: 
                break

    def search_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()                
            
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_w and self.y_player1>=0:
                    self.up_player1 = True
                if event.key == pygame.K_s and self.y_player1<=self.height:
                    self.down_player1 = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.y_player2>=0:
                    self.up_player2 = True
                if event.key == pygame.K_DOWN and self.y_player2<=self.height:
                    self.down_player2 = True
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.up_player1 = False
                if event.key == pygame.K_s:
                    self.down_player1 = False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.up_player2 = False
                if event.key == pygame.K_DOWN:
                    self.down_player2 = False
    
    def draw_screen(self):
        self.surface.fill((0, 0, 0))
        
        if self.up_player1:
            self.y_player1 -= 2
            if self.y_player1<=0:
                self.up_player1 = False
            
        if self.down_player1:
            self.y_player1 += 2
            if self.y_player1+self.player1.height>=self.height:
                self.down_player1 = False
        
        if self.up_player2:
            self.y_player2 -= 2
            if self.y_player2<=0:
                self.up_player2 = False
            
        if self.down_player2:
            self.y_player2 += 2
            if self.y_player2+self.player2.height>=self.height:
                self.down_player2 = False

        self.x_ball-=self.speed_x
        self.y_ball-=self.speed_y
        
        if self.y_ball<=0 or self.y_ball+self.ballsize>=self.height:
            self.speed_y=-self.speed_y
        
        #pygame.Rect.colliderect(self.ball,self.player1):
        if self.x_ball<self.player1.width:
            if (self.y_ball+self.ball.height)>=self.y_player1 and self.y_ball<=self.y_player1+self.player1.height:
                self.speed_x=-self.speed_x    
            else:
                self.speed_x=0
                self.speed_y=0
        
        #pygame.Rect.colliderect(self.ball,self.player2):    
        if self.x_ball+self.ballsize>=self.x_player2:
            if (self.y_ball+self.ball.height)>=self.y_player2 and self.y_ball<=self.y_player2+self.player1.height:
                self.speed_x=-self.speed_x
            else:
                self.speed_x=0
                self.speed_y=0
        
        self.player1=pygame.Rect(self.x_player1,self.y_player1,20,100)
        pygame.draw.rect(self.surface,(255,0,0),self.player1)
        self.player2=pygame.Rect(self.x_player2,self.y_player2,20,100)
        pygame.draw.rect(self.surface,(255,0,0),self.player2)
        
        self.ball=pygame.Rect(self.x_ball,self.y_ball,self.ballsize,self.ballsize)
        pygame.draw.circle(self.surface,(255,255,255),(self.x_ball+self.ballsize/2,self.y_ball+self.ballsize/2),self.ballsize/2)

        pygame.display.flip()
        self.clock.tick(60)

if __name__ == "__main__":
    Pong()
