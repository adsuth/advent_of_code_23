from pandas import DataFrame
from globals import PATH_TO_DAY_14, PATH_TO_DAY_14_SAMPLE

GRID = []

class Direction:
  NORTH = 0
  SOUTH = 1
  EAST  = 2
  WEST  = 3

class Vector:
  NORTH = ( -1, 0 )
  SOUTH = ( 1,  0 )
  EAST  = ( 0,  1 )
  WEST  = ( 1, -1 )

class Roller:
  LABEL = "O"
  
  def __init__( self, row, col ):
    self.row = row
    self.col = col
  
  def add_vector( self, vector: Vector ) -> tuple[ int, int ]:
    return ( self.row + vector[0], self.col + vector[1] )
  
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
    
def get_vector( direction: Direction ) -> Vector:
  if direction == Direction.NORTH:
    return Vector.NORTH
  elif direction == Direction.SOUTH:
    return Vector.SOUTH
  elif direction == Direction.EAST:
    return Vector.EAST
  elif direction == Direction.WEST:
    return Vector.WEST  
  
def get_new_coords( to_move: Roller, direction: Direction ) -> tuple[ int, int ]:
  vector   = get_vector( direction )
  row, col = to_move.add_vector( vector ) 
  
  is_oob = (
    row < 0 or 
    col < 0 or
    row > len( GRID ) -1 or
    col > len( GRID[0] ) -1
  )
  
  if is_oob:
    return ( to_move.row, to_move.col )
  
  if GRID[ row ][ col ] == None:
    return ( row, col )
  
  return ( to_move.row, to_move.col )

def move( to_move: Roller, direction: Direction ) -> None:
  row, col = get_new_coords( to_move, direction )
  
  GRID[ to_move.row ][ to_move.col ] = None
  GRID[ row ][ col ]                 = to_move.move_and_get( row, col )
  
  return to_move
  
def parse_file( lines ):
  for i, row in enumerate( lines ):
    cols = [ convert_item( col, i, j ) for j, col in enumerate( row ) ]
    GRID.append( cols )
  
def move_roller( candidate: Roller, current_direction: Direction ):
  if type( candidate ).__name__ != "Roller":
    return candidate

  return move( candidate, current_direction )

def move_rollers():
  number_of_cycles = 1_000_000_000
  printerval       = 1_000
  
  for i in range( number_of_cycles ):
    for current_direction in range( 4 ):
      for row in GRID:
        for item in row:
          move_roller( item, current_direction )
    
    if i % printerval == 0:
      print( f"PROGRESS >> {i}/{number_of_cycles}" )
      
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