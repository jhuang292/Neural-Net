import json
import sys
import numpy as np

def preprocess_json(json_file_name):
    json_file_data = open(json_file_name, 'r')
    print(len(json_file_data))
        

if __name__ == '__main__':

        json_file_name = sys.argv[1]
        preprocess_json(json_file_name)
