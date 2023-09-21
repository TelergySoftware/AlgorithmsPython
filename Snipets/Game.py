import pygame as pg


class Game:
    """
    Simple black screen template.
    """
    def __init__(self, title: str, width: int = 800, height: int = 600):
        # Initialize pygame
        pg.init()
        # Create the screen
        self.screen = pg.display.set_mode((width, height))
        # Set the title
        pg.display.set_caption(title)
        # Create the clock
        self.clock = pg.time.Clock()
        # Set the done flag
        self.done = False

    def run(self) -> None:
        """
        Run the game.
        """
        while not self.done:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self) -> None:
        """
        Handle events.
        """
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.done = True

    def update(self) -> None:
        """
        Update the game state.
        """
        pass

    def draw(self) -> None:
        """
        Clear the screen and draw the game objects.
        """
        self.screen.fill((0, 0, 0))
        pg.display.update()
