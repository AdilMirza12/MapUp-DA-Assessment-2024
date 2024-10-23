# Question 8: Time Check

import pandas as pd
from datetime import datetime, timedelta
WEEK_DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
def to_time(time_str):
    return datetime.strptime(time_str, '%H:%M:%S').time()
def check_time_completeness(df):
    completeness_status = {}
    grouped = df.groupby(['id', 'id_2'])
    for (id_val, id_2_val), group in grouped:
        days_covered = set()
        time_coverage = {day: [] for day in WEEK_DAYS}
        for _, row in group.iterrows():
            start_day, start_time = row['startDay'], to_time(row['startTime'])
            end_day, end_time = row['endDay'], to_time(row['endTime'])
            if start_day in WEEK_DAYS:
                days_covered.add(start_day)
                time_coverage[start_day].append((start_time, end_time))
            if end_day in WEEK_DAYS and end_day != start_day:
                days_covered.add(end_day)
                time_coverage[end_day].append((start_time, end_time))
        all_days_covered = len(days_covered) == 7
        all_times_covered = True
        for day in WEEK_DAYS:
            intervals = time_coverage[day]
            if not intervals:
                all_times_covered = False
                break
            intervals.sort(key=lambda x: x[0])
            current_time = datetime.strptime('00:00:00', '%H:%M:%S').time()
            for start, end in intervals:
                if current_time < start:
                    all_times_covered = False
                    break
                current_time = max(current_time, end)
            if current_time < to_time('23:59:59'):
                all_times_covered = False
        completeness_status[(id_val, id_2_val)] = not (all_days_covered and all_times_covered)
    result = pd.Series(completeness_status)
    result.index = pd.MultiIndex.from_tuples(result.index, names=['id', 'id_2'])
    
    return result
df = pd.read_csv('dataset-1.csv')
incorrect_timestamps = check_time_completeness(df)
print(incorrect_timestamps)
