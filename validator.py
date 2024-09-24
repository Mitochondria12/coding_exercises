# validator.py
import time
import math
from dataset import load_dataset
from miner import query_miners

def generate_reference(data, batch_size=10):
    print('📝 Generating reference...')
    references = []

    for i in range(0, len(data['n_1']), batch_size):
        batch_n_1 = data['n_1'][i:i + batch_size]
        batch_n_2 = data['n_2'][i:i + batch_size]
        batch_operands = data['operand'][i:i + batch_size]
        
        for n_1, n_2, operation in zip(batch_n_1, batch_n_2, batch_operands):
            try:
                if operation == '/' and n_2 == 0:
                    result = 'undefined (division by zero)'
                else:
                    result = eval(f"{n_1} {operation} {n_2}")
                references.append(result)
                print(f"Reference for {n_1} {operation} {n_2} = {result}")
            except Exception as e:
                print(f"Error processing {n_1} {operation} {n_2}: {e}")
    
    return references

def reward_miners(reference, miner_results, max_reward=10):
    print('💰 Rewarding miners...')

    batch_total_reward = 0
    tolerance = 0.01  # Define a tolerance level to avoid extremely small rewards

    def compute_reward(reference, miner_result, max_reward):
        error = abs(reference - miner_result)
        if error == 0:
            return max_reward
        decay_rate = 5  # Adjust decay rate
        reward = max_reward * math.exp(-decay_rate * error)
        return reward if reward > tolerance else 0

    for ref, miner_result in zip(reference, miner_results):
        reward = compute_reward(ref, miner_result, max_reward)
        batch_total_reward += reward
        print(f"Reference: {ref}, Miner Result: {miner_result}, Reward: {reward}")

    print(f'Total batch reward: {batch_total_reward}')
    return batch_total_reward

def execute_validator_step(data):
    # Generate reference values from data
    reference = generate_reference(data)
    
    # Query miners to get their results
    miner_results = query_miners(data)
    
    # Reward the miners based on the reference and their results
    results = reward_miners(reference, miner_results)
    print('Results:', results)

if __name__ == '__main__':
    print('Starting validator execution...')
    
    # Load the dataset
    dataset_iterator = load_dataset()

    # Print the first few items from the dataset iterator
    for i, data in enumerate(dataset_iterator):
        batch_data = {'n_1': [item['n_1'] for item in data],'n_2': [item['n_2'] for item in data],'operand': [item['operand'] for item in data]}
    
    # Run the validator step every 2 seconds
    while True:        
        execute_validator_step(batch_data)
        time.sleep(2)
