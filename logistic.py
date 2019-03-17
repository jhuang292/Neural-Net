import json
import sys
import numpy as np

def preprocess_json(json_file_name):
    
    with open(json_file_name, 'r') as f:
        json_dict = json.load(f)
    json_data = json_dict['data']
    json_features = json_dict['metadata']['features']
    for item in json_features:
        if item[1] != 'numeric':
            print(1)
        else:
            print(0)

if __name__ == '__main__':

        json_file_name = sys.argv[1]
        preprocess_json(json_file_name)
