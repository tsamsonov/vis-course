QgsProject.instance().removeAllMapLayers()
db = '/Volumes/Data/Spatial/Natural Earth/natural_earth_vector.gpkg|layername={layer}'

land = db.format(layer='ne_110m_land')

lyr_lnd = iface.addVectorLayer(land,'','ogr')

lnd_color = QColor (250,250,250)
cst_color = QColor ('darkblue')

symb_lnd = lyr_lnd.renderer().symbol()
symb_lnd.setColor(lnd_color)
cont_lnd = Qt.PenStyle(Qt.SolidLine)
symb_lnd.symbolLayer(0).setStrokeStyle(cont_lnd)
symb_lnd.symbolLayer(0).setStrokeColor(cst_color)

lyr_lnd.triggerRepaint()
iface.layerTreeView().refreshLayerSymbology(lyr_lnd.id())