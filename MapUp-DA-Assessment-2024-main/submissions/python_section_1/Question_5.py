# Question 5: Find All Dates in a Text

import re

def find_all_dates(text):
    date_pattern = r"\b(\d{2}-\d{2}-\d{4})\b|\b(\d{2}/\d{2}/\d{4})\b|\b(\d{4}\.\d{2}\.\d{2})\b"
    matches = re.findall(date_pattern, text)
    dates = [date for match in matches for date in match if date]
    return dates
text = "I was born on 23-08-1994, my friend on 08/23/1994, and another one on 1994.08.23."
print(find_all_dates(text))
