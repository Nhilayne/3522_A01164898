import math
import random
import datetime
import time

import asteroid


class Controller:

    def __init__(self, num_asteroids, radius_range_min, radius_range_max):
        self._asteroid_list = []
        for i in range(0, num_asteroids, 1):
            radius = random.randint(radius_range_min, radius_range_max)
            circumference = 2 * math.pi * radius
            position_gen = asteroid.Vector3D(random.randint(0, 99), random.randint(0, 99), random.randint(0, 99))
            velocity_gen = asteroid.Vector3D(random.randint(-5, 5), random.randint(-5, 5), random.randint(-5, 5))
            self._asteroid_list.append(asteroid.Asteroid(circumference, position_gen, velocity_gen))

    def simulate(self, seconds):
        print(f"Simulation start time:{datetime.datetime.now()}")
        while seconds > 0:
            curr_time = datetime.datetime.now()
            formatted_time = curr_time.strftime('%f')
            sleep_time = ((int(formatted_time) - 1000000) / 10000) / 100 * -1
            time.sleep(sleep_time)
            for x in self._asteroid_list:
                x.move()
                print(x.__str__())
            seconds = seconds - 1



def main():
    controller = Controller(100, 1, 4)
    controller.simulate(5)


if __name__ == "__main__":
    main()
