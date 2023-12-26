import regex as re
from globals import PATH_TO_DAY_ONE

from utils import head

def findFirstAndLastNumberInLineAsNumber( line: str ) -> int:
  numbers = re.sub( r"\D", "", line )
  if len( numbers ) == 1:
    return int( numbers * 2 ) 
  
  elif len( numbers ) == 2:
    return int( numbers )
  
  first, last = numbers[0], numbers[-1]
  
  return int( first + last )

def day_1_a():
  with open( PATH_TO_DAY_ONE ) as file:
    processed = [ findFirstAndLastNumberInLineAsNumber(line) for line in file ]
    head( processed, 10 )
    print( sum( processed ) )
    