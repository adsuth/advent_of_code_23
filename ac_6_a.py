
from math import prod
import regex as re
from globals import PATH_TO_DAY_6, PATH_TO_DAY_6_SAMPLE


class Race:
  def __init__( self, t, d ):
    self.time     = t
    self.best_distance = d
  
  def __repr__( self ):
    return f"Time: {self.time} | Best Distance: {self.best_distance}"

def parse_file( lines ):
  times = []
  distances = []
  
  for line in lines:
    values = list( map( lambda m: int( m.group() ), re.finditer( r"\d+", line ) ) )
    
    if "Time" in line:
      times.extend( values )
    elif "Distance" in line:
      distances.extend( values )
  
  races = []
  
  for t, d in zip( times, distances ):
    races.append( Race( t, d ) )
  
  # print( f"Times:     {times}" )
  # print( f"Distances: {distances}" )
  # print( f"Races: {races}" )
  
  return races
 
def calc_distance( time, velocity ):
  return velocity * time
    
def parse_races( races: list[Race] ):
  number_of_winnables_per_race = []
  
  for race in races:
    time, dist = race.time, race.best_distance
    winnables = 0
    
    for milli in range( 1, time - 1 ):
      if calc_distance( time - milli, milli ) > dist:
        winnables += 1
        
    number_of_winnables_per_race.append( winnables )
    
    
  print( f"Product of All: {prod( number_of_winnables_per_race )}" )
  

def day_6_a():
  with open( PATH_TO_DAY_6 ) as file:
    races = parse_file( [ line.strip() for line in file ] )  
    parse_races( races )

day_6_a()