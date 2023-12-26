from io import TextIOWrapper
import regex as re

from globals import PATH_TO_DAY_7, PATH_TO_DAY_7_SAMPLE

from pprint import pprint

CARD_VALUES = {
  "A": 14,
  "K": 13,
  "Q": 12,
  "J": 11,
  "T": 10,
  "9": 9,
  "8": 8,
  "7": 7,
  "6": 6,
  "5": 5,
  "4": 4,
  "3": 3,
  "2": 2,
}

class Hand:
  def __init__( self, hand: str, bet: int ):
    self.hand          = list( hand )
    
    self.best_pair     = -1
    self.value         = -1
    
    self.bet           = bet
    
    self.frequencies   = {}
    self.is_full_house = False
    self.has_two_pairs = False
  
  def count_cards( self ):
    frequencies = {}
    for card in self.hand:
      if frequencies.get( card, False ):
        frequencies[ card ] += 1
        continue
        
      frequencies[ card ] = 1
    
    self.frequencies = frequencies
  
  def determine_best_pair( self ):
    best_card  = None
    best_value = float( "-inf" )
    
    for card, value in self.frequencies.items():
      if best_value == 2 and value == best_value:
        self.has_two_pairs = True
        
      if value > best_value:
        best_card  = card
        best_value = value

    self.value = best_value
    self.card  = best_card
    
    # check for full house
    self.is_full_house = best_value == 3 and len( self.frequencies.values() ) == 2
  
  def add_hand_to_group( self ):
    if   self.value == 5:
      HandGroups.five_of_a_kinds.append( self )
    elif self.is_full_house:
      HandGroups.full_houses.append( self )
    elif self.value == 4:
      HandGroups.four_of_a_kinds.append( self )
    elif self.value == 3:
      HandGroups.three_of_a_kinds.append( self )
    elif self.has_two_pairs:
      HandGroups.two_pair_two_of_a_kinds.append( self )
    elif self.value == 2:
      HandGroups.two_of_a_kinds.append( self )
  
  def __repr__(self) -> str:
    return "".join( self.hand )
    
  
  def parse_hand( self ):
    self.count_cards()
    self.determine_best_pair()
    self.add_hand_to_group()
    # print( f"Hand: {self.hand}" )

class HandGroups:
  five_of_a_kinds:         list[Hand] = []
  full_houses:             list[Hand] = []
  four_of_a_kinds:         list[Hand] = []
  three_of_a_kinds:        list[Hand] = []
  two_pair_two_of_a_kinds: list[Hand] = []
  two_of_a_kinds:          list[Hand] = []
  high_cards:              list[Hand] = []
 
 
def sort_five_of_a_kinds( list: list[str] ):
  return sorted( list, key = lambda h: CARD_VALUES[ h.card ], reverse = True )
 
def sort_four_of_a_kinds( list: list[str] ):
  return sorted( list, key = lambda h: CARD_VALUES[ h.hand[0] ], reverse = True )
 
def sort_full_houses( list: list[str] ):
  return sorted( list, key = lambda h: CARD_VALUES[ h.hand[2] ], reverse = True )
 
def sort_two_pair( list: list[str] ):
  return sorted( list, key = lambda h: CARD_VALUES[ h.hand[1] ], reverse = True )
 
def sort_others( list: list[str] ):
  return sorted( list, key = lambda h: CARD_VALUES[ h.card ], reverse = True )
 
def get_cards_from_worst_to_best( bets: list[int], groups: dict[ str, list[ str ] ] ):
  arr = sort_five_of_a_kinds( groups[ "Five of a Kinds" ] )
  arr.extend( sort_full_houses( groups[ "Full Houses" ] ) )
  arr.extend( sort_four_of_a_kinds( groups[ "Four of a Kinds" ] ) )
  arr.extend( sort_others( groups[ "Three of a Kinds" ] ) )
  arr.extend( sort_two_pair( groups[ "Double Two of a Kinds" ] ) )
  arr.extend( sort_others( groups[ "Two of a Kinds" ] ) )

  return arr[::-1]

def parse_file( file: TextIOWrapper ) -> tuple[ list[str], list[int] ]:
  hands = []
  bets  = []
    
  for line in file:
    hands.append( re.search( r".{5}", line ).group().strip() )
    bets.append(  int( re.search( r" \d+", line ).group().strip() ) )
  
  return hands, bets


def read_hands( hands: list[ str ], bets: list[ int ] ):
  for i, hand_str in enumerate( hands ):
    hand = Hand( hand_str, bets[i] )
    hand.parse_hand()



def day_7_a():
  with open( PATH_TO_DAY_7 ) as file:
    hands, bets = parse_file( file )
    read_hands( hands, bets )
    
    pprint({
      "Five of a Kinds": HandGroups.five_of_a_kinds,
      "Full Houses": HandGroups.full_houses,
      "Four of a Kinds": HandGroups.four_of_a_kinds,
      "Three of a Kinds": HandGroups.three_of_a_kinds,
      "Double Two of a Kinds": HandGroups.two_pair_two_of_a_kinds,
      "Two of a Kinds": HandGroups.two_of_a_kinds,
    })
    
    wtb = get_cards_from_worst_to_best( bets, {
      "Five of a Kinds": HandGroups.five_of_a_kinds,
      "Full Houses": HandGroups.full_houses,
      "Four of a Kinds": HandGroups.four_of_a_kinds,
      "Three of a Kinds": HandGroups.three_of_a_kinds,
      "Double Two of a Kinds": HandGroups.two_pair_two_of_a_kinds,
      "Two of a Kinds": HandGroups.two_of_a_kinds,
      "High Cards": HandGroups.high_cards,
    })
    
    total = sum( [ hand.bet * (i + 1) for i, hand in enumerate( wtb ) ] )
    
    pprint( f"{wtb}" )
    pprint( f"{list( map( lambda x: x.bet , wtb ) )}" )
    print( f"{total}" )
    

day_7_a()