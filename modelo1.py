##modelo1=name
##mdp=raster
##delimitado=output raster
##poligonizado=output vector
##filtrado=output raster
##relleno=output raster
##seleccionados=output vector
##reclas=output raster
##finala=output vector
outputs_SAGAFILLSINKSXXLWANGLIU_1=processing.runalg('saga:fillsinksxxlwangliu', mdp,0.01,relleno)
outputs_GDALOGRRASTERCALCULATOR_1=processing.runalg('gdalogr:rastercalculator', mdp,'1',outputs_SAGAFILLSINKSXXLWANGLIU_1['FILLED'],'1',None,'1',None,'1',None,'1',None,'1','A-B',None,5,None,delimitado)
outputs_SAGARECLASSIFYGRIDVALUES_1=processing.runalg('saga:reclassifygridvalues', outputs_GDALOGRRASTERCALCULATOR_1['OUTPUT'],2,0.0,1.0,0,0.0,1.0,2.0,0,'-1.5,0,0,-50,-1.5,1',0,True,0.0,True,0.0,reclas)
outputs_GDALOGRSIEVE_1=processing.runalg('gdalogr:sieve', outputs_SAGARECLASSIFYGRIDVALUES_1['RESULT'],100.0,0,filtrado)
outputs_GDALOGRPOLYGONIZE_1=processing.runalg('gdalogr:polygonize', outputs_GDALOGRSIEVE_1['OUTPUT'],'DN',poligonizado)
outputs_QGISSELECTBYEXPRESSION_1=processing.runalg('qgis:selectbyexpression', outputs_GDALOGRPOLYGONIZE_1['OUTPUT'],'$area/$perimeter >= 4.5 AND  "DN" = 1',0)
outputs_QGISSAVESELECTEDFEATURES_1=processing.runalg('qgis:saveselectedfeatures', outputs_QGISSELECTBYEXPRESSION_1['RESULT'],seleccionados)
outputs_GDALOGRBUFFERVECTORS_1=processing.runalg('gdalogr:buffervectors', outputs_QGISSAVESELECTEDFEATURES_1['OUTPUT_LAYER'],'geometry',8.0,True,'DN',True,None,finala)