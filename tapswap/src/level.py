import json
import os

@property
def levels():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'level_data.json')

    with open(file_path, 'r') as f:
        data = json.load(f)
    return data
