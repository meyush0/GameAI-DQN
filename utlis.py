##   images from the environment are processed and fed into a neural network, and where proper weight initialization 

import cv2
import torch
import torch.nn as nn
import numpy as np


device = 'cuda' if torch.cuda.is_available() else 'cpu'


import cv2
import numpy as np
import torch

device = 'cuda' if torch.cuda.is_available() else 'cpu'

def preprocessing(image):
    if image is None:
        raise ValueError("Input image is None")
    
    # Convert to grayscale and resize
    image_data = cv2.cvtColor(cv2.resize(image, (84, 84)), cv2.COLOR_BGR2GRAY)
    # Binarize image
    image_data[image_data > 0] = 255
    # Reshape and convert to tensor
    image_data = np.reshape(image_data, (84, 84, 1))
    # image_tensor = image_data.transpose(2, 0, 1).astype(np.float32)
    image_tensor = torch.from_numpy(image_data.transpose(2, 0, 1).astype(np.float32)).to(device)

    return image_tensor


def init_weights(m):
    if type(m) == nn.Conv2d or type(m) == nn.Linear:
        torch.nn.init.uniform(m.weight, -0.01, 0.01)
        m.bias.data.fill_(0.01)