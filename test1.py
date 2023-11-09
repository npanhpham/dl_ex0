black_arr = np.zeros((5, 5), dtype=np.uint8)  # uint8: 0-255
    white_arr = np.ones((self.tile_size, self.tile_size), dtype=np.uint8)   # uint16: 65535
    # local var, no need self. ...
    # https://www.geeksforgeeks.org/numpy-concatenate-function-python/
    unit_tile_bw = np.concatenate((black_arr, white_arr), axis=1)
    unit_tile_wb = np.concatenate((white_arr, black_arr), axis=1)