#!/usr/bin/python3

import secrets


class Cage:
    def __init__(self, max_number):
        self.max_number = max_number
        self.pending = [i+1 for i in range(max_number)]
        self.drawn = []

    def roll(self):
        try:
            i = secrets.randbelow(len(self.pending))
            ball = self.pending.pop(i)
            self.drawn.append(ball)
            return ball
        except ValueError:
            return None

    def alt_roll(self):
        while len(self.drawn) < self.max_number:
            ball = secrets.randbelow(self.max_number)+1
            if ball not in self.drawn:
                self.drawn.append(ball)
                self.pending.remove(ball)
                return ball
        return None
