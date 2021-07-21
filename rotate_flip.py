import cv2
from cv2 import imread
import os

DIRECTORY = 'images'
for filename in os.listdir(DIRECTORY):
    if filename.endswith(".jpg"):
        img = imread(f'{DIRECTORY}/{filename}')

        # Rotate 90 clockwise
        img_rotated_90_clockwise = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(f'{DIRECTORY}/{filename}_rotated_90_clockwise.jpg', img_rotated_90_clockwise)

        # Rotate 180 clockwise
        img_rotated_180_clockwise = cv2.rotate(img_rotated_90_clockwise, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(f'{DIRECTORY}/{filename}_rotated_180_clockwise.jpg', img_rotated_180_clockwise)

        # Rotate 270 clockwise
        img_rotated_270_clockwise = cv2.rotate(img_rotated_180_clockwise, cv2.ROTATE_90_CLOCKWISE)
        cv2.imwrite(f'{DIRECTORY}/{filename}_rotated_270_clockwise.jpg', img_rotated_270_clockwise)

        # Flip vertically
        img_flipped_v = cv2.flip(img, 0)
        cv2.imwrite(f'{DIRECTORY}/{filename}_flipped_vertically.jpg', img_flipped_v)

        # Flip horizontally
        img_flipped_h = cv2.flip(img, 1)
        cv2.imwrite(f'{DIRECTORY}/{filename}_flipped_horizontally.jpg', img_flipped_h)

        # Flip both vertically and horizontally
        img_flipped_vh = cv2.flip(img, -1)
        cv2.imwrite(f'{DIRECTORY}/{filename}_flipped_both.jpg', img_flipped_vh)