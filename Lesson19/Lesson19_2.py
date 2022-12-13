import networkx as nx
import matplotlib.pyplot as plt


edgelist = [['Mannheim', 'Frankfurt', 85], ['Mannheim', 'Karlsruhe', 80], ['Erfurt', 'Wurzburg', 186],
            ['Munchen', 'Numberg', 167], ['Munchen', 'Augsburg', 84], ['Munchen', 'Kassel', 502],
            ['Numberg', 'Stuttgart', 183], ['Numberg', 'Wurzburg', 103], ['Numberg', 'Munchen', 167],
            ['Stuttgart', 'Numberg', 183], ['Augsburg', 'Munchen', 84], ['Augsburg', 'Karlsruhe', 250],
            ['Kassel', 'Munchen', 502], ['Kassel', 'Frankfurt', 173], ['Frankfurt', 'Mannheim', 85],
            ['Frankfurt', 'Wurzburg', 217], ['Frankfurt', 'Kassel', 173], ['Wurzburg', 'Numberg', 103],
            ['Wurzburg', 'Erfurt', 186], ['Wurzburg', 'Frankfurt', 217], ['Karlsruhe', 'Mannheim', 80],
            ['Karlsruhe', 'Augsburg', 250]]


g = nx.Graph()
for i in edgelist:
    g.add_edge(i[0], i[1], weight = i[2])


print(nx.shortest_path(g, 'Mannheim', 'Kassel', weight='weight'))
print(nx.shortest_path_length(g,  'Mannheim', 'Kassel', weight='weight'))

print(nx.shortest_path(g, 'Munchen', 'Erfurt', weight='weight'))
print(nx.shortest_path_length(g, 'Munchen', 'Erfurt', weight='weight'))

print(nx.shortest_path(g, 'Stuttgart','Karlsruhe', weight='weight'))
print(nx.shortest_path_length(g, 'Stuttgart','Karlsruhe', weight='weight'))

pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.title("Cities of Germany Graph Generation ")
plt.show()



