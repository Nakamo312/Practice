import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph ()
vert = ['Театральная',
        'Самарская',
        'Алабинская',
        'Российская',
        'Московская',
        'Гагаринская' ,
        'Спортивная',
        'Советская',
        'Победа',
        'Безымянка',
        'Кировская',
        'Юнгородок',
        'Хлебная площадь',
        'Вокзальная',
        'Клиническая',
        'Карла-Маркса',
        'Революционная',
        'Орловская']
graph.add_nodes_from(vert)
nx.draw(graph)
plt.show()

edges = [('Театральная','Самарская', 15),
         ('Самарская','Алабинская', 20),
         ('Алабинская','Российская', 10),
         ('Российская', 'Московская', 8),
         ('Московская', 'Гагаринская', 6),
         ('Гагаринская', 'Спортивная', 30),
         ('Спортивная', 'Советская', 6),
         ('Советская', 'Победа', 5),
         ('Победа', 'Безымянка', 4),
         ('Безымянка', 'Кировская', 3),
         ('Кировская', 'Юнгородок', 4),
         ('Хлебная площадь', 'Вокзальная', 4),
         ('Вокзальная','Клиническая', 12),
         ('Клиническая', 'Карла-Маркса', 8),
         ('Карла-Маркса', 'Революционная', 9),
         ('Революционная', 'Орловская', 9),
         ('Московская', 'Карла-Маркса', 1),]
graph.add_weighted_edges_from(edges)
nx.draw_circular(graph, with_labels=True)
plt.show()

graph.add_weighted_edges_from(edges)
pos = nx.spring_layout(graph)
weights = nx.get_edge_attributes(graph,'weight')
nx.draw(graph,pos = pos,with_labels=True, node_size = 300)

plt.show()


graph.add_node('Ленина')
graph.add_node('Комсомольская')
graph.add_weighted_edges_from([('Юнгородок','Комсомольская', 13),
                               ('Комсомольская','Ленина',23)])
weights = nx.get_edge_attributes(graph,'weight')
pos = nx.spring_layout(graph)

nx.draw_networkx(graph,pos = pos)
nx.draw_networkx_edge_labels(graph, pos, edge_labels=weights)
plt.show()


subList = ['Победа','Кировская', 'Юнгородок']
subgraph = graph.subgraph(subList)
nx.draw(subgraph, with_labels=True)
plt.show()