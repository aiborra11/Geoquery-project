# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4, letter
# import os
# import webbrowser
# import seaborn as sns
# from folium.plugins import FastMarkerCluster
# import folium
#
#
#
# def mapa(df):
#     latlong = df[['lat', 'lng']]
#     mi = folium.Map(location=latlong, zoom_start=16, control_scale=True)
#     folium.Marker(location=latlong,
#                   popup='This seems to be a good area to place your bar',
#                   icon=folium.Icon(color='blue', icon='glyphicon glyphicon-star-empty'), ).add_to(mi)
#     folium.Circle(location=latlong, radius=500, color='blue', fill=True, fill_color='blue').add_to(mi)
#     minimap = FastMarkerCluster(latlong).add_to(mi)
#     mi.add_child(minimap)
#     mi.save('../pdf/my_bar.html')
#     return webbrowser.open('file://' + os.path.realpath('my_bar.html'))
#
#
# mapa(top500)
















#PDF creator

# def shortpdf (name):
#     ancho, alto=A4        # ancho y alto de la pagina, en dinA4, es una tupla en puntos (un punto=1/72 pulgadas)
#     archivo ='../presentacion/Pipeline Project {}-2014.pdf'.format(yea)
#     # c=canvas.Canvas('../presentacion/Pipeline Project {}-2014.pdf'.format(yea), pagesize=A4)  # genera el archivo pdf vacio, con tamaño dinA4
#     # c.setStrokeColorRGB(0.7, 0.7, 0.7)
#     # c.setStrokeColorRGB(0.7, 0.7, 0.7)
#     # c.setFont("{}-Bold".format(font), 24)
#     # c.drawString(150, alto-50, "Pipelines Project Ironhack")    # escribe con margen de 50 puntos
#     # c.setFont('{}-BoldOblique'.format(font), 10)
#     # c.drawString(20, 20, "Data Bootcamp 06/19")
#     # c.drawRightString(ancho-30, 20, name)
#     # c.setFont("{}-Bold".format(font), 20)
#     # c.drawCentredString(round(ancho/2), alto-80, "Suicides between {}-2014".format(yea))
#     # c.drawImage("../presentacion/logo-ironhack-madrid.jpg", 0, alto-100, width=100, height=100)
#     asd = c.drawImage("../pdf/bar.png", ancho-100, alto-100, width=75, height=75)
#     x=0
#     y=alto-100
#     c.setLineWidth(3)
#     c.setStrokeGray(0)
#     # c.line(x, y, ancho, y)
#     # c.setFont('Times-Roman', 12)
#     # c.drawString(100, alto-155, " In the following graph you can observe the evolution of suicides versus the ")
#     # c.drawString(100, alto-168, " evolution of the GDP per capita:")
#     # c.drawImage(path3, 70, alto - 440, width=450, height=250)
#     # c.drawString(100, alto-480, " In the following graph you can observe the top 10 countries by suicide rate:")
#     # c.drawImage(path4, 70, alto - 750, width=450, height=250)
#     # c.setLineWidth(1)
#     #c.line(0, 50, ancho, 50)
#     # c.setFont('{}-Bold'.format(font), 10)
#     # c.drawCentredString(round(ancho/2), 20, "1/1")
#     c.showPage()
#     c.save()
#     return asd
#
# a = shortpdf ('alejandro')