import json
import os
import re

paths = [['images/train2014/', 'annotations/captions_train2014.json'], ['images/val2014/', 'annotations/captions_val2014.json'], ['images/test2014/', 'annotations/captions_test2014.json']]


valid_id = set()
for i in range(len(paths)):
    (f1, f2) = paths[i]
    print('\nf1: ', f1, ', f2: ', f2)
    for root, dirs, files in os.walk(f1):
        for f in files:
            arr = re.split('_|\.', f)
            valid_id.add(int(arr[2]))
    print('valid id: ', len(valid_id))
    with open(f2, 'r') as json_file:
        data = json.load(json_file)
        ann = []
        for d in data['annotations']:
            if d['image_id'] in valid_id:
                ann.append(d)
        data['annotations'] = ann
        
        imgs = []
        for img in data['images']:
            if img['id'] in valid_id:
                imgs.append(img)
                if i == 0:
                    img['file_name'] = img['file_name'].replace('val2014', 'train2014')
                elif i == 2:
                    img['file_name'] = img['file_name'].replace('val2014', 'test2014')
        data['images'] = imgs
    print('imgs len: ', len(imgs))
    print('ann len: ', len(ann))
    with open(f2, 'w') as json_file:
        json.dump(data, json_file)
    valid_id = set()
    

