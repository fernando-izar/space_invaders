import pygame

class Ship:
    """A class to manage the ship."""
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # get the screen rect attribute from ai_game's screen attribute
        self.screen_rect = ai_game.screen.get_rect()
        # load the ship image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # start each new ship at the bottom center of the screen
        # set the midbottom attribute of the ship's rect to match the midbottom attribute of the screen's rect
        self.rect.midbottom = self.screen_rect.midbottom
        # store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)
        # movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag."""
        # update the ship's x value, not the rect
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # update rect object from self.x
        self.rect.x = self.x


    def blitme(self):
        """Draw the ship at its current location."""
        # draw the image to the screen at the position specified by self.rect
        self.screen.blit(self.image, self.rect)