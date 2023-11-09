# import os
# import numpy as np
# import matplotlib.pyplot as plt
# import json
# path = './exercise_data/'
# label = './Labels.json'
# #show file in directory
# contents =  os.listdir(path)
# with open(label, 'r') as json_file:
#             data = json.load(json_file)
# for i in contents:
#     (data[(i[:-4])])


import numpy as np
# import matplotlib.pyplot as plt
# path_image = './exercise_data/10.npy'
# #Load the .npy file
# loaded_array = np.load(path_image)
# #print array
# print(loaded_array)
#  #print image
# plt.imshow(loaded_array)
# plt.show()"""
# image = np.array([[[255, 0, 0], [0, 255, 0]],
#                   [[0, 0, 255], [255, 255, 255]]])
# images = image[:,::-1, :]
# print(images)


x, y = np.meshgrid(2,3)
print(x)
print(y)