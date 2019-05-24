import itertools
import copy
import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt

"""
-NODE1 & NODE2: names of the nodes connected.

-TRAIL: edge attribute indicating the abbreviated name of the 
trail for each edge. For example: rs = red square

-DISTANCE: edge attribute indicating trail length in miles.

-COLOR: trail color used for plotting.

-ESTIMATE: edge attribute indicating whether the edge distance is 
estimated from eyeballing the trailmap (1=yes, 0=no) as some 
distances are not provided. This is solely for reference; 
it is not used for analysis.

"""

edgelist = pd.read_csv('https://gist.githubusercontent.com/brooksandrew/e570c38bcc72a8d102422f2af836513b/raw/89c76b2563dbc0e88384719a35cba0dfc04cd522/edgelist_sleeping_giant.csv')
#print(edgelist.head(10))

nodelist = pd.read_csv('https://gist.githubusercontent.com/brooksandrew/f989e10af17fb4c85b11409fea47895b/raw/a3a8da0fa5b094f1ca9d82e1642b384889ae16e8/nodelist_sleeping_giant.csv')
#print(nodelist.head(5))
#CREATE empty graph
g = nx.Graph()

# Add edges and edge attributes
for i, elrow in edgelist.iterrows():
    g.add_edge(elrow[0], elrow[1], attr_dict=elrow[2:].to_dict())


#print(elrow[0])#node 1
#print(elrow[1])#node 2
#print(elrow[2:].to_dict()) #edge attribute dict
#print(elrow)
#print(g.nodes())
for i,nlrow in nodelist.iterrows():
    g.node[nlrow['id']].update(nlrow[1:].to_dict())

#print(nlrow)#prints the node item that is assigned last!
#print(list(g.edges(data=True))[0:5])#previews the first 5 items of edges
#print(list(g.nodes(data=True))[0:10])#previews the first 10 nodes
#print('# of edges: {}'.format(g.number_of_edges()))
#print('# of nodes: {}'.format(g.number_of_nodes()))

################################
######## VISUALIZATION #########
################################

### Define node positions data structure (dict) for plotting
node_positions = {node[0]: (node[1]['X'], -node[1]['Y']) for node in g.nodes(data=True)}

#print(node_positions)#previews the positions
#print(dict(list(node_positions.items())[0:5]))#previews the first 5 items of positions in position list
# Define data structure (list) of edge colors for plotting
#print(list(g.edges(data=True))[2][2])
print(list(g.edges(data=True))[0][2])
print(list(g.edges(data=True))[1][2])
print(list(g.edges(data=True))[2][2])
my_list = list(g.edges(data=True))[0][2]
print(dict(my_list)['attr_dict']['color'])
edge_colors = [dict(attr[2])['attr_dict']['color'] for attr in list(g.edges(data=True))]
#edge_colors = [e[2]['color'] for e in list(g.edges(data=True))]
print(edge_colors[0:10])
plt.figure(figsize=(8, 6))
nx.draw(g, pos=node_positions, edge_color=edge_colors, node_size=10, node_color='black')
plt.title('raph Representation of Sleeping Giant Trail Map', size=15)
plt.show()