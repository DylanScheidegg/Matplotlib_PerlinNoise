from noise import snoise2
from matplotlib import pyplot as plt


class PerlinNoise(object):
    def __init__(self, width):
        self.width = width
        self.scl = 1

    def create(self):
        ycor = []
        for y in range(self.width):
            xcor = []
            for x in range(self.width):
                val = int(abs(snoise2(x * self.scl, y * self.scl) * 255))
                xcor.append(val)
            ycor.append(xcor)
        return ycor

    def draw(self, arr):
        loadx = []
        for x in arr:
            loady = []
            for y in x:
                loady.append(y)
            loadx.append(loady)

        plt.imshow(loadx, cmap='magma_r', interpolation='lanczos')
        plt.colorbar()

        plt.figure()
        plt.imshow(loadx, cmap='gray', interpolation='lanczos')
        plt.colorbar()
        plt.show()


graph = PerlinNoise(200)
coords = graph.create()
graph.draw(coords)
