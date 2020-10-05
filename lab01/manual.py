from typing import Tuple, List, Callable

def get_stable_pairs(f: Callable[[float, float], float], N: int, a: float, b: float) -> List[Tuple[float, float]]:
    h: float = (b - a)/N

    
