from django.core.exceptions import ValidationError
import pint
from pint.errors import UndefinedUnitError
from fractions import Fraction

def validate_unit(unit: str):
    ureg = pint.UnitRegistry()
    try:
        return str(ureg.parse_expression(unit).units)
    except (UndefinedUnitError, ZeroDivisionError):
        raise ValidationError(f'{unit} is not a valid unit')

def validate_qty(quantity: str):
    try:
        return float(sum(Fraction(x) for x in f'{quantity}'.split()))
    except (ZeroDivisionError, ValueError):
        raise ValidationError(f'{quantity} is not a valid quantity')