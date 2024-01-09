from PIL import Image, ImageChops
import os

IMAGE_FILE_DIRECTORY = 'Dataset\images'
FRAME_COUNT =  40   #number of images per data label


def getImages():
    fileNames = [fileName for fileName in os.listdir(IMAGE_FILE_DIRECTORY) if fileName.endswith(".png")]
    fileNames.sort(key=lambda name: int(name.split('.')[0]))
    return fileNames

def constructTrainingFile():
    tempCount =  1
    imageFiles = getImages()


    for image in imageFiles:
        name = image.split('.')[0]
        file = open(f"Dataset\labels\{name}.txt","w")
        im =  Image.open(IMAGE_FILE_DIRECTORY + '/' + image)
        bbox = [0.5,0.5,0.5,0.5]
        line = str(tempCount//FRAME_COUNT) +' ' +' '.join(map(str,bbox))
        file.write(line)
        file.close()
        tempCount = tempCount + 1
constructTrainingFile()