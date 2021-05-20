from statistics import mean
from typing import List

def extract_dict(trackeval_dict : dict) -> List[dict]:
    # Initialize hota/count score list
    hota_score_list : List[dict] = []
    # Extract informations of interest
    hota_score : dict = trackeval_dict['MotChallenge2DBox']['dataset_train']
    del hota_score['COMBINED_SEQ']
    
    # Browse for every sequence 
    for i in range(len(hota_score)):
        # Format score
        hota_score_temp : dict= hota_score['seq_{!s}'.format(i+1)]['pedestrian']['HOTA']
        # Remove unrelevent keys
        del hota_score_temp['HOTA(0)']
        del hota_score_temp['LocA(0)']
        del hota_score_temp['HOTALocA(0)']
        del hota_score_temp['RHOTA']
        for key in hota_score_temp.keys():
            hota_score_temp[key] = mean(hota_score_temp[key])
        
        # Add count keys to HOTA dict
        count_score_temp : dict = hota_score['seq_{!s}'.format(i+1)]['pedestrian']['Count']
        for key in count_score_temp.keys():
            hota_score_temp[key] = count_score_temp[key]

        # Append score hota
        hota_score_list.append(hota_score_temp)
    
    return hota_score_list
 
    
