import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self, color):
        super().__init__()
        self._points = 0
        self._points2 = 0
        self.add_points(0)
        self._color = color
        if color == constants.GREEN:
            self.set_position(Point(800, 0))
            self.set_text("Player Two: 0")
        else:
            self.set_position(Point(0, 0))

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        if self._color == constants.GREEN:
            self._points2 += points
            self.set_text(f"Player Two: {self._points2}")
        else:
            self._points += points
            self.set_text(f"Player One: {self._points}")

    def set_position(self, position):
        if self._color == constants.GREEN:
            super().set_position(Point(800, 0))
            super().set_text("Player Two: 0")
        else:
            super().set_position(Point(600, 0))
        return super().set_position(position)