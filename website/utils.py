import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

def draw_bounding_box(img_path, c):
    '''
    Recieve image path and
    '''
    img = cv2.imread('.' + img_path)
    color_box = (255, 255, 255)
    color_text = (0, 0, 0)
    thickness = 2

    font = "Arial Unicode.ttf"
    font_text = ImageFont.truetype(font=font, size=32)

    for box in c:
        img = cv2.fillPoly(img, [np.array(box['vertices'], dtype=np.int32)], color_box)

        img_pil = Image.fromarray(img)
        draw = ImageDraw.Draw(img_pil)
        draw.text((box['vertices'][0][0]+5, box['vertices'][0][1]+5), box['text'], font=font_text, fill=color_text)
        img = np.array(img_pil)

    # im_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    x = img_path.rfind(".")
    new_path = '.' + img_path[:x] + '_edit' + img_path[x:]

    cv2.imwrite(new_path, img)

    return new_path

# if __name__ == '__main__':
#     draw_bounding_box('/uploads/sample.jpg', c)
