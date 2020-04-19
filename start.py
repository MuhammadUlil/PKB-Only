from mnist import MNIST
import numpy as np 

mndata = MNIST('./data')
images, labels = mndata.load_training()
t_images, t_labels = mndata.load_testing()

