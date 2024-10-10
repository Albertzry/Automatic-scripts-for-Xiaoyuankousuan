import pytesseract
from PIL import Image

def identify(image):
    """
    Identify the number in the image
    :param image: get data from get_image.py
    :return: string of the number
    """
    text = pytesseract.image_to_string(image, config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    return text

if __name__ == '__main__':
    image = Image.open('num1.png')
    print(identify(image))
