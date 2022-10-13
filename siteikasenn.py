import geopandas as gpd
import matplotlib.pyplot as plt
import folium
from IPython.display import display
from bs4 import BeautifulSoup

# geopandasにshp読み込み
path_shp = "W05-09_27_GML/W05-09_27-g_Stream.shp"

gdf = gpd.read_file(path_shp, encoding='UTF-8')

# 以下、気象庁XML分析

import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

url = 'https://www.gpvweather.com/jmaxml-view.php?k=%E6%8C%87%E5%AE%9A%E6%B2%B3%E5%B7%9D%E6%B4%AA%E6%B0%B4%E4%BA%88%E5%A0%B1&p=%E5%A4%A7%E9%98%AA%E5%BA%9C+%E5%A4%A7%E9%98%AA%E7%AE%A1%E5%8C%BA%E6%B0%97%E8%B1%A1%E5%8F%B0&ym=2021-05&f=2021-05-20T22%3A25%3A40-20210520222541_0_VXKO73_270000.xml'

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    XmlData = response.read()

root = ET.fromstring(XmlData)

# 河川codeと予報河川の照らし合わせ


gdf['kasenn'] = '1'
for child in root[1][8][2][0][1]:
    for index, row in gdf.iterrows():
        if child[1].text == row['W05_002']:
            #予報codeを代入（xmlごとに予報code統一されてるから色分けはしなくてよさそう）
            gdf.at[index, 'kasenn'] = root[1][8][2][0][0][1].text

# geopandasでプロット
# gdf.plot("kasenn", legend=True)
gdf.plot(column="kasenn", legend=True, figsize=[30, 10], cmap="Blues")
plt.show()
