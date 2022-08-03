import json
import pandas as pd
import numpy as np

## Load the annotation data
### Download CoCo annotations from http://images.cocodataset.org/annotations/annotations_trainval2017.zip
### and put in a folder named coco_annotations in the current directory
cat_train_2017 = './coco_annotations/instances_train2017.json'
cat_val_2017 = './coco_annotations/instances_val2017.json'

with open(cat_train_2017,'r') as COCO:
    annot_train_2017 = json.loads(COCO.read())

with open(cat_val_2017,'r') as COCO:
    annot_val_2017 = json.loads(COCO.read())

## List of image_ids in each train and validation annotation datasets
train_image_ids = np.array([dic['image_id'] for dic in annot_train_2017['annotations']])
val_image_ids = np.array([dic['image_id'] for dic in annot_val_2017['annotations']])

## Load the trial info data
info_df = pd.read_csv('nsd_stim_info_merged.csv')

people_count = []
animal_count = []
for index, row in info_df.iterrows():
    ## Extract the CoCo categories for each image
    if row['cocoSplit'] == 'val2017':
        id_indices = np.argwhere(val_image_ids==row['cocoId'])
        categories = []
        for idx in id_indices.flatten():
            categories.append(annot_val_2017['annotations'][idx]['category_id'])
    elif row['cocoSplit'] == 'train2017':
        id_indices = np.argwhere(train_image_ids==row['cocoId'])
        categories = []
        for idx in id_indices.flatten():
            categories.append(annot_train_2017['annotations'][idx]['category_id'])
    categories = np.array(categories)

    ## Find the number of "person"(1) and "animal"(16-25) super-categories
    people_count.append(np.sum(categories==1))
    is_animal = (categories >= 16) & (categories <= 25)
    animal_count.append(np.sum(is_animal))

info_df['people_count'] = people_count
info_df['animal_count'] = animal_count

info_df.to_csv('stim_info_coco_annot.csv', index=False)
