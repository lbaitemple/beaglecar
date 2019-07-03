import cv2
import os
import time
import json
import numpy as np

from suiron import SuironIO
from suiron import Clock
# Load image settings
with open('settings.json') as d:
    SETTINGS = json.load(d)

# Instantiatees our IO class
suironio = SuironIO(id=0, width=SETTINGS['width'], height=SETTINGS['height'], depth=SETTINGS['depth'])
suironio.init_saving()

clck=Clock(suironio, 1)
clck.start() 

# Allows time for the camerae to warm up
print('Warming up...')
print('Recording data...')

while True:
    try:
        s={}
        s['motor']=1
        s['servo']=2
        suironio.record_inputs(s)
    except KeyboardInterrupt:
#        suironio.save_inputs()
        break
    

print('Saving file...')
suironio.save_inputs()
clck.stop()
