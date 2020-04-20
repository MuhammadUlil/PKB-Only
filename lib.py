import numpy as np

mndata = MNIST('./data')
images, labels = mndata.load_training()
t_images, t_labels = mndata.load_testing()

images = np.array(images)
t_images = np.array(t_images)
labels = np.array(labels)
t_labels = np.array(t_labels)

print("statistics for testing") 

for i in range(num_class):
    print("class", i, "instances: ", np.sum(t_labels==i))