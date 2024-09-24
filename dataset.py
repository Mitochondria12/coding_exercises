# dataset.py
from datasets import load_dataset

def load_dataset():
    print('Retrieving data from Hugging Face...')

    # Load the dataset from Hugging Face (this loads the 'train' split by default)
    dataset = load_dataset('synapse-alpha/coding_exercises', split='train')

    # Convert the dataset to a format that your application expects (a dictionary with 'n_1', 'n_2', 'operand')
    data = {
        'n_1': [item['n_1'] for item in dataset],
        'n_2': [item['n_2'] for item in dataset],
        'operand': [item['operand'] for item in dataset]
    }

    return data
