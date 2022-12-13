import networkx as nx
import matplotlib.pyplot as plt

def find_trip(graph,a,b):
	march=nx.shortest_path(g, a, b, weight='weight')
	dist=nx.shortest_path_length(g, a, b, weight='weight')
	return march, dist

city_list=[]
with open("C:\\Users\\Александр\\Desktop\\Academy\\Materials\\cities.csv","r") as file:
	while True:
		ln=file.readline()
		if ln:
			ls=ln.split(';')
			ls[2]=int(ls[2])
			city_list.append(ls)
		else:
			break

	g = nx.Graph()
	for i in city_list:
		g.add_edge(i[0], i[1], weight=i[2])

	m=""
	while True:
		start_city=input("Введіть начальний пункт поїздки (англійською мовою з великої літери) : ")
		if any(x == start_city for x, *_ in city_list):
			break
		else:
			print("Нажаль я не знаю такого міста. Спробуйте ще раз.")
	while True:
		finish_city=input("Введіть пункт призначення (англійською мовою з великої літери) : ")
		if any(x == finish_city for x, *_ in city_list):
			break
		else:
			print("Нажаль я не знаю такого міста. Спробуйте ще раз.")

	y=input("Малювати карту маршруту? (Y/N)")
	march,dist=find_trip(g,start_city,finish_city)

	for i in range(len(march)-1):  #Це просто для краси виводу
		m+=march[i]
		m+='-'
	m+=march[-1]

	print(f'Пропоную маршрут довжиною у {dist} кілометра' )
	print(m)
	if y=='Y':
		pos = nx.spring_layout(g)
		nx.draw_networkx(g, pos)
		plt.title("Cities of Ukraine ")
		plt.show()