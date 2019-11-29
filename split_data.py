import os
import shutil
import math
import re
import json


TRAIN_DIR = 'images/train2014/'
VAL_DIR = 'images/val2014/'
TEST_DIR = 'images/test2014/'

os.mkdir(TRAIN_DIR)
os.mkdir(VAL_DIR)
os.mkdir(TEST_DIR)

count = 30000
removed_f = open('removed_id.txt', 'w')
for root, dirs, files in os.walk('images'):
    i = 0
    removed_count = len(files) - count 
    for f in files:
        if i < removed_count:
            arr = re.split('_|\.', f)
            removed_f.write(str(int(arr[2])) + '\n')
            os.remove('images/'+f)
        elif i < removed_count + math.floor(0.64 * count):
            # train
            nf = f.replace('val', 'train')
            os.rename('images/'+f, TRAIN_DIR+nf)
        elif i < removed_count + math.floor(0.8 * count):
            # val
            nf = f
            #os.rename('images/'+f, VAL_DIR+nf)
            os.rename('images/'+f, VAL_DtIR+nf)
        else:
            # test
            nf = f.replace('val', 'test')
            os.rename('images/'+f, TEST_DIR+nf)
        i += 1
    break
removed_f.close()

removed_id = set()
with open('removed_id.txt', 'r') as removed_f:
    for line in removed_f:
        image_id = int(line)
        removed_id.add(image_id)

shutil.copyfile('annotations/captions_val2014.json', 'annotations/captions_train2014.json')
shutil.copyfile('annotations/captions_val2014.json', 'annotations/captions_test2014.json')
