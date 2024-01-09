# Author: Minh Nguyen
# Date: 11/15/2023
# Purpose: Displaying the map

# extra credit: display names of vertices on the path along with source and destination when picked
# (distinguish the source and destination vs the other location on the path)

from cs1lib import *
from load_graph import create_vertex_dictionary
from bfs import breadth_first

#variables
WINDOW_WIDTH = 1012
WINDOW_HEIGHT = 811

# initial mouse coordinates
mx = 0
my = 0

# initial start and goal vertex
start_vertex = None
goal_vertex = None

mpressed = False

vertex_dict = create_vertex_dictionary("dartmouth_graph.txt")

def draw(): # main graphics function
    global mx, my, mpressed, start_vertex, goal_vertex, vertex_dict
    # Draw the map background
    map = load_image("dartmouth_map.png")
    draw_image(map, 0, 0)

    for vertices in vertex_dict:
        vertex_dict[vertices].draw_vertex(0, 0, 1)
        vertex_dict[vertices].draw_all_edges(0, 0, 1)
        # print(vertex_dict[vertices])

    for vertex in vertex_dict: # To select a vertex as the start vertex, the user should hover the mouse pointer
        # over it and press and release the mouse button. If the user repeats this on a different vertex,
        # then that should become a new start vertex.
        if vertex_dict[vertex].is_clicked(mx, my) and mpressed == True:
            start_vertex = vertex_dict[vertex]

    for other_vertex in vertex_dict: # Once a start vertex is picked, the user should hover the mouse pointer
        # over another vertex (without clicking the mouse) to make that vertex the goal vertex.
        if vertex_dict[other_vertex].is_clicked(mx, my) and mpressed == False:
            goal_vertex = vertex_dict[other_vertex]

    if start_vertex != None: #draw start vertex
        start_vertex.draw_vertex(1, 0, 0)
        start_vertex.draw_name(0, 0, 0) # name of start bold black

    # Once the start and goal vertices are selected, call function implementing the BFS algorithm
    # on these vertices to find the path between them and display it on the Dartmouth map.
    if start_vertex != None and goal_vertex != None:
        path = breadth_first(start_vertex, goal_vertex)
        i = len(path) - 1
        while i > 0: # Once the BFS algorithm returns the path, draw the vertices on the path and the edges
            # between the vertices in a color that is different from the color used to draw the vertices
            # and edges in the rest of the map.
            path[i].draw_vertex(1, 0, 0)
            path[i].draw_edge(path[i - 1], 1, 0, 0)
            i = i - 1

        j = len(path) - 2
        while j > 0: # name of locations on the path bold pink
            path[j].draw_name(1, 0, 1)
            j = j - 1

    if goal_vertex != None: # draw goal vertex
        goal_vertex.draw_vertex(1, 0, 0)
        goal_vertex.draw_name(0, 0, 0) # name of goal bold black


def mpress(x, y):
    global mx, my, mpressed
    mpressed = True
    mx = x
    my = y

def mrelease(x, y):
    global mx, my, mpressed
    mx = x
    my = y
    mpressed = False

def mmove(x, y):
    global mx, my
    mx = x
    my = y

start_graphics(draw, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, mouse_press=mpress, mouse_move=mmove, mouse_release=mrelease)
