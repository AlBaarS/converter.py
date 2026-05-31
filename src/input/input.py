from typing import NamedTuple

class Input(NamedTuple):
    input_value: float
    raw_input_unit: str
    raw_output_unit: str
    decimals: int = -1
