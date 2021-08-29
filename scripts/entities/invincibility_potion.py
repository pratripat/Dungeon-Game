from .potion import Potion

class Invincibility_Potion(Potion):
    def __init__(self, game, id, rect):
        super().__init__(game, id, rect)

    def update(self):
        super().update(self.interaction)

    def interaction(self):
        #Increments player invincibility when player touches the potion
        if self.id == 'small_invincibility_potion':
            self.game.entity_manager.player.increment_invincibility(5)

        if self.id == 'big_invincibility_potion':
            self.game.entity_manager.player.increment_invincibility(10)

        self.game.entity_manager.invincibility_potions.remove(self)
