"""
This file contains functions that extract the manual annotations from jspsych outputs
"""

import pandas as pd

def extract_motion_levels(motion_df):
    image_id = []
    motion_level = []
    for index, row in motion_df.iterrows():
        if index > 0:
            image_id.append(int(row['stimulus'].split('/')[1].split('.')[0]))
            motion_level.append(int(row['response']))
    motion_output = pd.DataFrame({'73KID': image_id, 'motion_level': motion_level})
    return motion_output


def extract_interaction_types(interaction_df):
    image_id = []
    interaction_type = []
    for index, row in interaction_df.iterrows():
        if index > 0:
            image_id.append(int(row['stimulus'].split('/')[1].split('.')[0]))
            if row['response']=='0':
                interaction_type.append('Unrelated people')
            elif row['response']=='1':
                interaction_type.append('Joint attention')
            elif row['response']=='2':
                interaction_type.append('Social interaction')
    interaction_output = pd.DataFrame({'73KID': image_id, 'interaction_type': interaction_type})
    return interaction_output


def main():
    ## Load the apps' output files
    motion_df = pd.read_csv('motion.csv')
    interaction_df = pd.read_csv('interaction.csv')

    ## Extract the ratings for each image id
    # motion_output = extract_motion_levels(motion_df)
    interaction_output = extract_interaction_types(interaction_df)

    ## Save the annotations
    # motion_output.to_csv('motion_annotations.csv', index=False)
    interaction_output.to_csv('interaction_annotations.csv', index=False)

if __name__=="__main__":
    main()
