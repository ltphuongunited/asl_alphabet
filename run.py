import cv2
import numpy as np
import random
import glob

def random_rotation(image):
    rows,cols = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((cols/2,rows/2),random.uniform(-30,30),1)
    result = cv2.warpAffine(image, rotation_matrix, (cols,rows))
    return result

def random_shift(image):
    rows,cols = image.shape[:2]
    M = np.float32([[1,0,random.uniform(-cols/100,cols/100)],[0,1,random.uniform(-rows/100,rows/100)]])
    result = cv2.warpAffine(image,M,(cols,rows))
    return result

def random_color_change(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv[:,:,0] = hsv[:,:,0] * random.uniform(0.5, 1.5)
    hsv[:,:,1] = hsv[:,:,1] * random.uniform(0.5, 1.5)
    hsv[:,:,2] = hsv[:,:,2] * random.uniform(0.5, 1.5)
    result = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return result

def random_noise(image):
    mean = 0
    var = 0.1
    sigma = var**0.5
    gaussian = np.random.normal(mean, sigma, image.shape)
    noisy_image = image + gaussian
    return noisy_image

def generate_augmented_images(image):
    augmented_images = []
    for i in range(50):
        augmented_image = random_rotation(image)
        augmented_image = random_shift(augmented_image)
        augmented_image = random_color_change(augmented_image)
        augmented_image = random_noise(augmented_image)
        augmented_images.append(augmented_image)
    return augmented_images


# Load the original image
# list_folder = glob.glob('*')
# list_folder.remove("run.py")
list_folder = ['P','M','N','F','G','H','J']
for folder in list_folder:
    image = cv2.imread(folder + '/'+ folder + '.jpg')

    # Generate the augmented images
    augmented_images = generate_augmented_images(image)

    # Save the augmented images
    for i, augmented_image in enumerate(augmented_images):
        cv2.imwrite(folder + '/' + folder + str(i) + '.jpg', augmented_image)