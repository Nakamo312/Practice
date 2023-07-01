import osmnx as ox
import networkx as nx
import matplotlib.pyplot as plt

ox.config(log_console=True, use_cache=True)
G = ox.graph_from_place('Samara, Samara, Russia', network_type='drive')
Samara_University =( 53.21208746743906,50.17784794661887)
Kuibyshev_square = (53.19549,50.10217)
fig, ax = ox.plot_graph(G, figsize=(5,5), close=False, show=False)

ax.scatter(Samara_University[1],Samara_University[0], c='red', s=100)
ax.scatter(Kuibyshev_square[1], Kuibyshev_square[0], c='red', s=100)
plt.show()

nearest_edge1 = ox.nearest_nodes(G, Samara_University[1], Samara_University[0] )
nearest_edge2 = ox.nearest_nodes(G, Kuibyshev_square[1], Kuibyshev_square[0] )
route = nx.shortest_path(G, nearest_edge1,nearest_edge2)
fig, ax = ox.plot_graph_route(G, route, figsize=(5,5))
plt.show()

