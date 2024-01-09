# Author: Minh Nguyen
# Date: 11/15/2023
# Purpose: Vertex class

from cs1lib import *

#constant variables
R = 7
W = 2

class Vertex:
    def __init__(self, name, x, y): # This method will initialize the instance variables name,
        # x- and y-coordinates using the given parameters and set the adjacency list to a empty list.
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.adjacent = []

    def __str__(self): # This method return a string that is created by concatenating all the strings
        str_names = ""
        i = 0
        for adj_vertex in self.adjacent:
            i = i + 1
            vertex_name = adj_vertex.name
            if i == len(self.adjacent):
                str_names = str_names + str(vertex_name)
            else:
                str_names = str_names + str(vertex_name) + ", "

        return str(self.name) + "; " + "Location: " + str(self.x) + ", " + str(self.y) + "; " + "Adjacent vertices: " + str(str_names)

    def draw_vertex(self, r, g, b): # This method takes floating point values r, g and b,
        # defining a color as parameters. It draws a circle of the given color at x and y
        # coordinates saved as instance variables.
        disable_stroke()
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, R)

    def draw_edge(self, vertex, r, g, b): # This method takes a reference to another Vertex object
        # and r, g, b as parameters, and it draws an edge between the Vertex that the method is called on
        # (i.e., self) and the other vertex, in the color given by r, g, b.
        enable_stroke()
        set_stroke_width(W)
        set_stroke_color(r, g, b)
        draw_line(self.x, self.y, vertex.x, vertex.y)

    def draw_all_edges(self, r, g, b): # This method takes floating point values r, g and b,
        # defining a color as parameters, and draws all the edges between the vertex and all the vertices
        # in its adjacency list, in the color given by r, g, b.
        enable_stroke()
        set_stroke_width(W)
        set_stroke_color(r, g, b)
        for other_vertex in self.adjacent:
            draw_line(self.x, self.y, other_vertex.x, other_vertex.y)

    def is_clicked(self, x, y): # This method takes the x and y coordinates of the point where the mouse
        # is clicked as parameters and returns a boolean value.
       return self.x - R <= x <= self.x + R and self.y - R <= y <= self.y + R

    def draw_name(self, r, g, b): # display name of the locations on the path
        enable_stroke()
        set_font_bold()
        set_stroke_color(r, g, b)
        draw_text(self.name, self.x, self.y - R)