from Vector import Vector
from Square import Square
from Map import Map


if __name__ == '__main__':
    mapa = Map()
    for i in mapa.to_grid():
        print(i)
    # x = Square(Vector(11, 49), Map())
    # for i in range(20):
    #     x.jump()
    #     x.move()
    #     print(x)
    #     print("------------------------")
