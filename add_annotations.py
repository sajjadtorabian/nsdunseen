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

def add_manual_annot(response_df):
    # motion_annotations = pd.read_csv('annot_app/motion_annotations.csv')
    interaction_annotations = pd.read_csv('annot_app/interaction_annotations.csv')
    tmp =  pd.merge(response_df, interaction_annotations, on="73KID", how="outer")
    # tmp =  pd.merge(tmp, motion_annotations, on="73KID", how="outer")
    return tmp

def add_shared1000(response_df):
    info_df = pd.read_csv('stim_info_coco_annot.csv')
    shared1000 = []
    for index, row in response_df.iterrows():
        shared1000.append(info_df[info_df['nsdId'] == (row['73KID']-1)]['shared1000'].values[0])
    del info_df
    response_df['shared1000'] = shared1000
    return response_df

def main():
    ## Load the response data file
    response_df = pd.read_csv('subj01/behav/responses.tsv', sep='\t')

    ## Add the CoCo annotations
    coco_annotated_response_df = add_coco_annot(response_df)

    ## Add the shared1000 column
    coco_annotated_shared1000_response_df = add_shared1000(coco_annotated_response_df)

    ## Add the manual annotations
    final_response_df = add_manual_annot(coco_annotated_shared1000_response_df)

    ## Save the final fully annotated and processed response file
    final_response_df.to_csv('subj01/behav/final_response.tsv', sep='\t', index=False)

if __name__=="__main__":
    ## TODO: take an argument from terminal that determines which subject data to process
    main()
