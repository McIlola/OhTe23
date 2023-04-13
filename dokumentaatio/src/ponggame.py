import pygame

class Pong:
    def __init__(self) -> None:
        pygame.init()

        self.width=640
        self.height=480
        self.surface=pygame.display.set_mode((self.width,self.height))
        
        self.x_player1=0
        self.y_player1=0
        self.up_player1 = False
        self.down_player1 = False
        self.player1=pygame.Rect(self.x_player1,self.y_player1,20,100)

        self.x_player2=620
        self.y_player2=0
        self.up_player2 = False
        self.down_player2 = False
        self.player2=pygame.Rect(self.x_player2,self.y_player2,20,100)
        self.clock=pygame.time.Clock()
        self.loop()
        
        
    def loop(self):
        while True:
            self.search_events()
            self.draw_screen()

    def search_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_w and self.y_player1>=0:
                    self.up_player1 = True
                if event.key == pygame.K_s and self.y_player1<=480:
                    self.down_player1 = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and self.y_player2>=0:
                    self.up_player2 = True
                if event.key == pygame.K_DOWN and self.y_player2<=480:
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
            if self.y_player1+self.player1.height>=480:
                self.down_player1 = False
        
        if self.up_player2:
            self.y_player2 -= 2
            if self.y_player2<=0:
                self.up_player2 = False
            
        if self.down_player2:
            self.y_player2 += 2
            if self.y_player2+self.player2.height>=480:
                self.down_player2 = False

        pygame.draw.rect(self.surface,(255,0,0),(self.x_player1,self.y_player1,20,100))
        pygame.draw.rect(self.surface,(255,0,0),(self.x_player2,self.y_player2,20,100))
        
        pygame.display.flip()
        self.clock.tick(60)
Pong()  