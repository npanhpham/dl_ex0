# created on : Oct 2023
# author: minh nq

import numpy as np
import matplotlib.pyplot as plt
# import NumpyTests

# For CheckerBoard  - RGB: black:0 --- white:255


class Checker:
    resolution = 0
    tile_size = 0
    # Implement a constructor 2 int arguments: resolution, tile_size
    # Store the arguments as instance var. Create an add instance var Output
    # that can store the pattern

    def __init__(self, resolution, tile_size):
        self.resolution = resolution
        self.tile_size = tile_size
        self.output = None  # Here is an instance var
        # if resolution % (2 * tile_size) != 0:
        #     raise ValueError("Resolution must be evenly divisible by 2 * tile_size")

    # a method Draw creates the checkerboard pattern as a numpy array
    # tile in the top left is black + resolution value is dividable by 2*tile_size
    # Store the pattern in the instance variable output and return a copy.
    def draw(self):
        black_arr = np.zeros((self.tile_size, self.tile_size), dtype=np.uint8)  # uint8: 0-255
        white_arr = np.ones((self.tile_size, self.tile_size), dtype=np.uint8)   # uint16: 65535
        # local var, no need self. ...
        # https://www.geeksforgeeks.org/numpy-concatenate-function-python/
        unit_tile_bw = np.concatenate((black_arr, white_arr), axis=1)
        unit_tile_wb = np.concatenate((white_arr, black_arr), axis=1)
        # A sample concatenate matrix black-white
        unit_tile = np.concatenate((unit_tile_bw, unit_tile_wb), axis=0)
        # Fill the image with the number of repetitions of unit tile
        num_of_tile = self.resolution // (2 * self.tile_size)   # Integer division
        # Store the pattern in the instance var output
        # np.tile - Creates an array by repeating
        # the specified array number of repetitions times (tuple)
        self.output = np.tile(unit_tile, (num_of_tile, num_of_tile))
        # Return an array copy of the given object
        result = np.copy(self.output)   # copy output to the result var
        return result

    def show(self):
        if self.output is not None:
            plt.imshow(self.draw(), cmap='gray')
            plt.axis()  # Hidden the axis
            plt.show()
        else:
            print("Call the draw() method to generate the circle first.")

# Cher = Checker(250, 25)
# Cher.draw()
# Cher.show()

class Circle:
    # Implement a constructor 3 int arguments: resolution, radius and position
    # Hint: using np.mesh grid
    # Define radius and center of a circle - then meshgrid - then circular mask

    def __init__(self, resolution, radius, position):
        self.resolution = resolution
        self.radius = radius
        self.position = position
        self.output = None  # Here is an instance var

        # Here to check: number of pixel must greater than twice of the radius
        # if self.resolution < (2*self.radius):
        #     print("Resolution must greater than twice of radius. Please try again!")
        #     print("The resolution is: ")
        #     self.resolution = int(input())  # Need to cast the typing, as str, to int

        # a method Draw creates the circle pattern as a numpy array
        # Store the pattern in the instance variable output and return a copy.
    def draw(self):
        # Create a black output matrix, value 0-black.
        self.output = np.zeros((self.resolution, self.resolution), dtype=np.uint8)
        # Calculate the center of the circle
        center_x, center_y = self.position
        # Generate a grid of coordinates
        x, y = np.meshgrid(np.arange(self.resolution), np.arange(self.resolution))
        # # Generate a grid of coordinates
        # x, y = (np.og rid[:self.resolution, :self.resolution])
        # Calculate the distance of each point from the center: all the points inside circle
        distance = (((x - center_x) ** 2 + (y - center_y) ** 2) <= self.radius**2)
        # Set pixels inside the circle to 1 (white) and keep the rest, outside, to 0 (black)
        self.output[distance] = 1
        # Make a copy and return it
        result = np.copy(self.output)
        return result

    def show(self):
        if self.output is not None:
            plt.imshow(self.draw(), cmap='gray')
            plt.axis('off')  # Hidden the axis
            plt.show()
        else:
            print("Call the draw() method to generate the circle first.")
pic = Circle(200, 20, (50,50))
pic.draw()
pic.show()

class Spectrum:
    # Implement a constructor 1 int arguments: resolution
    # Hint: using np.mesh grid

    def __init__(self, resolution):
        self.resolution = resolution
        self.output = None  # Here is an instance var

        # a method Draw creates the spectrum as a numpy array
        # RGB has 3 layers, channels that rising value from 0.0 - 1.0
        # Store the pattern in the instance variable output and return a copy

    def draw(self):
        # Create a rising array across a specific resolution
        rising_arr = np.linspace(0, 1, self.resolution)
        # Create each R - G - B plane
        # Red plane with self.resolution rows with 1. Then we have a matrix resolution x resolution
        # with each row is np.lin space(0, 1, self.resolution)
        r = np.tile(rising_arr, (self.resolution, 1))
        # Rotate r 90 to have g
        g = np.rot90(np.rot90(np.rot90(r)))
        # Rotate g 90 to have b
        b = np.rot90(np.rot90(r))
        # Combine all to become rgb matrix
        # v stack for vertical arrays, AAA. h Stack for horizontal. dstack for depth.
        self.output = np.dstack((r, g, b))
        # Return an array copy of the given object
        result = np.copy(self.output)  # copy output to the result var
        return result

    def show(self):
        if self.output is not None:
            plt.imshow(self.draw(), cmap='gray')
            plt.axis('off')  # Hidden the axis
            plt.show()
        else:
            print("Call the draw() method to generate the circle first.")


# Spec = Spectrum(100)
# Spec.draw()
# Spec.show()
