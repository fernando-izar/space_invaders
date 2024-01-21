import pygame

class Ship:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        # get the screen rect attribute from ai_game's screen attribute
        self.screen_rect = ai_game.screen.get_rect()
        # load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # start each new ship at the bottom center of the screen
        # set the midbottom attribute of the ship's rect to match the midbottom attribute of the screen's rect
        self.rect.midbottom = self.screen_rect.midbottom
    def blitme(self):
        """Draw the ship at its current location."""
        # draw the image to the screen at the position specified by self.rect
        self.screen.blit(self.image, self.rect)