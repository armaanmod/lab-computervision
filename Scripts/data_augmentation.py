import albumentations as A
from albumentations.pytorch import ToTensorV2
import cv2
import os

# Define augmentations
augmentation_pipeline = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
    A.Rotate(limit=30, p=0.5),
    A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.1, rotate_limit=15, p=0.5),
    ToTensorV2()
])

# Apply augmentations
def augment_and_save(input_dir, output_dir, augmentation_pipeline, num_augmentations=2):
    for class_name in os.listdir(input_dir):
        class_path = os.path.join(input_dir, class_name)
        output_class_path = os.path.join(output_dir, class_name)
        os.makedirs(output_class_path, exist_ok=True)

        for image_name in os.listdir(class_path):
            image_path = os.path.join(class_path, image_name)
            image = cv2.imread(image_path)

            # Save original image
            cv2.imwrite(os.path.join(output_class_path, image_name), image)

            # Apply augmentations
            for i in range(num_augmentations):
                augmented = augmentation_pipeline(image=image)
                augmented_image = augmented['image']
                output_image_name = f"{os.path.splitext(image_name)[0]}_aug_{i}.jpg"
                cv2.imwrite(os.path.join(output_class_path, output_image_name), augmented_image)

# Example usage
train_input_dir = "path/to/split_dataset/train"
train_output_dir = "path/to/augmented_train_dataset"
augment_and_save(train_input_dir, train_output_dir, augmentation_pipeline, num_augmentations=3)
