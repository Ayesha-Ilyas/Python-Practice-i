import folium
import os
import json
# create map object
m= folium.Map(location=[32.34661206257162,74.36559677124023],zoom_start=12)

#global tooltip
tooltip= 'click for more info'
#create custom marker icon
logoicon=folium.features.CustomIcon('abc.png',icon_size =(50,50))
#vega date
#vis=os.path.join('data', 'vis.json ')
#create markers
folium.Marker([32.346613,74.365598],
              popup='<strong>Location One </strong>',
              tooltip=tooltip).add_to (m),
folium.Marker([32.346614,74.365597],
              popup='<strong>Location two </strong>',
              tooltip=tooltip,
              icon=folium.Icon(icon='cloud')).add_to (m),
folium.Marker([32.346615,74.3655963],
              popup='<strong>Location two </strong>',
              tooltip=tooltip,
              icon=folium.Icon(colour='purpule')).add_to (m),
folium.Marker([32.346616,74.3655965],
              popup='<strong>Location two </strong>',
              tooltip=tooltip,
              icon=folium.Icon(colour='green')).add_to (m),
#folium.Marker([32.34638982,74.365594747],
#              popup=folium.Popup(max_width=450).add_child(folium.Vega(json.load(open(vis)),
 #                                                                     width=450,height=250))).add_to (m),

#circle marker
folium.CircleMarker(
    radius='30',
    location=[32.346618,74.365590],
    popup='myplace',
    color='#536',
    fill=True,
    fill_color='#939'
).add_to(m),
#Generate map
m.save('map.html')