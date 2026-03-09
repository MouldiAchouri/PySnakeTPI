from game import game
from config.constants import *

class Menu:
    def __init__(self, options= None):
        self.active = False
        self.countdown = False
        self.timer = 0

        self.overlay = pygame.Surface((WIDTH, HEIGHT))
        self.overlay.fill((0 ,0 ,0 ))

        self.options = options if options else ["Reprendre","Recommencer","Option", "Quitter"]
        self.selected_index = 0

#    def pause(self):
#        if


