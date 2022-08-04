"""
Functions that separate the images containing people and animals, in order to use in the manual annotation app
"""

import pandas as pd

def separate_people_images(stim_info, threshold_num):
    people_img_ids = stim_info[stim_info['people_count'] >= threshold_num]['nsdId'] + 1
    return people_img_ids.tolist()

def separate_animal_images(stim_info, threshold_num):
    animal_img_ids = stim_info[stim_info['animal_count'] >= threshold_num]['nsdId'] + 1
    return animal_img_ids.tolist()


def main():
    ## Load the response data file
    stim_info_coco_annot = pd.read_csv('stim_info_coco_annot.csv')
    stim_info_shared1000 = stim_info_coco_annot[stim_info_coco_annot['shared1000']]
    people_indices = separate_people_images(stim_info_shared1000, 1)
    social_indices = separate_people_images(stim_info_shared1000, 2)
    animal_indices = separate_animal_images(stim_info_shared1000, 1)

    print(f"Indices of images with at least one person = {people_indices}")
    print(f"Indices of images with at least two people = {social_indices}")
    print(f"Indices of images with at least one animal = {animal_indices}")

if __name__=="__main__":
    main()
