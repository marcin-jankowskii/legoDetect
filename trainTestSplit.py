import os
import shutil
from sklearn.model_selection import train_test_split

def train_test_split_images_labels(images_dir, labels_dir, train_dir, valid_dir, test_dir, test_size=0.2, valid_size=0.25):
    # Get all files in the images and labels directories
    images = os.listdir(images_dir)
    labels = os.listdir(labels_dir)

    # Split the data into training and testing
    images_train, images_test, labels_train, labels_test = train_test_split(images, labels, test_size=test_size, random_state=42)

    # Split the training data into training and validation
    images_train, images_valid, labels_train, labels_valid = train_test_split(images_train, labels_train, test_size=valid_size, random_state=42)

    # Function to copy files
    def copy_files(files, src_dir, dst_dir):
        for file in files:
            shutil.copy(os.path.join(src_dir, file), os.path.join(dst_dir, file))

    # Copy files
    copy_files(images_train, images_dir, os.path.join(train_dir, 'images'))
    copy_files(images_valid, images_dir, os.path.join(valid_dir, 'images'))
    copy_files(images_test, images_dir, os.path.join(test_dir, 'images'))

    copy_files(labels_train, labels_dir, os.path.join(train_dir, 'labels'))
    copy_files(labels_valid, labels_dir, os.path.join(valid_dir, 'labels'))
    copy_files(labels_test, labels_dir, os.path.join(test_dir, 'labels'))

# Usage
train_test_split_images_labels('allSet\\images', 'allSet\\labels', 'Dataset\\train', 'Dataset\\valid', 'Dataset\\test')