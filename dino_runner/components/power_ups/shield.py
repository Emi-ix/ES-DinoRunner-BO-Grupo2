from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import SHIELD_TYPE , SHIELD

class Shield(PowerUp):
    def _init_(self):
        self.image = SHIELD
        self.type = SHIELD_TYPE
        super()._init_(self.image, self.type)