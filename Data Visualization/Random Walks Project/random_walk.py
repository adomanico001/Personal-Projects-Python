# Generates data for a random walk
# @author Addie Domanico
# @version 05/04/2024

from random import choice

class RandomWalk:
    """A class to generate random walks"""

    def __init__(self, num_points=5000):
        """Initializes attributes of a walk"""
        self.num_points = num_points

        # Each walk starts at coordinate (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Calculates all the points in the walk.
            Will the walk go left or right?
            How far will it go in that direction?
            Will it go up or down?
            How far will it go in that direction?"""
        # Steps taken until walk reaches desired length
        while len(self.x_values) < self.num_points:
            # Decide which direction to go and how far to go in that direction
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            # Reject the moves that go nowhere
            if x_step == 0 and y_step == 0:
                continue

            # Calculates the new position
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)
            
