"""
Determine the ASCII code for the current character of the string.
Increase the current value by the ASCII code you just determined.
Set the current value to itself multiplied by 17.
Set the current value to the remainder of dividing itself by 256.
"""

from globals import PATH_TO_DAY_15, PATH_TO_DAY_15_SAMPLE
import regex as re

def parse_file( line: str ):
  return [ match.group() for match in re.finditer( r"\w+.\d?", line ) ]
  

def hash( strings: list[ list[str] ] ) -> int:
  def perform_hash( string: list[ str ] ) -> int:
    total = 0
    for char in string:
      total = ( ( total + ord( char ) ) * 17 ) % 256
      
    return total
  
  return sum( [ perform_hash( string ) for string in strings ] )

def day_15():
  with open( PATH_TO_DAY_15 ) as file:
    steps = parse_file( [ line.strip() for line in file ][0] )
    print( hash( steps ) )
    
day_15()