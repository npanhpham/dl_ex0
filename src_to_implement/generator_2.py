import os.path
import json
import scipy.misc
import numpy as np
import matplotlib.pyplot as plt
import os
import random
import scipy
import math
import skimage

# In this exercise task you will implement an image generator. Generator objects in python are defined as having a next function.
# This next function returns the next generated object. In our case it returns the input of a neural network each time it gets called.
# This input consists of a batch of images and its corresponding labels.
class ImageGenerator:
    def __init__(self, file_path, label_path, batch_size, image_size, rotation=False, mirroring=False, shuffle=False):
        # Define all members of your generator class object as global members here.
        # These need to include:
        # the batch size
        # the image size
        # flags for different augmentations and whether the data should be shuffled for each epoch
        # Also depending on the size of your data-set you can consider loading all images into memory here already.
        # The labels are stored in json format and can be directly loaded as dictionary.
        # Note that the file names correspond to the dicts of the label dictionary.

        self.class_dict = {0: 'airplane', 1: 'automobile', 2: 'bird', 3: 'cat', 4: 'deer', 5: 'dog', 6: 'frog',
                           7: 'horse', 8: 'ship', 9: 'truck'}
        self.data = [] # array of (image array, label)
        with open(label_path, 'r') as fpath:  #label_path: path to JSON file  #fpath: file object 
            self.labels = json.load(fpath)  #load the dictionary from Labels.json

            #file path: directory to all images: exercise_data
        for img_file in os.listdir(file_path): #return a list of all file under file path, the elements are file names
            img_full_path = os.path.join(file_path, img_file) #add an additional path for directory to each image 
            img_array = np.load(img_full_path)
            self.data.append((img_array, self.labels[img_file[:-len(".npy")]])) # take labels from file name without suffix
        self.batch_size = batch_size
        self.image_size = image_size
        self.rotation = rotation
        self.mirroring = mirroring
        self.shuffle = shuffle
        if self.shuffle:
            random.shuffle(self.data) # shuffle data
        self.current_index = 0 # current start image index of next batch
        self.epoch = -1 # current epoch in training, -1 because first epoch is 0

    def next(self):
        # This function creates a batch of images and corresponding labels and returns them.
        # In this context a "batch" of images just means a bunch, say 10 images that are forwarded at once.
        # Note that your amount of total data might not be divisible without remainder with the batch_size.
        # Think about how to handle such cases
        #TODO: implement next method
        if self.current_index < self.batch_size: # if index at the beginning is less than batch size -> begin of new epoch
            self.epoch += 1
        reset_index_to_0 = False # reset the index to 0 in case of shuffling and end of epoch
        
        #CASE 1: Data size is divisible by batch size
        if self.current_index + self.batch_size <= len(self.data):
            next_batch = self.data[self.current_index:self.current_index+self.batch_size] 
            if self.current_index + self.batch_size == len(self.data):
                if self.shuffle:
                    random.shuffle(self.data)
        
        #CASE 2: Data size is not divisible by batch size
        else:
            offset = self.current_index + self.batch_size - len(self.data) #remainder for the next epoch
            next_batch = self.data[self.current_index:] #remainder of the last batch of previous epoch
            #If shuffle = Reset index
            if self.shuffle:
                random.shuffle(self.data) 
                reset_index_to_0 = True  
            #If no shuffle = reusing images from the beginning
            else:
                next_batch += self.data[:offset] 
        images = []
        labels = []
        for img, label in next_batch:
            img = skimage.transform.resize(img, self.image_size)
            img = self.augment(img)
            images.append(img)
            labels.append(label)
        if reset_index_to_0:
            self.current_index = 0
        else:
            self.current_index = (self.current_index + self.batch_size) % len(self.data) # move self.current_index to beginning of next batch

        return np.array(images), np.array(labels) # numpy arrays

    def augment(self, img):
        # this function takes a single image as an input and performs a random transformation
        # (mirroring and/or rotation) on it and outputs the transformed image
        #TODO: implement augmentation function
        if self.mirroring:
            axis = random.choice(['x', 'y', None]) # randomly select an image axis to flip
            if axis == 'x':
                img = img[:,::-1,:]
            elif axis == 'y':
                img = img[::-1,:,:]
            # don't rotate if axis is None
        if self.rotation:
            angle = random.choice([90, 180, 270]) # randomly select an angle to rotate
            img = scipy.ndimage.rotate(img, angle)
        return img

    def current_epoch(self):
        # return the current epoch number
        return self.epoch

    def class_name(self, x):
        # This function returns the class name for a specific input
        #TODO: implement class name function
        return self.class_dict[x]

    def show(self):
        images, labels = self.next()
        PLOT_COLS = 3 # number of columns in the
        fig, axs = plt.subplots(nrows=math.ceil(len(images)/PLOT_COLS), ncols=PLOT_COLS)
        plt.subplots_adjust(hspace=1.)
        plt.axis('off') # turn off x, y axes
        for i in range(len(images)):
            x, y = i // PLOT_COLS, i % PLOT_COLS
            axs[x, y].set_title(self.class_name(labels[i]))
            axs[x, y].imshow(images[i])
            axs[x, y].axis('off')
        plt.show()
