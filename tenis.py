import sys, pygame, random

class Ball:
    def __init__(self, speed, screen):
        self.speed = speed
        self.image = pygame.image.load("ball.png").convert()
        screen.blit(self.image, (400,300))
        # pygame.display.flip()

        self.area = screen.get_rect()
    
    def move(self):
        dir = random.randint(1, 2)
        #if dir == 1:
            #TODO: add checks for it to move through x and y direction correctly
        

class Player:
    x = 0 #static variables, belong to the class
    y = 0
    def __init__(self, speed, screen, x, y):
        Player.x = x #access the static variable by calling the class
        Player.y = y
        self.player = pygame.image.load("player.png").convert()
        screen.blit(self.player, (Player.x, Player.y))
       
        self.area = screen.get_rect()
        self.speed = speed

    def update(self):
        newpos = self.move(self.rect)
        self.rect = newpos

    def move(self, screen):
        # screen.blit(pygame.image.load("background.png"), (0, 0)) #draw the background
        userInput = pygame.key.get_pressed()
        if userInput[pygame.K_w]:
            print("w")
            Player.y = Player.y - self.speed
            screen.blit(pygame.image.load("background.png"), (0, 0)) #draw the background
            screen.blit(self.player, (Player.x, Player.y))
        if userInput[pygame.K_s]:
            print("s")
            Player.y = Player.y + self.speed
            screen.blit(pygame.image.load("background.png"), (0, 0)) #draw the background
            screen.blit(self.player, (Player.x, Player.y))
        #TODO: add check to see if it goes over the limits
        
    
        pygame.display.update()


class Enemy:

    def __init__(self, speed, screen):
        self.enemy = pygame.image.load("enemy.png").convert()
        screen.blit(self.enemy, (760, 10))

    # def move:
        

class Main:
    pygame.init()
    size = width, height = 800, 600 
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Ping Pong")
    background = pygame.image.load("background.png")

    screen.blit(background, (0, 0)) #draw the background
    

    clock = pygame.time.Clock()

    pygame.display.update() #shows all changes on screen
    speed = 20
    x = 5
    y = 10

    while True:
        player = Player(speed, screen, x, y)
        ball = Ball(speed, screen)
        enemy = Enemy(speed, screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit
                pygame.quit()
                quit()

            # screen.blit(background, (0, 0)) #draw the background
            player.move(screen)
            x = player.x
            y = player.y
            # screen.blit(player, (Player.x, Player.y))
            
        # pygame.display.update()