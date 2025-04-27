import sys, pygame, random

class Ball:
    x = [0]
    y = [0]
    def __init__(self, speed, screen, x, y):
        self.speed = speed
        self.image = pygame.image.load("ball.png").convert()
        Ball.x = x
        Ball.y = y
        screen.blit(self.image, (x,y))
        self.area = screen.get_rect()
        
    
    def move(self, screen, dir):
        if dir == 1: #go up to the left
            print(1, " before ", Ball.x, " ", Ball.y)
            Ball.x = Ball.x - self.speed
            Ball.y = Ball.y - self.speed
            print(1, " after ", Ball.x, " ", Ball.y)
            screen.blit(pygame.image.load("background.png"), (0, 0)) #draw the background
            screen.blit(self.image, (Ball.x, Ball.y))
        elif dir == 2: #go up to the right
            print(3, " before ", Ball.x, " ", Ball.y)
            Ball.x = Ball.x + self.speed
            Ball.y = Ball.y - self.speed
            print(3, " after ", Ball.x, " ", Ball.y)
            screen.blit(pygame.image.load("background.png"), (0, 0)) #draw the background
            screen.blit(self.image, (Ball.x, Ball.y))
        elif dir == 3: #go down to the left
            print(2, " before ", Ball.x, " ", Ball.y)
            Ball.x = Ball.x - self.speed
            Ball.y = Ball.y + self.speed
            print(2, " after ", Ball.x, " ", Ball.y)
            screen.blit(pygame.image.load("background.png"), (0, 0)) #draw the background
            screen.blit(self.image, (Ball.x, Ball.y))
        elif dir == 4: #go down to the right
            print(4, " before ", Ball.x, " ", Ball.y)
            Ball.x = Ball.x + self.speed
            Ball.y = Ball.y + self.speed
            print(4, " after ", Ball.x, " ", Ball.y)
            screen.blit(pygame.image.load("background.png"), (0, 0)) #draw the background
            screen.blit(self.image, (Ball.x, Ball.y))
        Ball.checkBounds(self, screen)
        # Because I am calling the class method, I have to pass self to give the actual instance of the method. 
        # Another way to deal with this would be to instanciate the class first, but this solution fits my case
       
    def checkBounds(self, screen):
        if Ball.x <= 0:
            print("Enemy wins")
            #mark points to the enemy
        elif Ball.x >=800:
            print("Player wins")
            #mark points to the player
        elif Ball.y <= 0:
            dir = random.randint(3, 4) #I checked if a collision happened at the top, and if it did, I am randomly choosing between going down through right or left
            Ball.move(self, screen, dir)
        elif Ball.y >= 600:
            dir = random.randint(1, 2) #I checked if a collision happened at the bottom, and if it did, I am randomly choosing between going up through right or left
            Ball.move(self, screen, dir)

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
            Player.y = Player.y - self.speed
            screen.blit(pygame.image.load("background.png"), (0, 0)) #draw the background
            screen.blit(self.player, (Player.x, Player.y))
        if userInput[pygame.K_s]:
            Player.y = Player.y + self.speed
            screen.blit(pygame.image.load("background.png"), (0, 0)) #draw the background
            screen.blit(self.player, (Player.x, Player.y))
        
    
        # pygame.display.update()


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
    ballSpeed = 10
    x = 5
    y = 10
    xBall = 400
    yBall = 300
    dir = random.randint(1, 4)

    while True:
        player = Player(speed, screen, x, y)
        ball = Ball(ballSpeed, screen, xBall, yBall)
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
            ball.move(screen, dir)
            xBall = ball.x
            yBall = ball.y
        pygame.display.update()