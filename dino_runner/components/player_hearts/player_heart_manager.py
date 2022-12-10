from dino_runner.utils.constants import HEART_COUNT
from dino_runner.components.player_hearts.heart import Heart

class PlayerHeartManager:
    def __init__(self):
        self.heart_count = HEART_COUNT
        
    def draw(self, screen):
        x_postion = 10
        y_postion = 20

        for counter in range(self.heart_count): #0,1,2,3,4 (0,4)
            heart = Heart(x_postion, y_postion)
            heart.draw(screen)
            x_postion += 30

    def reduce_heart(self):
        self.heart_count -= 1