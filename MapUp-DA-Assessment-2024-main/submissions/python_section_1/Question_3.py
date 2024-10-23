# Question 3: Flatten a Nested Dictionary

def flatten_dict(d, parent_key='', result=None):
    if result is None:
        result = {}

    for key, value in d.items():
        new_key = f"{parent_key}.{key}" if parent_key else key 
        
        if isinstance(value, dict):
            flatten_dict(value, new_key, result)
        elif isinstance(value, list):
            for i, item in enumerate(value):
                flatten_dict({f"{key}[{i}]": item}, parent_key, result)
        else:
            result[new_key] = value

    return result
nested_dict = {
    "road": {
        "name": "Highway 1",
        "length": 350,
        "sections": [
            {
                "id": 1,
                "condition": {
                    "pavement": "good",
                    "traffic": "moderate"
                }
            }
        ]
    }
}

flattened = flatten_dict(nested_dict)
print(flattened)
