# Question 12: Calculate Toll Rate

import pandas as pd
import numpy as np
from datetime import time

def calculate_time_based_toll_rates(df):
    weekday_discount = {
        'morning': 0.8, 
        'day': 1.2,      
        'evening': 0.8  
    }
    weekend_discount = 0.7
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    df['start_day'] = np.random.choice(days_of_week, len(df))
    df['end_day'] = np.random.choice(days_of_week, len(df))
    df['start_time'] = pd.to_datetime(np.random.choice(pd.date_range("00:00", "23:59", freq='H').time, len(df))).dt.time
    df['end_time'] = pd.to_datetime(np.random.choice(pd.date_range("00:00", "23:59", freq='H').time, len(df))).dt.time
    for index, row in df.iterrows():
        start_day = row['start_day']
        end_day = row['end_day']
        start_time = row['start_time']
        end_time = row['end_time']
        
        if start_day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]:  # Weekdays
            if time(0, 0) <= start_time <= time(10, 0):
                discount_factor = weekday_discount['morning']
            elif time(10, 0) < start_time <= time(18, 0):
                discount_factor = weekday_discount['day']
            else:
                discount_factor = weekday_discount['evening']
        else: 
            discount_factor = weekend_discount
        for vehicle in ['moto', 'car', 'rv', 'bus', 'truck']:
            df.at[index, vehicle] *= discount_factor
    return df
time_based_toll_rates_df = calculate_time_based_toll_rates(toll_rates_df)
print(time_based_toll_rates_df)
