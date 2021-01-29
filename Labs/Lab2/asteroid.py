import random
import datetime

class Vector3D:
    def __init__(self, x, y, z):
        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value

    def add(self, vector):
        self.x = (self.x + vector.x)
        self.y = (self.y + vector.y)
        self.z = (self.z + vector.z)

    def get_tuple(self):
        vector_tuple = (self.x, self.y, self.z)
        return vector_tuple

    def __str__(self):
        return f'x:{self.x}, y:{self.y}, z:{self.z}'


class Asteroid:

    count = 0

    def __init__(self, circumference, position, velocity):
        self._circumference = circumference
        self._position = position
        self._velocity = velocity
        self._id = self.inc_id()

    @property
    def circumference(self):
        return self._circumference

    @circumference.setter
    def circumference(self, value):
        self._circumference = value

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, value):
        self._velocity = value

    @property
    def id(self):
        return self._id

    @classmethod
    def inc_id(cls):
        cls.count = cls.count + 1
        return cls.count

    def move(self):
        self.position.add(self.velocity)
        return ""


    def __str__(self):
        return f'Asteroid #{self.id}; position:{self.position}, velocity:{self.velocity}'


def main():
    my_vector = Vector3D(2,4,6)
    new_vector = Vector3D(6,4,2)
    my_vector.add(new_vector)
    print(my_vector.__str__())
    print("##############")
    my_asteroid = Asteroid(10, my_vector, new_vector)
    print(my_asteroid.position)
    print(my_asteroid.__str__())
    print(my_asteroid.move())
    print(my_asteroid.position)



if __name__ == "__main__":
    main()
