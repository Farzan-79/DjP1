from django.core.exceptions import ValidationError
import pint
from pint.errors import UndefinedUnitError

def validate_unit(unit):
    ureg = pint.UnitRegistry()
    try:
        myUnit = ureg.parse_expression(unit).units
    except UndefinedUnitError:
        raise ValidationError(f'{unit} is not a valid unit')
    #return myUnit