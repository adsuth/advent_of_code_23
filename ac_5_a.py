import regex as re

from io import TextIOWrapper
from globals import PATH_TO_DAY_5, PATH_TO_DAY_5_SAMPLE

class Map:
  class Entry:
    def __init__( self, destination, source, range ):
      self.min_dest = destination
      self.max_dest = destination + range - 1
      
      self.min_source = source
      self.max_source = source + range - 1
      
      self.range = range
      
      self.items = [] # for example, the seeds
    
      
    """Is the item (eg: seed) a part of this entry?"""
    def item_in_range( self, item: int ) -> bool:
      return (
        item <= self.max_source and
        item >= self.min_source
      )
  
    def calculate_destination( self, item: int ) -> int:
      return item - self.min_source + self.min_dest
    
    
  def __init__( self, name: str, id: int ):
    self.id = id
    self.name = name
    self.entries: list[ Map.Entry ] = []
  
  
  def feed_entry( self, values: list[int] ):
    dest, src, range = values
    self.entries.append( Map.Entry( dest, src, range ) )
  
  
  def get_entries( self ):
    return list( map( lambda e: (e.min_dest, e.min_source, e.range), self.entries ) )
    
    
  def fetch_destination_candidates( self, seed: int ):
    candidates = []
    for entry in self.entries:
      if entry.item_in_range( seed ):
        candidates.append( entry.calculate_destination( seed ) )
    
    if len( candidates ) == 0:
      candidates = [ seed ]
    return candidates
    

###


""" Fetches the seeds from the first line """
def read_seeds( line: str ):
  seeds_part = re.sub( r".*: " , "", line )
  seeds      = seeds_part.split( " " )
  return list( map( int, seeds ) )

def read_map_title( line: str ):
  map_title = re.search( r"(.+)(?=[ ])", line )
  return map_title.group()

def read_values( line: str ) -> list[ int ]:
  value_matches = re.finditer( r"\d+", line )
  return list( map( lambda match: int( match.group() ), value_matches ) )


def parse_file( file: TextIOWrapper ) -> tuple[ list[int], list[Map] ]:
  map_no                   = 0
  maps:  list[Map]         = []
  
  # parse the seeds:
  for i, line in enumerate( file ):
    line = line.strip()
    
    # seeds are at start
    if i == 0:
      seeds = read_seeds( line )
      continue
    
    # map header found
    if ":" in line:
      maps.append( Map( read_map_title( line ), map_no ) )
      map_no += 1
    else:
      vals = read_values( line )
      if len( vals ) == 0:
        continue
      maps[-1].feed_entry( vals )
  
  return seeds, maps
      
def day_5_a():
  with open( PATH_TO_DAY_5 ) as file:
    seeds, maps = parse_file( file )
    last_map    = max( maps, key=lambda map: map.id )
    map = maps[0]
    
    closest = float( "inf" )
    
    
    with open( "DAY_5_DEBUG.txt", "w" ) as d_file:
      d_file.write("")
    
    with open( "DAY_5_DEBUG.txt", "a" ) as d_file:
      for seed in seeds:
        d_file.write( f"\nSEED >> {seed}\n" )
        d_file.write( f"------------\n" )
        
        best_of_last = seed
        
        for map in maps:
          map_candidates = map.fetch_destination_candidates( best_of_last )
          best = min( map_candidates )
          best_of_last = best
        
          d_file.write( f"  MAP >> name: '{map.name}' | id: '{map.id}'\n" )
          d_file.write( f"    ENTRIES >> Entries (D, S, R): {map.get_entries()}\n" )
          d_file.write( f"    BEST >> in: {best_of_last} | out: {best}\n" )
          d_file.write( f"\n" )

          # update the lowest location
          if map == last_map:
            closest = best_of_last if best_of_last < closest else closest

      d_file.write( f"\n" )
      d_file.write( f"CLOSEST >> {closest}\n" )
        
    # print()
    # print( f"Entries (D, S, R): {map.get_entries()}" )
    # print( f"Seed: {seed} | Best: {best} | Candidates: {candidates}" )
      
    print( closest )
  print()

day_5_a() 