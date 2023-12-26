
from functools import reduce
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
  time = -1
  distance = -1
  
  for line in lines:
    value = int( "".join( [ match.group() for match in re.finditer( r"\d+", line ) ] ) )
    
    if "Time" in line:
      time = value
    elif "Distance" in line:
      distance = value
  
  race = Race( time, distance )
  
  # print( f"Time:     {time}" )
  # print( f"Ditance: {ditance}" )
  # print( f"Race: {race}" )
  
  return race
 
def calc_distance( time, velocity ):
  return velocity * time
    
def parse_race( race: Race ):
  number_of_winnables_per_race = []
  
  time, dist = race.time, race.best_distance
  winnables = 0
  
  for milli in range( 1, time - 1 ):
    if calc_distance( time - milli, milli ) > dist:
      winnables += 1
      
  number_of_winnables_per_race.append( winnables )
    
    
  print( f"Product of All: {prod( number_of_winnables_per_race )}" )
  

def day_6_a():
  with open( PATH_TO_DAY_6 ) as file:
    race = parse_file( [ line.strip() for line in file ] )  
    parse_race( race )

day_6_a()