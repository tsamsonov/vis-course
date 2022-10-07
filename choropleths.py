QgsProject.instance().removeAllMapLayers()

#uri = "X:/Spatial/Natural Earth/natural_earth_vector.gpkg|layername=ne_10m_admin_0_countries"

uri = "/Volumes/Data/Spatial/Natural Earth/natural_earth_vector.gpkg|layername=ne_10m_admin_0_countries"
countries = iface.addVectorLayer(uri, "countries", "ogr")

# Filtering
countries.setSubsetString("CONTINENT = 'Africa'")

# Classification methods and ramp
classreg = QgsApplication.classificationMethodRegistry()
nms = classreg.methodNames()
method = classreg.method('Pretty')
ramp = QgsStyle().defaultStyle().colorRamp('Reds')

# Renderer
renderer = QgsGraduatedSymbolRenderer()
renderer.setClassAttribute('GDP_MD_EST')
renderer.setClassificationMethod(method)
renderer.updateClasses(countries, 15)
renderer.updateColorRamp(ramp)

#colors = []
#for r in renderer.ranges():
#    colors.append(r.symbol().color().getRgb())
#    
colors = [r.symbol().color().getRgb() for r in renderer.ranges()]

distances = []

i = 0
while i < len(colors)-1:
    c1 = colors[i]
    c2 = colors[i+1]
    d = math.sqrt((c1[0]-c2[0])**2 + 
                  (c1[1]-c2[1])**2 + 
                  (c1[2]-c2[2])**2)
    distances.append(round(d, 1))
    i += 1
    
print(distances)

# Visualize
countries.setRenderer(renderer)
countries.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(countries.id())

