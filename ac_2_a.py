import regex as re
from globals import PATH_TO_DAY_TWO_A

from utils import head

"""only 12 red cubes, 13 green cubes, and 14 blue cubes"""

MAX_REDS   = 12
MAX_GREENS = 13
MAX_BLUES  = 14

class CubeGame:
  class Round:
    def __init__( self ):
      self.reds   = 0
      self.greens = 0
      self.blues  = 0
      
      self.is_legal = True
      
  def __init__( self, game ):
    self.game     = game
    self.rounds   = []
    self.is_legal = True
    
  def feed_counts( self, counts: list[int, int, int] ):
    round = CubeGame.Round()
    round.reds, round.greens, round.blues = counts
    self.rounds.append( round )
    
    self.check_legality()
    return self
  
  def check_legality( self ):
    for round in self.rounds:
      self.is_legal = (
        round.reds   <= MAX_REDS   and
        round.greens <= MAX_GREENS and
        round.blues  <= MAX_BLUES 
      ) and self.is_legal
    
  def read_game( self ):
    return self.game if self.is_legal else 0
  
  def to_string( self ):
    return f"Game {self.game} >> {'LEGAL' if self.is_legal else 'ILLEGAL'}"
  

def count_color( counts ) -> list[int, int, int]:
  color_counts = {
    "red":   0,
    "green": 0,
    "blue":  0
  }
  
  for count in counts:
    color  = re.search( r"[a-z]+", count )[0]
    amount = re.search( r"\d+", count )[0]
    
    color_counts[ color ] += int( amount )
    
  return color_counts.values()

def parse_rounds( i: int, rounds: list[ list[ str ] ] ) -> list[int]:
  new_game = CubeGame( i + 1 )
  for round in rounds:
    new_game.feed_counts( count_color( round ) )
    
  return new_game
    
def process_line( i: int, line: str ):
  """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"""
  raw           = re.search( r"(?<=:\ ).*", line )[0]
  rounds  = re.split( r"; ", raw )
  rounds        = [ re.split( r", ", round ) for round in rounds ]
  
  return parse_rounds( i, rounds )
  

def day_2_a():
  with open( PATH_TO_DAY_TWO_A ) as file:
    games = [ process_line(i, line) for i, line in enumerate( file ) ]
    
    with open( "./debug_text.txt", "w" ) as debug:
      debug.writelines( [ game.to_string() + "\n" for game in games ] )
      
    print( sum( [ game.read_game() for game in games ] ) )