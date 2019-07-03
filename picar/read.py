import cv2
from suiron import get_servo_dataset
import sys
from PIL import Image
import numpy as np

d='output_7.csv'

c_x, c_s=get_servo_dataset(d)
print(len(c_x))
#im=Image.fromarray(c_x[int(sys.argv[1])])
im=Image.fromarray(np.uint8(c_x[22]))
im.save('new.jpg')
#print(c_x)
