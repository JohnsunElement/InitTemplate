import os, sys
import cv2
import numpy as np
from os.path import basename, dirname, splitext
from tqdm import tqdm
from glob import glob
from argparse import ArgumentParser



if __name__ == '__main__':
    fd_model_list = ['scrfd', 'centeface', 'blazeface', 'opencv']
    lmk_model_list = ['scrfd', 'yin_cnn', 'PFLD']
    
    parser = ArgumentParser()
    parser.add_argument("--img", type=str, default=None)
    parser.add_argument("--VAL_src_dir", nargs='+',  default=[]) #  '/media/hermes/datashare/AWS-DataCollection/NORMAL'
    parser.add_argument("--INVAL_src_dir", nargs='+',  default=[])  # '/media/hermes/datashare/AWS-DataCollection/EXTREME_ANGLE/'
    parser.add_argument("-o","--out", type=str, default='')  
    args = parser.parse_args()