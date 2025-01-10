from fractions import Fraction
from typing import Union, Tuple

def str_to_float(amount:str) -> (any, bool):
    
    success = False
    num = amount
    try:
        num = float(sum(Fraction(s) for s in f'{num}'.split()))
    except:
        pass
    if isinstance(num, float):
        success = True
    return(num, success)