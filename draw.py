import pyautogui
import time

def draw_shape(region, shape, duration=0.101):
    """
    Draw a shape ('<', '>', '=') in the specified region.

    :param region: Tuple (x, y, width, height) specifying the region.
    :param shape: Shape to draw ('<', '>', '=').
    :param duration: Time in seconds to move between points.
    """
    x, y, width, height = region

    if shape == '<':
        points = [
            (x + width, y),
            (x, y + height // 2),
            (x + width, y + height)
        ]
    elif shape == '>':
        points = [
            (x, y),
            (x + width, y + height // 2),
            (x, y + height)
        ]
    elif shape == '=':
        points = [
            (x, y + height // 3),
            (x + width, y + height // 3),
            (x, y + 2 * height // 3),
            (x + width, y + 2 * height // 3)
        ]
    else:
        raise ValueError("Shape must be '<', '>', or '='")

    # Draw the shape by dragging the cursor through the points
    if shape == '=':
        pyautogui.moveTo(points[0][0], points[0][1], duration=duration)
        pyautogui.dragTo(points[1][0], points[1][1], duration=duration, button='left')
        pyautogui.moveTo(points[2][0], points[2][1], duration=duration)
        pyautogui.dragTo(points[3][0], points[3][1], duration=duration, button='left')
    else:
        pyautogui.moveTo(points[0][0], points[0][1], duration=duration)
        for point in points[1:]:
            pyautogui.dragTo(point[0], point[1], duration=duration, button='left')

if __name__ == '__main__':
    region = (1820, 1050, 50, 50)
    shape = 0
    time.sleep(2)
    draw_shape(region, shape)