from cv2 import imread
from cv2 import CascadeClassifier
from cv2 import rectangle
from cv2 import imshow
from cv2 import waitKey
import os

DIRECTORY = 'images'
for filename in os.listdir(DIRECTORY):
	if filename.endswith(".jpg"):
		print(filename)
		# load the photograph
		pixels = imread(f'{DIRECTORY}/{filename}')
		# load the pre-trained model
		classifier = CascadeClassifier('haarcascade_frontalface_default.xml')
		# perform face detection
		bboxes = classifier.detectMultiScale(pixels)

		# delete multiface images and images without face
		if len(bboxes) > 1 or len(bboxes) == 0:
			if os.path.exists(f'{DIRECTORY}/{filename}'):
				os.remove(f'{DIRECTORY}/{filename}')
			else:
				print("The file does not exist")
		else:
			for box in bboxes:
				print(box)
				# get left-hand-bottom corner of box and its width and height
				x, y, width, height = box

				# delete images with face dimension less than 256x256
				if len(bboxes) == 1:
					if width < 256 or height < 256:
						if os.path.exists(f'{DIRECTORY}/{filename}'):
							os.remove(f'{DIRECTORY}/{filename}')
						else:
							print("The file does not exist")

# Покрутить картинки обработанные
