import regex as re
from globals import PATH_TO_DAY_FOUR_A, PATH_TO_DAY_FOUR_A_SAMPLE


class Card:
  # static vars
  all_cards = [] # every unique card
  my_cards  = [] # cards we have won
  
  def __init__( self, card_no, numbers, winners ):
    self.card_no  = card_no
    self.numbers  = numbers
    self.winners  = winners
    self.points   = 0
  
  def scratch( self ):
    next_card_no = self.card_no
    for number in self.numbers:
      if self.did_win( number ):
        next_card_no += 1
        Card.my_cards.append( Card.all_cards[ next_card_no ] )
    
    return self
  

  def did_win( self, number ):
    return number in self.winners
  
  def __str__( self ):
    return f"Card No.: {self.card_no}"
    


def process_card( line: list[ str ], i: int ):
  line = re.sub( r".*: ", "", line )
  
  number = re.sub( r"\|.*", "", line )
  number = re.sub( r"  ", " ", number )
  numbers = number.strip().split( " " )
  numbers = list( map( lambda x: int(x), numbers ) )
  
  winner = re.sub( r".* \|", "", line )
  winner = re.sub( r"  ", " ", winner )
  winners = winner.strip().split( " " )
  winners = list( map( lambda x: int(x), winners ) )
  
  return Card( i + 1, numbers, winners )


def scratch_cards():
  current_card = 1
  with open( "DAY_4_DEBUG.txt", "w" ) as file:
    while current_card < len( Card.my_cards ):
      card: Card = Card.my_cards[ current_card ]
      card.scratch()
      current_card += 1
    
    file.writelines( list( map( lambda c: str( c ) + "\n", Card.my_cards[ 1: ] ) ) )
    
  print( f"Total Cards: {len( Card.my_cards[1:] )}" )



def day_4_b():
  
  with open( PATH_TO_DAY_FOUR_A ) as file:
    Card.all_cards = [ None ] + [ process_card(line, i) for i, line in enumerate( file ) ]
    Card.my_cards = Card.all_cards[::]
    scratch_cards()
    
    
day_4_b()