import sys
import networkx as nx
import osmnx as ox
from geopy.geocoders import Nominatim
sys.path.insert(0, "osmnx-main")
sys.path.insert(0, "geopandas-main")


ox.config(log_console=True, use_cache=True)
locator = Nominatim(user_agent="myapp")
start_location = "Brandenburger Tor"
end_location = "Pergamonmuseum"

start_latlng = locator.geocode(start_location).point
end_latlng = locator.geocode(end_location).point
place = "Berlin, Germany"

mode = 'drive'  # 'drive', 'bike', 'walk'
optimizer = 'time'  # 'length','time'

graph = ox.graph_from_place(place, network_type=mode)
# orig_node = ox.get_nearest_node(graph, start_latlng)
orig_node = ox.get_nearest_node(graph, start_latlng)
dest_node = ox.get_nearest_node(graph, end_latlng)
# shortest_route = nx.shortest_path(graph, orig_node, dest_node, weight=optimizer)
# shortest_route = nx.astar_path(graph, orig_node, dest_node, weight=optimizer)
# shortest_route = nx.floyd_warshall(graph)
shortest_route = nx.bidirectional_shortest_path(graph, orig_node, dest_node)

shortest_route_map = ox.plot_route_folium(graph, shortest_route, tiles='openstreetmap')
shortest_route_map.save('bidirectional_shortest_path.html')

fig, ax = ox.plot_graph_route(graph, shortest_route, save=True)
