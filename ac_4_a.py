import regex as re
from globals import PATH_TO_DAY_FOUR_A, PATH_TO_DAY_FOUR_A_SAMPLE


class Card:
  def __init__( self, numbers, winners ):
    self.numbers  = numbers
    self.winners  = winners
    self.points   = 0
  
  def calc_points( self ):
    for number in self.numbers:
      if self.did_win( number ):
        self.calc_new_points()
    
    return self
      
    
  def calc_new_points( self ):
    if self.points == 0:
      self.points = 1
    else:
      self.points *= 2

  def did_win( self, number ):
    return number in self.winners
  
  def __repr__( self ):
    return str( self.points )
    


def process_card( line: list[ str ] ):
  line = re.sub( r".*: ", "", line )
  
  number = re.sub( r"\|.*", "", line )
  number = re.sub( r"  ", " ", number )
  numbers = number.strip().split( " " )
  numbers = list( map( lambda x: int(x), numbers ) )
  
  winner = re.sub( r".* \|", "", line )
  winner = re.sub( r"  ", " ", winner )
  winners = winner.strip().split( " " )
  winners = list( map( lambda x: int(x), winners ) )
  
  return Card( numbers, winners ).calc_points()



def day_4_a():
  with open( PATH_TO_DAY_FOUR_A ) as file:
    cards = [ process_card(line) for line in file ]
    total = sum( list( map( lambda card: card.points, cards ) ) )
    print( total )
    
day_4_a()