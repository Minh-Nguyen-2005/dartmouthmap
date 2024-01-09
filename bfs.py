# Author: Minh Nguyen
# Date: 11/15/2023
# Purpose: Breadth-first search (BFS)

from collections import deque

def breadth_first(src, dest): # Input: source (Src) and destination (Dest)
    frontier = deque() # frontier (queue, implemented using deque in Python)
    backpointer = {} # backpointer dictionary

    frontier.append(src) # Add source to frontier
    backpointer[src] = None # Add source as key and None as asssociated value to backpointer dictionary

    while dest not in backpointer and len(frontier) != 0:
        # Get a vertex V from the front of the frontier (removes the vertex V from frontier)
        V = frontier.popleft()

        for U in V.adjacent:
            # determine whether a vertex has already been visited because if it has,
            # then it should not be inserted again into the queue for the frontier.
            if U not in backpointer:
                frontier.append(U)
                backpointer[U] = V
 # Getting path from backpointer dictionary
    path = []
    V = dest
    while V != None:
        path.append(V)
        V = backpointer[V]

    return path # Output: references to vertices that make the path from source to destination