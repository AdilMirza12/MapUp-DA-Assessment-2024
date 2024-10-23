# Question 9: Distance Matrix Calculation

import pandas as pd
import numpy as np
def calculate_distance_matrix(df):
    toll_ids = pd.concat([df['from_id'], df['to_id']]).unique()
    toll_ids.sort() 
    n = len(toll_ids)
    toll_index = {toll_id: idx for idx, toll_id in enumerate(toll_ids)}

    dist_matrix = np.full((n, n), np.inf)
    np.fill_diagonal(dist_matrix, 0)
    for _, row in df.iterrows():
        from_idx = toll_index[row['from_id']]
        to_idx = toll_index[row['to_id']]
        distance = row['distance']
        dist_matrix[from_idx, to_idx] = distance
        dist_matrix[to_idx, from_idx] = distance
    
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist_matrix[i, j] = min(dist_matrix[i, j], dist_matrix[i, k] + dist_matrix[k, j])
    
    dist_df = pd.DataFrame(dist_matrix, index=toll_ids, columns=toll_ids)
    
    return dist_df
df = pd.read_csv('dataset-2.csv')
distance_matrix = calculate_distance_matrix(df)
print(distance_matrix)
