# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 17:37:09 2023

@author: Konstantin
"""

from time import sleep


class Motor:
    def __init__(self):
        self.ang = 1.0

    def moveTo(self, ang: float) -> None:
        # print(f" Moving to {ang:.5f} rad", end=' ')
        sleep(0.5)
        self.ang = ang

    def shiftTo(self, ang):
        # print(f" Moving to {ang:.5f} rad", end=' ')
        sleep(0.5)
        self.ang += ang

    def pos(self):
        return self.ang
