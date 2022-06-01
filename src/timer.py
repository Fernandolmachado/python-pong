import pygame


class Timer(object):
    def __init__(self, clock, delay):
        self.clock = clock
        self.delay_time = delay
        self.time = 0
        self.running = False

        self.reached = False

    def start(self):
        self.running = True

    def pause(self):
        self.running = False

    def stop(self):
        self.running = False
        self.reached = False
        self.time = 0

    def time_reached(self) -> bool:
        return self.reached

    def get_time(self):
        return self.format_time(self.time / 1000)

    def get_countdown(self):
        return self.format_time((self.delay_time - self.time) / 1000)

    @staticmethod
    def format_time(minutos):
        str_min = minutos // 60
        str_sec = minutos % 60
        return "{:02d}:{:02d}".format(int(str_min), int(str_sec))

    def update(self):
        if self.running:
            self.time += self.clock.get_time()

            if self.delay_time <= self.time:
                self.reached = True
                self.pause()
