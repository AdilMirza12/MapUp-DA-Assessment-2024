# Question 11: Finding IDs within Percentage Threshold

import pandas as pd
import numpy as np

def find_ids_within_ten_percentage_threshold(df, reference_id):
    average_distance = df[df['id_start'] == reference_id]['distance'].mean()
    lower_bound = average_distance * 0.9
    upper_bound = average_distance * 1.1
    filtered_ids = df[(df['distance'] >= lower_bound) & (df['distance'] <= upper_bound)]['id_start'].unique()ds
    return sorted(filtered_ids)
reference_id = 'A'
ids_within_threshold = find_ids_within_ten_percentage_threshold(unrolled_df, reference_id)
print(ids_within_threshold)
