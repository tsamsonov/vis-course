# Hello world

print("Hello world!")
uri = "E:/Geodata/NaturalEarth/vector_v4/natural_earth_vector.gpkg_v4.1.0/packages/natural_earth_vector.gpkg|layername=ne_10m_admin_0_countries"
vlayer = iface.addVectorLayer(uri, "countries", "ogr")

# Viewing vector layer attributes

iface.showAttributeTable(vlayer)

for field in vlayer.fields():
    print(field.name())

for feature in vlayer.getFeatures():
    print(feature["ADMIN"])

# Filtering

vlayer.setSubsetString("ADMIN LIKE 'A%'")
for feature in vlayer.getFeatures():
    print(feature["ADMIN"])

vlayer.setSubsetString("")
for feature in vlayer.getFeatures():
    print(feature["ADMIN"])

my_char = "C"
vlayer.setSubsetString("ADMIN LIKE '"+my_char+"%'")
print("The following country names start with {}:".format(my_char))
for feature in vlayer.getFeatures():
    print(feature['ADMIN'])

for feature in vlayer.getFeatures():
    print("{pop:.2f} mio people live in {name}".format(name=feature['ADMIN'],pop=feature['POP_EST']/1000000))

# Styling

uri = "E:/Geodata/NaturalEarth/vector_v4/natural_earth_vector.gpkg_v4.1.0/packages/natural_earth_vector.gpkg|layername=ne_110m_populated_places_simple"
vlayer = iface.addVectorLayer(uri, "places", "ogr")

vlayer.renderer().symbol().setSize(6)
vlayer.triggerRepaint()

vlayer.renderer().symbol().setColor(QColor("blue"))
vlayer.triggerRepaint()

iface.layerTreeView().refreshLayerSymbology(vlayer.id())

# Styling Heatmap

uri = "E:/Geodata/NaturalEarth/vector_v4/natural_earth_vector.gpkg_v4.1.0/packages/natural_earth_vector.gpkg|layername=ne_110m_populated_places_simple"
vlayer = iface.addVectorLayer(uri, "places", "ogr")

heatmap = QgsHeatmapRenderer()
vlayer.setRenderer(heatmap)
vlayer.triggerRepaint()

heatmap.setRadius(20)
vlayer.setRenderer(heatmap)
vlayer.triggerRepaint()

QgsStyle().defaultStyle().colorRampNames()

ramp = QgsStyle().defaultStyle().colorRamp('Blues')
heatmap.setColorRamp(ramp)
vlayer.setRenderer(heatmap)
vlayer.triggerRepaint()