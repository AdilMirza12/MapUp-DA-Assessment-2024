# Question 10: Unroll Distance Matrix

import pandas as pd
def unroll_distance_matrix(dist_matrix):
    unrolled_data = []
    for id_start in dist_matrix.index:
        for id_end in dist_matrix.columns:
            if id_start != id_end:  
                distance = dist_matrix.loc[id_start, id_end]
                unrolled_data.append([id_start, id_end, distance])
    unrolled_df = pd.DataFrame(unrolled_data, columns=['id_start', 'id_end', 'distance'])
    
    return unrolled_df
unrolled_df = unroll_distance_matrix(distance_matrix)
print(unrolled_df)
