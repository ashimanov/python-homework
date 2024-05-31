
import time

class Player:
    def __init__(self, position_x, position_y):
        self.hp = 4
        self.position = (position_x, position_y)

    def walk_left(self, distance):
        if distance > self.position[0]:
            distance = self.position[0]
        elif distance < 0:
            distance = 0
        self.position = (max(0, self.position[0] - distance), self.position[1])
        print(f'You have walked back {distance} meters. You position is now {self.position}!')
    
    def walk_right(self, distance):
        if distance < 0:
            distance = 0
        elif (self.position[0] + distance) > 1000:
            distance = 1000 - self.position[0]
        self.position = (min(1000, self.position[0] + distance), self.position[1])
        print(f'You have walked {distance} meters. You position is now {self.position}!')

    def jump(self, distance: int):
        if distance > 100:
            distance = 100
        elif distance < 0:
            distance = 0

        self.position = (self.position[0], max(0, self.position[1] + distance))
        print(f'You have jumped {distance} meters high. You position is now {self.position}!')
        time.sleep(2)
        print('Still in the air!')
        time.sleep(2)
        self.position = (self.position[0], 0)
        print(f'You have landed! Your position is now {self.position}!')




alex = Player(0, 0)
alex.hp

alex.walk_left(200)
alex.walk_right(150)
alex.walk_right(450)
alex.walk_left(50)
alex.walk_right(900)
alex.walk_left(350)
alex.jump(5)
alex.jump(25)
alex.jump(150)






class Player1:
    def __init__(self, health=4, x=0, y=0):
        self.health = health
        self.position = (x, y)

    def walk_left(self, distance):
        self.position = (max(0, self.position[0] - distance), self.position[1])

    def walk_right(self, distance):
        self.position = (min(1000, self.position[0] + distance), self.position[1])

    def jump(self, height):
        self.position = (self.position[0], min(100, self.position[1] + height))

    def __str__(self):
        return f"Health: {self.health}, Position: ({self.position[0]}, {self.position[1]})"


# Вот как можно протестировать:
player = Player1()
player.walk_right(10150)
player.walk_left(50)
player.jump(20)
print(player)