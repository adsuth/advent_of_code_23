from pandas import DataFrame
from globals import PATH_TO_DAY_14, PATH_TO_DAY_14_SAMPLE
from pprint import pprint 

GRID = []

class Roller:
  LABEL = "O"
  
  def __init__( self, row, col ):
    self.row = row
    self.col = col
  
  def move_and_get( self, row, col ):
    self.row = row
    self.col = col
    
    return self
  
  def __repr__(self):
    return Roller.LABEL

class Static:
  LABEL = "#"
  
  def __init__( self, row, col ):
    self.row = row
    self.col = col

  def __repr__(self):
    return Static.LABEL


def convert_item( item, row, col ):
  new_item = None
  
  if item == Roller.LABEL:
    new_item = Roller( row, col )
    
  elif item == Static.LABEL:
    new_item = Static( row, col )
    
  return new_item
    
    
def get_new_coords( to_move: Roller ) -> tuple[ int, int ]:
  row = to_move.row
  new_row = row - 1
  col = to_move.col
  
  if new_row < 0:
    return ( row, to_move.col )
  
  if GRID[ new_row ][ col ] == None:
    return ( new_row, col )
  
  return ( row, col )


def move_north( to_move: Roller ) -> None:
  row, col = get_new_coords( to_move )
  
  GRID[ to_move.row ][ to_move.col ] = None
  GRID[ row ][ col ]                 = to_move.move_and_get( row, col )
  
  return to_move
  
  
def parse_file( lines ):
  for i, row in enumerate( lines ):
    cols = [ convert_item( col, i, j ) for j, col in enumerate( row ) ]
    GRID.append( cols )
  
def move_roller( candidate: Roller ):
  if type( candidate ).__name__ != "Roller":
    return candidate

  return move_north( candidate )

def move_rollers():
  for _ in range( len( GRID ) ):
    for row in GRID:
      for item in row:
        move_roller( item )

def calc_load():
  total_len  = len( GRID )
  total_load = 0
  
  for i, row in enumerate( GRID ):
    roller_count = len( [ item for item in row if type( item ).__name__ == "Roller" ] )
    magnitude = total_len - i
    total_load += magnitude * roller_count
  
  return total_load

def day_14():
  global GRID
  
  with open( PATH_TO_DAY_14 ) as file:
    parse_file( [ list( line.strip() ) for line in file ] )
    
    print( "BEFORE\n", DataFrame( GRID ), end="\n\n" )

    move_rollers()
    print( "AFTER\n", DataFrame( GRID ), end="\n\n" )
    
    print( f"Total >> {calc_load()}" )

  # with open( "Debug_14.txt", "w" ) as dfile:
  #   dfile.writelines( GRID )
    
day_14()