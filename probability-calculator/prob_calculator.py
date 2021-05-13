import copy
from collections import Counter, ChainMap
import random

# Consider using the modules imported above.


class Hat:
    def __init__(self, **kwargs) -> None:
        self.content = []
        for key, value in kwargs.items():
            for _ in range(value):
                self.content.append(key)

    def draw(self, num_balls_to_draw):
        if num_balls_to_draw > len(self.content):
            return self.content
        return random.sample(self.content, num_balls_to_draw)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    c = Counter(expected_balls)
    expected_balls_list = list(c.elements())
    for _ in range(num_experiments):
        draw_list = hat.draw(num_balls_drawn)
        if set(expected_balls_list).issubset(draw_list):
           count += 1
    return count / num_experiments
