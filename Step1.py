#교수님 몰래 강의실 탈출
import pygame
from Player import Player
from Study import Study
from Desk import Desk
from Door import Door
from Screen2 import Screen2
from Step2 import Step2
from Step3 import Step3
from Step4 import Step4
from Clear import Clear

class Step1:
    width = 1200
    height = 800

    x = 275
    y = 240

    face = "back"

    desk = None
    desks = []

    invincibility_flag = False

    face_timer = 700

    screen = pygame.display.set_mode((width, height))

    front = pygame.image.load("resources/images/front.png")
    back = pygame.image.load("resources/images/back.png")
    board = pygame.image.load("resources/images/board.png")

    fpsClock = pygame.time.Clock()
    FPS = 100

    def __init__(self):
        self.player = Player(self.screen, self.x, self.y)
        self.study = Study(self.screen, self.player, self.desks, self.invincibility_flag)
        self.screen2 = Screen2(self.screen, self.width, self.height)

    def Step1(self):

        finisher=True
        while finisher:
            for event in pygame.event.get():    #종료 이벤트
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
            pygame.display.update()

            self.screen.fill((135, 135, 135))

            self.screen.blit(self.board, (50, 100))

            for i in range(3):
                for j in range(3):
                    self.desk = Desk(self.screen, 275 + self.width/5 * i, 340 + self.height/5 *j)
                    self.desk.draw()
                    self.desks.append(self.desk)
            self.study.study(self.desk)

            self.door = Door(self.screen, 1050, 600)
            self.door.draw()
            self.player.move()

            if self.face == "front":
                if self.study.invincibility_flag==True:
                    print(2)
                else:
                    print(1)

            if self.face == "front":
                self.screen.blit(self.front, (700, 50))
            elif self.face == "back":
                self.screen.blit(self.back, (700, 50))
            self.face_timer -= 1

            if self.face_timer ==0:
                if self.face == "front":
                    self.face_timer = 700
                    self.face = "back"

                elif self.face == "back":
                    self.face_timer = 300
                    self.face = "front"

            if self.player.colliderect(self.door):
                finisher = False

    def Starting(self):
        while True:
            self.screen2.Start()
            game_step1 = Step1()
            game_step1.Step1()
            game_step2 = Step2(self.screen, self.width, self.height)
            game_step2.Step2()
            game_step3 = Step3(self.screen, self.width, self.height)
            game_step3.Step3()
            game_step4 = Step4(self.screen, self.width, self.width)
            game_step4.Step4()
            clear = Clear(self.screen, self.width, self.height)
            clear.Start()

game2 = Step1()
game2.Starting()