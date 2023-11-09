import numpy as np
import matplotlib.pyplot as plt

class Checker:
    def __init__(self, resolution, tile_size):
        self.resolution = resolution
        self.tile_size = tile_size
        self.output = np.zeros((resolution, resolution))

    def draw(self):
        #check resolution and tile_size
        assert self.resolution % (2*self.tile_size) == 0, "resolution is not divisible by 2*tile_size, try again!"
        for i in range(self.resolution):
            for j in range(self.resolution):
                #0 is black, 1 is white
                if (i//self.tile_size)%2 == 0 and (j//self.tile_size)%2 ==0:
                    self.output[i][j] = 0
                elif (i//self.tile_size)%2 == 1 and (j//self.tile_size)%2 ==1:
                    self.output[i][j] = 0
                else:
                    self.output[i][j] = 1
        #return a copy
        return np.copy(self.output) 
    
    def show(self):
        plt.imshow(self.output, cmap="gray")
        plt.show()

class Circle:
    def __init__(self, resolution, radius, position):
        self.resolution = resolution
        self.radius = radius
        self.position = position
        self.output = np.zeros((resolution, resolution))
    def draw(self):
        x = self.position[0]   #x-coordinate
        y = self.position[1]   #y-coordinate
        x, y = np.meshgrid(x,y)
        for i in range(self.resolution):
            for j in range(self.resolution):
                distance = np.sqrt((j-x)**2+(i-y)**2)
                if distance <= self.radius:
                    self.output[i][j] = 1 #1 is white
                else: 
                    self.output[i][j] = 0 #0 is black
        return np.copy(self.output)
    def show(self):
        plt.imshow(self.output, cmap = "gray")
        plt.show()
cir = Circle(200,20,(30,40))
cir.draw()
cir.show()    

# class Specturm:
#     def __init__(self, resolution):
#         self.resolution = resolution
#         self.output = None

#     def draw(self):
#         #Create an empty array with shape for 3 channels
#         self.output = np.zeros((self.resolution, self.resolution, 3)) #rows, columns, 3 color channels (Red, Green, Blue)
        

#         for i in range(self.resolution):
#             intensity = 
#             for j in range(self.resolution):
#                 self.output[i][j][0] =    #red channel
#                 self.output[i][j][1] = 
#                 self.output[i][j][2]

#         self.output[self.]
#     def show(self):
#         plt.imshow()

