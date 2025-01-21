from django.core.exceptions import ValidationError
import pint
from pint.errors import UndefinedUnitError
from typing import Tuple
from fractions import Fraction

def valid_unit(unit:str):
    ureg = pint.UnitRegistry()
    myUnit = str(ureg.parse_expression(unit).units)
    try:
        return myUnit
    except:
        raise ValidationError('something went wrong in unit validation')

def valid_qty(quantity):
    qty = quantity
    qty = float(sum(Fraction(x) for x in f'{qty}'.split()))
    try:
        return float(round(qty, 2))
    except:
        raise ValidationError('something went wrong in quantity validation')