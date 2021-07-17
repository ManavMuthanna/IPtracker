import folium
import geocoder

IPaddress=input("Enter IP address")

g = geocoder.ip(IPaddress)

myaddress = g.latlng
print(myaddress)

my_map1 = folium.Map(location=myaddress,
zoom_start=12)


folium.CircleMarker(location=myaddress,
radius=50,popup="Approximate Location").add_to(my_map1)


folium.Marker(myaddress,popup="Approximate Location").add_to(my_map1)


my_map1.save("my_map.html")


