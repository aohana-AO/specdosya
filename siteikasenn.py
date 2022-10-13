import geopandas as gpd
import matplotlib.pyplot as plt
import folium
from IPython.display import display
from bs4 import BeautifulSoup

#geopandasにshp読み込み
#path_shp = "W05-09_27_GML/W05-09_27-g_RiverNode.shp"
path_shp = "W05-09_27_GML/W05-09_27-g_Stream.shp"
# path_shp = "20190125_AreaForecast_GIS/全国・地方予報区等.shp"
gdf = gpd.read_file(path_shp, encoding='UTF-8')
gdf.head()
print(gdf.loc[3])
print(gdf.loc[4])
print(gdf.loc[5])


'''
for index, row in gdf.iterrows():
    print(row)
    print(index)
'''


import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
url = 'https://www.gpvweather.com/jmaxml-view.php?k=%E6%8C%87%E5%AE%9A%E6%B2%B3%E5%B7%9D%E6%B4%AA%E6%B0%B4%E4%BA%88%E5%A0%B1&p=%E5%A4%A7%E9%98%AA%E5%BA%9C+%E5%A4%A7%E9%98%AA%E7%AE%A1%E5%8C%BA%E6%B0%97%E8%B1%A1%E5%8F%B0&ym=2021-05&f=2021-05-20T22%3A25%3A40-20210520222541_0_VXKO73_270000.xml'
#url = 'https://www.data.jma.go.jp/developer/xml/feed/regular.xml'

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    XmlData = response.read()

root = ET.fromstring(XmlData)

print(root[1][8][2][0][1].tag, root[1][8][2][0][1].attrib)
print(root[1][8][2][0][1][1][0].text)


gdf['kasenn']='1'
for child in root[1][8][2][0][1]:
    '''
    print(child[1].tag, child.attrib)
    print(child[1].text)
    '''
    for index, row in gdf.iterrows():
        if child[1].text == row['W05_002']:
            gdf.at[index,'kasenn'] = '10'


#gdf.plot("kasenn", legend=True)
gdf.plot(column="kasenn", legend=True, figsize=[30,10], cmap="Blues")
plt.show()

import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET


#聴き来るxml読み込み
#url = 'https://www.data.jma.go.jp/developer/xml/data/20220920060020_0_VPRN50_010000.xml'
url = 'https://www.data.jma.go.jp/developer/xml/data/20220927015051_0_VPRN50_010000.xml'
#url = 'https://www.data.jma.go.jp/developer/xml/data/20220920070011_0_VPRN50_010000.xml'
# url = 'https://www.data.jma.go.jp/developer/xml/feed/regular.xml'

'''
gdf.plot(legend=True)
plt.show()

'''

'''
shounai = gpd.read_file('市町村等（土砂災害警戒情報）.json')
print(shounai.head())
latlon = [shounai.geometry.centroid.y[0],shounai.geometry.centroid.x[0]]
'''
'''
m = folium.Map(latlon, zoom_start=12, control_scale=True)
folium.GeoJson(shounai).add_to(m)
m
'''

# display(gdf)
# gdf.to_csv("市町村等（土砂災害警戒情報.csv")
'''
f = plt.figure(figsize=(6, 6))
a = f.gca()
a.plot(*gdf.iloc[0].geometry.exterior.xy)
'''
