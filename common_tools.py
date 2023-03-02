import cv2
import os, sys
from glob import glob
from tqdm import tqdm

def Get_Image_List(data_dir_list):
    data_list = []
    for data_dir in data_dir_list:
        for data_path in glob(f'{data_dir}/*'):
            if os.path.isdir(data_path):
                data_list.extend( glob(f'{data_path}/*') )
            else:
                if data_path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
                    data_list.append(data_path)

    return data_list


def resize_with_pad(image, 
                    new_shape, 
                    padding_color = (255, 255, 255)):
    original_shape = (image.shape[1], image.shape[0])
    ratio = float(max(new_shape))/max(original_shape)
    new_size = tuple([int(x*ratio) for x in original_shape])
    image = cv2.resize(image, new_size)
    delta_w = new_shape[0] - new_size[0]
    delta_h = new_shape[1] - new_size[1]
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)
    image = cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=padding_color)
    return image

def load_image_bgr(fn):
    return cv2.imread(fn, cv2.IMREAD_COLOR) # in BGR

def save_jpeg( savedir, im, is_bgr = True, quality = 100):
    # grayscale or bgr, no color conversion is needed
    #if not os.path.exists()
    if len(im.shape) == 2 or is_bgr:
        cv2.imwrite(savedir, im, [int(cv2.IMWRITE_JPEG_QUALITY), quality])
    else:
        cv2.imwrite(savedir, cv2.cvtColor(im, cv2.COLOR_RGB2BGR), [int(cv2.IMWRITE_JPEG_QUALITY), quality])