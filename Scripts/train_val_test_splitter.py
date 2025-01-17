import os
import shutil
import random

def split_dataset(input_dir, output_dir, train_ratio, val_ratio):
    # Validate the split ratios
    if train_ratio + val_ratio >= 1.0:
        raise ValueError("The sum of train_ratio and val_ratio must be less than 1.0.")

    # Define the paths for train, val, and test folders
    train_dir = os.path.join(output_dir, 'train')
    val_dir = os.path.join(output_dir, 'val')
    test_dir = os.path.join(output_dir, 'test')

    # Create train, val, and test directories if they don't exist
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # Iterate through each class in the input directory
    for class_name in os.listdir(input_dir):
        class_path = os.path.join(input_dir, class_name)

        # Skip if not a directory
        if not os.path.isdir(class_path):
            continue

        # Get all image file names for the class
        images = os.listdir(class_path)
        random.shuffle(images)

        # Calculate split points
        train_split = int(len(images) * train_ratio)
        val_split = int(len(images) * (train_ratio + val_ratio))

        train_images = images[:train_split]
        val_images = images[train_split:val_split]
        test_images = images[val_split:]

        # Create class directories in train, val, and test folders
        train_class_dir = os.path.join(train_dir, class_name)
        val_class_dir = os.path.join(val_dir, class_name)
        test_class_dir = os.path.join(test_dir, class_name)

        os.makedirs(train_class_dir, exist_ok=True)
        os.makedirs(val_class_dir, exist_ok=True)
        os.makedirs(test_class_dir, exist_ok=True)

        # Move the files to their respective directories
        for image in train_images:
            shutil.copy(os.path.join(class_path, image), os.path.join(train_class_dir, image))
        for image in val_images:
            shutil.copy(os.path.join(class_path, image), os.path.join(val_class_dir, image))
        for image in test_images:
            shutil.copy(os.path.join(class_path, image), os.path.join(test_class_dir, image))

    print(f"Dataset split complete. Train, val, and test datasets are in {output_dir}.")

# Example usage
# Specify the input dataset directory, output directory, and split ratios
input_dir = r"C:\Users\armaa\Desktop\Lab Computer Vision\Project\EuroSAT_RGB"
output_dir = r"C:\Users\armaa\Desktop\Lab Computer Vision\Project\EuroSAT_RGB_split_80.10.10"
train_ratio = 0.80  # 80% train
val_ratio = 0.10    # 10% validation

split_dataset(input_dir, output_dir, train_ratio, val_ratio)
