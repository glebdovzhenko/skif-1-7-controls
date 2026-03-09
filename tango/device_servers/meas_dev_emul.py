# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 17:49:51 2023

@author: Konstantin
"""

from time import sleep
from math import sin, pi


class Meter:
    def __init__(self, Mutex=None):
        self.meas_count = 0
        self.acc_time = 1
        self.Mutex = Mutex
        pass

    def reset(self):
        self.meas_count = 0

    def setAccTime(self, acc_time):
        self.acc_time = acc_time

    def meas(self):
        # print('Start meas.')
        if self.Mutex:
            self.Mutex.lock()

        sleep(self.acc_time)

        if self.Mutex:
            self.Mutex.unlock()
        # print('Stop meas.')

        self.meas_count += 1
        # print(" Meas ",self.meas_count, " point ",end=' ')
        return [
            sin((self.meas_count * pi - 1) / 10.0) ** 2 * 100,
            sin((self.meas_count * pi - 1) / 10.0 - pi / 4) ** 2 * 50,
        ]

    def start_meas(self):
        # print('Start meas.')
        if self.Mutex:
            self.Mutex.lock()
        self.meas_count += 1
        if self.Mutex:
            self.Mutex.unlock()

    def end_meas(self):
        # if self.Mutex:
        #    self.Mutex.unlock()
        # print('Stop meas.')

        # print(" Meas ",self.meas_count, " point ",end=' ')
        return [
            sin((self.meas_count * pi - 1) / 10.0) ** 2 * 100,
            sin((self.meas_count * pi - 1) / 10.0 - pi / 4) ** 2 * 50,
        ]

    def NumberProfs(self):
        return 2
