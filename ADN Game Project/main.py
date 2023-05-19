import pygame
import time
import random
from pygame.locals import * #for all modules to be imported from a particular file

size =40

#apple class
class Apple:
    def __init__(self ,parent_screen):
        self.block=pygame.image.load("Resources/apple2.jpeg").convert()
        self.parent_screen=parent_screen
        self.x= size*3
        self.y= size*3

    def draw(self):
        self.parent_screen.blit(self.block,(self.x,self.y)) 
        pygame.display.flip() #to refresh 
    
    def move(self):
        self.x=random.randint(0,24)*size
        self.y=random.randint(0,19)*size

#snake class
class Snake:
    def __init__(self, parent_screen, length):
        self.parent_screen=parent_screen
        self.block= pygame.image.load("Resources/block.jpg").convert()
        self.direction = 'down'

        self.length=length
        self.x=[40]*length
        self.y=[40]*length
        
    def increase_length(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_left(self):
        self.direction = 'left'
    
    def move_right(self):
        self.direction = 'right'
    
    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'
         
    def walk(self):
        for i in range(self.length-1,0,-1):
            self.x[i]=self.x[i-1]
            self.y[i]=self.y[i-1]

        if self.direction =='left':
            self.x[0]-= size
        if self.direction =='right':
            self.x[0]+= size
        if self.direction =='up':
            self.y[0]-= size
        if self.direction =='down':
            self.y[0]+= size
        self.draw()
    
    def draw(self):
        self.parent_screen.fill((110,110,5))

        for i in range(self.length):
            self.parent_screen.blit(self.block,(self.x[i],self.y[i])) 
        pygame.display.flip() #to refresh 
        
    
#for game 
class Game:
    def __init__(self):
        pygame.init() #for initialization
        pygame.display.set_caption("Snake And Apple Game")
        # To initialize a window or screen for display
        self.surface = pygame.display.set_mode((1000,800))  
        self.surface.fill((110,110,5)) #to fill the background
        self.snake=Snake(self.surface,1)
        self.snake.draw()
        self.apple =Apple(self.surface)
        self.apple.draw()
    
    def collision(self,x1,y1,x2,y2):
        if x1 >= x2 and x1<x2+size:
            if y1 >=y2 and y1<y2+size:
                return True
        return False
        
    def start(self):
        self.snake.walk()
        self.apple.draw()
        self.score_display()
        pygame.display.flip()

        #snake colliding with apple
        if self.collision(self.snake.x[0],self.snake.y[0],self.apple.x,self.apple.y):
            self.snake.increase_length()
            self.apple.move()

        #snake colliding with itself
        for i in range(3,self.snake.length):
            if self.collision(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                raise "Game Over"

    def score_display(self):
        font = pygame.font.SysFont('Calibri',30)
        welcome = font.render(f"Serpent-pomme Game",True,(200,200,200))
        self.surface.blit(welcome,(20,10))
        score= font.render(f"Score: {self.snake.length}",True, (200,200,200))
        self.surface.blit(score,(880,10))
    
    def show_game_over(self):
        self.surface.fill((110,110,5))
        font = pygame.font.SysFont('Calibri',30)
        over1 =font.render(f"Game is over! Your score is: {self.snake.length}",True, (200,200,200))
        self.surface.blit(over1,(200,300))
        over2 =font.render("Press Enter to play again. To exit press Escape!",True,(200,200,200))
        self.surface.blit(over2,(200,350))
        pygame.display.flip()

    def reset(self):
        self.snake=Snake(self.surface,1)
        self.apple =Apple(self.surface)

    def run(self):
        running =True
        pause = False

        while(running):
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running =False
                    
                    if event.key == K_RETURN:
                        pause =False

                    if event.key == K_UP:
                        self.snake.move_up()

                    if event.key == K_DOWN:
                        self.snake.move_down()

                    if event.key == K_LEFT:
                        self.snake.move_left()

                    if event.key ==K_RIGHT:
                        self.snake.move_right()

                elif event.type == QUIT:
                    running= False 
            try:
                if not pause:
                    self.start() 
            except Exception as e:
                self.show_game_over() 
                pause= True
                self.reset()
            
            time.sleep(0.2)

       


if __name__ == "__main__":
    game =Game()
    game.run()
    

