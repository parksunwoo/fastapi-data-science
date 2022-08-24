from typing import List, Union

l: List[Union[int, float]] = [1, 2.5, 3.14, 5]

def greeting(name: Union[str, None] = None) -> str:
    return f"Hello, {name if name else 'Anonymous'}"
