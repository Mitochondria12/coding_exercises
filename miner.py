from typing import List
from dataclasses import dataclass

# miner.py
class MathSynapse:
    def __init__(self, n_1, n_2, operation):
        self.n_1 = n_1
        self.n_2 = n_2
        self.operation = operation

class ExampleMiner:
    def forward(self, synapse):
        # Example miner logic: perform the operation
        try:
            return eval(f"{synapse.n_1} {synapse.operation} {synapse.n_2}")
        except ZeroDivisionError:
            return 'undefined'

def query_miners(data, batch_size=10):
    print('💬 Querying miners for data...')
    
    miner_results = []
    for i in range(0, len(data['n_1']), batch_size):
        batch_n_1 = data['n_1'][i:i + batch_size]
        batch_n_2 = data['n_2'][i:i + batch_size]
        batch_operands = data['operand'][i:i + batch_size]

        for n_1, n_2, operation in zip(batch_n_1, batch_n_2, batch_operands):
            synapse = MathSynapse(n_1, n_2, operation)
            miner_response = ExampleMiner().forward(synapse)
            miner_results.append(miner_response)
            print(f"Miner result: {miner_response}")
    
    return miner_results
