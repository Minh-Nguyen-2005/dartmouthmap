# Author: Minh Nguyen
# Date: 11/15/2023
# Purpose: Creating the vertex dictionary

from vertex import Vertex

def create_vertex_dictionary(filename):
    input_file = open(filename, "r")
    name_dict = {}

    for line in input_file:
        # Split up the line into three pieces: the vertex name, the list of names of adjacent vertices,
        # and the x- and y-coordinates.
        section_split = line.split(";")
        vertex_name = section_split[0].strip()
        coordinates = section_split[2].strip()
        coord_list = coordinates.split(",")
        coord_x = coord_list[0].strip()
        coord_y = coord_list[1].strip()
        # Create a new Vertex object with the name and coordinate data stored as instance variables.
        # (The name is a string, and the coordinates are integers.) The adjacency list, for now, is an empty list.
        vertex = Vertex(vertex_name, coord_x, coord_y)
        # Put the new Vertex object into a dictionary with the string "Green Southwest" as the key.
        name_dict[vertex_name] = vertex

    input_file.close()

    input_file = open(filename, "r")

    for line in input_file:
        # Get its name and the names of its adjacent vertices.
        section_split = line.split(";")
        vertex_name = section_split[0].strip()
        adjacency = section_split[1].strip()
        adjacent_list = adjacency.split(",")
        # Look up the current vertex in the dictionary.
        # For each vertex that is adjacent to the current vertex, look it up in the dictionary using its name.
        for ele in adjacent_list:
            adj = ele.strip()
            # For each adjacent vertex, append a reference to its Vertex object to the adjacency list in the Vertex
            # object of the current vertex.
            name_dict[vertex_name].adjacent.append(name_dict[adj])

    input_file.close()

    return name_dict