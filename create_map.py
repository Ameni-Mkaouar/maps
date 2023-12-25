import folium

# Create a map centered on Maryland
maryland_map = folium.Map(location=[39.0458, -76.6413], zoom_start=8)

# Replace the coordinates with SERC site coordinates
serc_site_coordinates = [38.905, -76.56]

# Add a marker for the SERC site
folium.Marker(location=serc_site_coordinates, popup='SERC Site').add_to(maryland_map)

# Save the map to an HTML file
maryland_map.save('maryland_map_with_serc.html')
