from typing import List
from pydantic import BaseModel


class Container(BaseModel):
    containers: List[List[int]]

def calculate_min_moves(containers: List[List[int]]) -> int:
    from itertools import permutations
    types = [0, 1, 2]
    min_moves = float('inf')

    for assignment in permutations(types):
        moves = 0
        for cont_idx, correct_type in enumerate(assignment):
            container = containers[cont_idx]
            moves += sum(container) - container[correct_type]
        min_moves = min(min_moves, moves)

    return min_moves