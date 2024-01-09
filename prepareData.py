from PIL import Image, ImageChops
import os
import cv2
import numpy as np

IMAGE_FILE_DIRECTORY = 'allSet\images'
FRAME_COUNT =  40   #number of images per data label

def create_single_bounding_box(image_path):
    # Wczytanie obrazu
    image = cv2.imread(image_path)
    if image is None:
        return "Nie można wczytać obrazu."

    # Pobieranie rozmiarów obrazu
    height, width = image.shape[:2]

    # Konwersja do przestrzeni barw HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Definiowanie zakresów koloru czerwonego w przestrzeni HSV
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])

    # Tworzenie masek dla czerwonego koloru
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    # Dylatacja maski, aby połączyć bliskie sobie obszary
    kernel = np.ones((10,10),np.uint8)  # Możesz dostosować rozmiar jądra
    dilated_mask = cv2.dilate(mask, kernel, iterations=1)

    # Znalezienie konturów
    contours, _ = cv2.findContours(dilated_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # Znalezienie największego konturu (głównego obiektu)
        largest_contour = max(contours, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(largest_contour)

        # Znormalizowanie współrzędnych bounding boxa
        x_center = (x + w / 2) / width
        y_center = (y + h / 2) / height
        w_norm = w / width
        h_norm = h / height

    return [x_center, y_center, w_norm, h_norm]
 


def getImages():
    fileNames = [fileName for fileName in os.listdir(IMAGE_FILE_DIRECTORY) if fileName.endswith(".png")]
    fileNames.sort(key=lambda name: int(name.split('.')[0]))
    return fileNames

def constructTrainingFile():
    tempCount =  1
    imageFiles = getImages()


    for image in imageFiles:
        name = image.split('.')[0]
        file = open(f"allSet\labels\{name}.txt","w")
        im =  Image.open(IMAGE_FILE_DIRECTORY + '/' + image)
        bbox = create_single_bounding_box(IMAGE_FILE_DIRECTORY + '/' + image)
        #bbox = [0.5,0.5,0.5,0.5]
        line = str(tempCount//FRAME_COUNT) +' ' +' '.join(map(str,bbox))
        file.write(line)
        file.close()
        tempCount = tempCount + 1
constructTrainingFile()