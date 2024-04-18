from typing import List
from dataclasses import dataclass

@dataclass
class MathSynapse:
    n_1:float = 0
    n_2:float = 0
    operand: str = ''
    
   
class ExampleMiner:
    def __init__(self):
        self.name = "ExampleMiner"

    # Note that you can modify the forward method to accept a list of synapses to perform batch processing
    def forward(synapse: MathSynapse): 
        ...
