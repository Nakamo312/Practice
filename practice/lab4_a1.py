import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph ()
vert1 = ['Хлебная площадь',
        'Музей истории города',
        'Музей истории милиции',
        'Площадь революции',
        'Областной художественный музей',
        'Музей-усадьба А.Толстого' ,
        'Областной театр',
        'Театр "СМАРТ"',
        'Струковский парк',
        'Жигулевский пивовареный завод',
        'Монумент славы',
        'Набережная',
        'Цирк им. О.Попова',
        'Ботанический сад',
        'Парк Дружбы',
        'Парк Победы',
        'Парк им. Гагарина',
        '"Загородный парк"',
        'Вокзал']
graph.add_nodes_from(vert1)
nx.draw(graph)
plt.show()

edges1 = [('Хлебная площадь','Музей истории милиции', 15),
          ('Вокзал', "Ботанический сад", 32),
          ('Театр "СМАРТ"', 'Вокзал', 12),
         ('Музей истории города','Площадь революции', 20),
         ('Областной художественный музей','Площадь революции', 10),
         ('Областной художественный музей','Музей истории милиции', 8),
         ( 'Музей истории города', 'Областной театр', 6),
         ( 'Музей-усадьба А.Толстого', 'Областной театр', 6),
         ('Областной театр', 'Театр "СМАРТ"', 30),
         ('Театр "СМАРТ"', 'Парк Победы', 6),
         ('Музей-усадьба А.Толстого', 'Струковский парк', 11),
         ('Струковский парк', 'Жигулевский пивовареный завод', 11),
         ('Жигулевский пивовареный завод', 'Набережная', 22),
         ('Набережная', 'Цирк им. О.Попова', 17),
         ('Цирк им. О.Попова', 'Монумент славы', 13),
         ('Парк Победы', 'Парк Дружбы', 21),
         ('Монумент славы', 'Ботанический сад', 22),
         ('Ботанический сад', 'Парк им. Гагарина', 12),
         ('Парк им. Гагарина', '"Загородный парк"', 34)]


graph.add_weighted_edges_from(edges1)
pos = nx.spring_layout(graph)
weights = nx.get_edge_attributes(graph,'weight')
nx.draw(graph,pos = pos,with_labels=True, node_size = 300)

plt.show()


graph.add_nodes_from(['Театр Оперы и Балета',"Цирк"])
graph.add_weighted_edges_from([('Музей истории города',"Цирк",12),("Цирк",'Театр Оперы и Балета',16)])
graph.edges["Цирк",'Театр Оперы и Балета']['weight'] = 20
weights = nx.get_edge_attributes(graph,'weight')
pos = nx.spring_layout(graph)

nx.draw_networkx(graph,pos = pos)
nx.draw_networkx_edge_labels(graph, pos, edge_labels=weights)
plt.show()


subList = ['Вокзал','Цирк', 'Театр Оперы и Балета']
subgraph = graph.subgraph(subList)
nx.draw(subgraph, with_labels=True)
plt.show()