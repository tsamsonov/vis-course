QgsProject.instance().removeAllMapLayers()
db = '/Volumes/Data/Spatial/Natural Earth/natural_earth_vector.gpkg|layername={layer}'

land = db.format(layer='ne_110m_land')

layer = iface.addVectorLayer(land,'','ogr')

fill = QColor (250,250,250)
stroke = QColor('darkblue')

symbol = layer.renderer().symbol()
symbol.setColor(fill)
pen = Qt.PenStyle(Qt.SolidLine)
symbol.symbolLayer(0).setStrokeStyle(pen)
symbol.symbolLayer(0).setStrokeColor(stroke)

layer.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(layer.id())