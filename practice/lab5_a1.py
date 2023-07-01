import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

ox.config(log_console=True, use_cache=True)
G = ox.graph_from_place('Samara, Samara, Russia', network_type='walk')
obj1 =( 53.203414,50.110344)
obj2 = (53.185584,50.087626)
fig, ax = ox.plot_graph(G, figsize=(5,5), close=False, show=False)

ax.scatter(obj1[1],obj1[0], c='red', s=100)
ax.scatter(obj2[1], obj2[0], c='red', s=100)
plt.show()

nearest_edge1 = ox.nearest_nodes(G, obj1[1], obj1[0] )
nearest_edge2 = ox.nearest_nodes(G, obj2[1], obj2[0] )
route = nx.shortest_path(G, nearest_edge1,nearest_edge2)
fig, ax = ox.plot_graph_route(G, route, figsize=(5,5))
plt.show()