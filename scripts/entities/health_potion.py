from .potion import Potion

class Health_Potion(Potion):
    def __init__(self, game, id, rect):
        super().__init__(game, id, rect)

    def update(self):
        super().update(self.interaction)

    def interaction(self):
        #Increments player health when player touches the potion
        if self.id == 'small_health_potion':
            self.game.entity_manager.player.increment_health(1)

        if self.id == 'big_health_potion':
            self.game.entity_manager.player.increment_health(2)

        self.game.entity_manager.health_potions.remove(self)
        self.game.sfx_manager.play_sfx('power_up')
