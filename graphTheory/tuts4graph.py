import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt
import itertools as it


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
NODE_POSITIONS = {node[0]: (node[1]['X'], -node[1]['Y']) for node in g.nodes(data=True)}

#print(node_positions)#previews the positions
#print(dict(list(node_positions.items())[0:5]))#previews the first 5 items of positions in position list
# Define data structure (list) of edge colors for plotting
#print(list(g.edges(data=True))[2][2])
#print(list(g.edges(data=True))[0][2])
#print(list(g.edges(data=True))[1][2])
#print(list(g.edges(data=True))[2][2])
my_list = list(g.edges(data=True))[0][2]
#print(dict(my_list)['attr_dict']['color'])
EDGE_COLORS = [dict(attr[2])['attr_dict']['color'] for attr in list(g.edges(data=True))]
###PROBLEMATIC###
#edge_colors = [e[2]['color'] for e in list(g.edges(data=True))]
###PROBLEMATIC###
#print(edge_colors[0:10])
plt.figure(figsize=(8, 6))
nx.draw(g, pos=NODE_POSITIONS, edge_color=EDGE_COLORS, node_size=50, node_color='skyblue', widths=40)
plt.title('raph Representation of Sleeping Giant Trail Map', size=15)
#plt.show()

#########################################
#####NOW CHINESE POSTMAN PROBLEM#########
#########################################

################
###odd_nodes####
################
#print(g.degree())
nodes_odd_degree = [v for v, d in list(g.degree()) if d % 2 == 1]
#print(nodes_odd_degree)
#print("Number of odd total nodes :{}".format(len(g.node)))
#print("Number of nodes of odd degree :{}".format(len(nodes_odd_degree)))

odd_node_pairs = list(it.combinations(nodes_odd_degree, 2))
#print(odd_node_pairs)
#print(len(odd_node_pairs))

def get_shortest_path_with_dijkstra(graph, pairs, edge_weight_name):
    """Compute shortest distance between each pair of nodes in a graph. 
    Return a dictionary keyed on node pairs (tuple).
    """
    distances = {}

    for pair in pairs:
        distances[pair] = nx.dijkstra_path(graph, pair[0], pair[1], weight=edge_weight_name)
    
    return distances

odd_node_pairs_shortest_paths = get_shortest_path_with_dijkstra(g, odd_node_pairs, 'distance')
print(dict(list(odd_node_pairs_shortest_paths.items())[0:10]))

def create_complete_Graph(pair_weights, flip_weights=True):
    """
    Create a completely connected graph using a list of vertex pairs and the shortest path distances between them
    Parameters:
        pair_weights: list[tuple] from the output of get_shortest_paths_distances
        flip_weights: Boolean. Should we negate the edge attribute in pair_weights?
    """
    g = nx.Graph()
    for k, v in pair_weights.items():
        wt_i = -v if flip_weights else v
        g.add_edge(k[0], k[1], attr_dict={'distance': v, 'weight': wt_i})
    return g

g_odd_complete = create_complete_Graph(odd_node_pairs_shortest_paths, flip_weights=True)

# Counts
print('Number of nodes: {}'.format(len(g_odd_complete.nodes())))
print('Number of edges: {}'.format(len(g_odd_complete.edges())))