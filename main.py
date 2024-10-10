import get_image
import identify
import draw

n = 10 #题目数量

#自定义两个数的区域以及绘制区域
num1_region = (1800, 670, 86, 40)
num2_region = (1973, 670, 80, 40)
draw_region = (1820, 1050, 10, 10)

#用于确保识别速度与绘制速度一致
pre_num1 = 0
pre_num2 = 0

while True:
    get_image.get_image(num1_region, 'num1.png')
    get_image.get_image(num2_region, 'num2.png')

    num1 = identify.identify('num1.png')
    num2 = identify.identify('num2.png')

    if num1 == '' or num2 == '':
        continue

    num1 = int(num1)
    num2 = int(num2)

    print(f"识别到num1:{num1}, num2:{num2}")

    if num1 == pre_num1 and num2 == pre_num2:
        continue


    pre_num1 = num1
    pre_num2 = num2

    if num1 > num2:
        shape = '>'
    elif num1 < num2:
        shape = '<'
    else:
        shape = '='
    print(f"num1:{num1}, num2:{num2}，result:{shape}")
    draw.draw_shape(draw_region, shape)

    n -= 1
    if n == 0:
        break



