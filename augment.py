import cv2
import numpy as np
import random
import glob


def random_shift(image):
    rows,cols = image.shape[:2]
    M = np.float32([[1,0,random.uniform(-cols/8,cols/8)],[0,1,random.uniform(-rows/8,rows/8)]])
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

def random_brightness(image):
    image = image.astype(np.float32)
    brightness_coef = random.uniform(0.5, 1.5)
    image = image * brightness_coef
    image = np.clip(image, 0, 255)
    result = image.astype(np.uint8)
    return result

def generate_augmented_images(image):
    augmented_images = []
    for i in range(30):
        augmented_image = random_shift(image)
        augmented_image = random_color_change(augmented_image)
        augmented_image = random_noise(augmented_image)
        augmented_image = random_brightness(augmented_image)
        augmented_images.append(augmented_image)
    return augmented_images


# Load the original image
list_folder = glob.glob('*')
list_folder.remove("run.py")

for folder in list_folder:
    list_img = glob.glob(folder +'/*.jpg')
    for index, img in enumerate(list_img):
        image = cv2.imread(img)

        # Generate the augmented images
        augmented_images = generate_augmented_images(image)

        # Save the augmented images
        for i, augmented_image in enumerate(augmented_images):
            cv2.imwrite(folder + '/' + folder + str(index) +  str(i) + '_.jpg', augmented_image)