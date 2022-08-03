import pandas as pd

def add_coco_annot(response_df):
    info_df = pd.read_csv('stim_info_coco_annot.csv')
    people_count = []
    animal_count = []
    for index, row in response_df.iterrows():
        people_count.append(info_df[info_df['nsdId'] == (row['73KID']-1)]['people_count'].values[0])
        animal_count.append(info_df[info_df['nsdId'] == (row['73KID']-1)]['animal_count'].values[0])
    del info_df
    response_df['people_count'] = people_count
    response_df['animal_count'] = animal_count
    return response_df

def add_manual_annot():
    pass


def main():
    ## Load the response data file
    response_df = pd.read_csv('subj01/behav/responses.tsv', sep='\t')
    coco_annotated_response_df = add_coco_annot(response_df)
    coco_annotated_response_df.to_csv('subj01/behav/coco_annot_response.tsv', sep='\t', index=False)

if __name__=="__main__":
    main()
