# Question 12: Calculate Toll Rate

import pandas as pd
def calculate_toll_rate(df):
    rate_coefficients = {
        'moto': 0.8,
        'car': 1.2,
        'rv': 1.5,
        'bus': 2.2,
        'truck': 3.6
    }
    for vehicle, coefficient in rate_coefficients.items():
        df[vehicle] = df['distance'] * coefficient
    return df
toll_rates_df = calculate_toll_rate(unrolled_df)
print(toll_rates_df)
