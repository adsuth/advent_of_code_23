import regex as re
from globals import PATH_TO_DAY_THREE_A, PATH_TO_DAY_THREE_A_SAMPLE

GEAR_SYMBOL = "*"

def find_rest_of_num( line: str, i: int ) -> tuple[int, str]:
  number = ""
  
  left  = i
  right = i + 1
  
  # find the center + left side
  while line[ left ].isnumeric():
    number += line[ left ]
    line = line[:left] + "." + line[left+1:]
    left -= 1
  
  # reverse the number 
  number = number[ ::-1 ]
  
  try:
    # find the right side
    while line[ right ].isnumeric():
      number += line[ right ]
      line = line[:right] + "." + line[right+1:]
      right += 1
  except:
    ...
    
  number = int( number ) if number.isnumeric() else 0
  
  return number, line

def try_access_row( grid: list[ str ], i: int ):
  row = None
  try:
    row = grid[ i ]
  except:
    ...
  finally:
    return row

def try_check_for_neighbor( row: str, i: int ):
  has_symbol = False
  try:
    has_symbol = row[ i ].isnumeric()
  except:
    ...
  finally:
    return has_symbol

def try_check_row( row: str, i: int ):
  numbers = []
  
  if row == None:
    return False
  
  if try_check_for_neighbor( row, i -1 ):
    new_nums, row = find_rest_of_num( row, i -1 )
    numbers.append( new_nums )
    
  if try_check_for_neighbor( row, i ):
    new_nums, row = find_rest_of_num( row, i )
    numbers.append( new_nums )
    
  if try_check_for_neighbor( row, i +1 ):
    new_nums, row = find_rest_of_num( row, i +1 )
    numbers.append( new_nums )
  
  return numbers

def find_all_symbols( line: str ) -> list[ re.Match ]:
  return re.finditer( r"[^0-9\.]", line )



def find_neighboring_numbers( row_number: int, grid: list[str], match: re.Match ):
  numbers = []
  
  start         = match.start()
  end           = match.end()
  
  row_upper_number = row_number - 1
  row_lower_number = row_number + 1
  
  row       = try_access_row( grid, row_number )
  
  row_upper = try_access_row( grid, row_upper_number if row_upper_number >= 0          else None )
  row_lower = try_access_row( grid, row_lower_number if row_lower_number < len( grid ) else None )
  
  
  if try_check_for_neighbor( row, start - 1 ):
    new_nums, row = find_rest_of_num( row, start - 1 )
    numbers.append( new_nums )
    
  if try_check_for_neighbor( row, end ):
    new_nums, row = find_rest_of_num( row, end )
    numbers.append( new_nums )
    
  numbers.extend( try_check_row( row_upper, start ))
  numbers.extend( try_check_row( row_lower, start ) )

  return numbers




def process_grid( grid: list[str] ):
  numbers = []
  for row_number, row in enumerate( grid ):
    symbol_matches = find_all_symbols( row )
    
    for match in symbol_matches:
      # if match.group() == GEAR_SYMBOL:
      #   ...
      new_nums = find_neighboring_numbers( row_number, grid, match )
      numbers.extend( new_nums )
  
  return sum( numbers )
      

def day_3_a():
  with open( "Debug.txt", "w" ) as file:
    file.write("")
    
  with open( PATH_TO_DAY_THREE_A ) as file:
    grid = [ line.strip() for line in file ]
    
    print( process_grid( grid ) )