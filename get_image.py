import pyautogui
import cv2
import numpy as np

def get_image(region, save_path):
    """
    get image from the specified region, process it and save it to the specified path
    :param region: example (0, 0, 300, 300)
    :param save_path: Path to save the processed image
    :return: Processed image as a numpy array
    """
    region_screenshot = pyautogui.screenshot(region=region)
    image = cv2.cvtColor(np.array(region_screenshot), cv2.COLOR_RGB2BGR)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
    binary_image = cv2.adaptiveThreshold(blurred_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    inverted_image = cv2.bitwise_not(binary_image)
    cv2.imwrite(save_path, inverted_image)
    return inverted_image

if __name__ == '__main__':
    region = (1950, 670, 90, 40)
    save_path = 'region_screenshot.png'
    get_image(region, save_path)
    print("Image saved and processed")