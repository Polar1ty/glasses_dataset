# Humans wearing glasses dataset🤓
Scripts for collecting pictures of humans wearing glasses.

## Before start:
- You need to prepare chrome webdriver of from **[chromedriver](https://chromedriver.chromium.org/downloads)** (You can check your chrome version in Help -> About Google Chrome).
- Clone pretrained model for face detection from this repo (.xml file).
- Also you need to install through pip needed packages as requests, PIL, selenium, cv2 (for last one write `pip install opencv-python`).

## Overview:
1. `scrape_images.py` - script for extracting pictures from google pictures by entering specific query (borrowed and modified from https://towardsdatascience.com/image-scraping-with-python-a96feda8af2d). Images will be stored in created "images" directory.
2. `preprocessing.py` - script which goes through scraped pictures, detects faces and removes those doesn't fit the rules.
  1. Only 1 face on 1 picture
  2. Each face at least 256x256 pixels
3. `rotate_flip.py` - script which rotates each correct image by 90, 180 and 270 degrees clockwise and flips them horizontally, verctically and both.

## How to reproduce:
Run `scrape_images.py` (modify or add some queries `search_terms` tuple before run if you want to). After images collected run `preprocessing.py` to remove those pictures which underfit the rules. In the end run `rotate_flip.py` for expanding dataset by rotating and flipping each picture. Final dataset with humans wearing 👓 will be stored in "images" directory.
