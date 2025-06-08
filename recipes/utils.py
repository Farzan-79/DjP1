from django.core.exceptions import ValidationError
import pint
from pint.errors import UndefinedUnitError
from typing import Tuple
from fractions import Fraction
from pathlib import Path
import time

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
    
def recipe_image_upload_handler(instance, filename):
    fpath = Path(filename)
    ext = fpath.suffix.replace(" ","_")  # Includes the dot, e.g. ".jpg"
    clean_name = fpath.stem  # Filename without extension
    
    # Create organized path structure
    path = Path("recipes") / f"recipe_{instance.recipe.slug}"
    
    # Final filename: originalname_timestamp.ext
    new_filename = f"{clean_name}_{int(time.time())}{ext}"
    print(path)
    print(new_filename)
    return str(path / new_filename)