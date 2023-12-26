
import sys
import regex as re
from globals import PATH_TO_DAY_8, PATH_TO_DAY_8_SAMPLE

sys.setrecursionlimit( 20_000 )

class Node:
  def __init__( self, position, left, right ):
    self.position = position
    self.left     = left
    self.right    = right

  def __repr__( self ):
    return f"{self.position} = {self.left} | {self.right}"

def parse_file( lines ):
  instructions = ""
  nodes = []
  
  for i, line in enumerate( lines ):
    if i == 0:
      instructions = line
      continue
    
    matches = list( map( lambda x: x.group(), re.finditer( r"\w+", line ) ) )
    if len( matches ) < 3: 
      continue

    pos, left, right = matches
    nodes.append( Node( pos, left, right ) )
    
  # print( f"Instructions: {instructions}" )
  # print( f"Nodes:        {nodes}" )
  
  return list(instructions), nodes
    
def find_node( q, nodes ):
  return [ node for node in nodes if node.position == q ][0]    

def follow_dir( instructions, nodes, current_node, pos = 0, step_count = 0 ):
  if "ZZZ" in current_node.position:
    return step_count
  
  dir = current_node.right if instructions[ pos ] == "R" else current_node.left
  next_pos = (pos + 1) % len( instructions )
  
  return follow_dir( instructions, nodes, find_node( dir, nodes ), next_pos, step_count + 1 )
  

def parse_nodes( instructions, nodes ):
  step_count = follow_dir( instructions, nodes, find_node( "AAA", nodes ) )
  print( step_count )
  

def day_8_a():
  with open( PATH_TO_DAY_8 ) as file:
    instructions, nodes = parse_file( [ line.strip() for line in file ] )
    parse_nodes( instructions, nodes )
    

day_8_a()