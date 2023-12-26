import regex as re
from globals import PATH_TO_DAY_TWO

from utils import head

NUMBERS = {
  "one":   "1",
  "two":   "2",
  "three": "3",
  "four":  "4",
  "five":  "5",
  "six":   "6",
  "seven": "7",
  "eight": "8",
  "nine":  "9",
}

def convertFirstAndLastWordsToNumbers( line: str ):
  search_results = re.findall(r"(?=("+'|'.join( NUMBERS.keys() )+r"))", line)
  
  if len( search_results ) == 0:
    return line
  
  first, last = search_results[0], search_results[-1]
  
  line = line.replace( first, NUMBERS.get( first ) + first )
  line = line.replace( last,  NUMBERS.get( last ) )
  
  return line
  

def findFirstAndLastNumberInLineAsNumber( line: str ) -> int:
  numbers = re.sub( r"\D", "", convertFirstAndLastWordsToNumbers( line ) )
  
  if len( numbers ) == 1:
    return int( numbers * 2 )
  elif len( numbers ) == 2:
    return int( numbers )
  
  first, last = numbers[0], numbers[-1]
  
  return int( first + last )

def day_1_b():
  with open( PATH_TO_DAY_TWO ) as file:
    processed = [ findFirstAndLastNumberInLineAsNumber( line.strip() ) for line in file ]
    print( sum( processed ) )