import pandas as pd
import numpy as np


def average_steps(filename):
    df = pd.read_csv("./data/"+filename+".csv")
    print(filename)
    return df.groupby(['tag']).agg('mean').to_dict()['n_steps']

def queue_func(input_, output):
    for filename in iter(input_.get, 'STOP'):
        result = average_steps(filename)
        output.put(result)
        
def combine_results(data):
    temp = {}
    for _, tag in data.items():
        for key, value in tag.items():
            if key not in temp:
                temp[key] = []
            temp[key].append(value)

    combined = {}
    for k, v in temp.items():
        combined[k] = np.mean(v)
    return combined
