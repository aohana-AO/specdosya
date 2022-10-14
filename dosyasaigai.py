import geopandas as gpd
import matplotlib.pyplot as plt
import folium
from IPython.display import display
from bs4 import BeautifulSoup

#geopandasにshp読み込み
path_shp = "市町村等（土砂災害警戒情報）/市町村等（土砂災害警戒情報）.shp"
gdf = gpd.read_file(path_shp, encoding='UTF-8')



import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET


#ききくるxml読み込み
url = 'https://www.data.jma.go.jp/developer/xml/data/20220927015051_0_VPRN50_010000.xml'

req = urllib.request.Request(url)

with urllib.request.urlopen(req) as response:
    XmlData = response.read()

root = ET.fromstring(XmlData)


#留意事項列追加、この列で色分け
gdf['ryuui']='-5'

#一つ目飛ばす用の0
x = 0

for child in root[2][3][1]:
    if x == 0:
        # Itemのとこひとつめ[0]は補足事項的なものだから飛ばす、じゃないと以後indexerro出る
        x += 1
        continue

    for index, row in gdf.iterrows():
        if row['name']==child[1][0].text:


            #土砂災害
            if child[0][0][1][0][0][1].text=='00':
                gdf.at[index,'ryuui'] = '0'
            elif child[0][0][1][0][0][1].text=='12':
                gdf.at[index,'ryuui']= '12'
            elif child[0][0][1][0][0][1].text=='22':
                gdf.at[index,'ryuui']= '22'
            elif child[0][0][1][0][0][1].text=='32':
                gdf.at[index,'ryuui']= '32'
            elif child[0][0][1][0][0][1].text=='42':
                gdf.at[index,'ryuui']= '42'
            elif child[0][0][1][0][0][1].text=='52':
                gdf.at[index,'ryuui']= '52'
            else:
                gdf.at[index,'ryuui'] = ''
            print(gdf.at[index,'ryuui'])

            '''
          #洪水被害

            if child[0][0][1][0][2][1].text == '00':
                gdf.at[index, 'ryuui'] = '00'
            elif child[0][0][1][0][2][1].text == '22':
                gdf.at[index, 'ryuui'] = '22'
            elif child[0][0][1][0][2][1].text == '32':
                gdf.at[index, 'ryuui'] = '32'
            elif child[0][0][1][0][2][1].text == '42':
                gdf.at[index, 'ryuui'] = '42'
            elif child[0][0][1][0][2][1].text == '52':
                gdf.at[index, 'ryuui'] = '52'
            else:
                gdf.at[index, 'ryuui'] = ''
            print(gdf.at[index, 'ryuui'])
            #浸水被害

            try:
                print(child[0][0][1][0][1].tag, child[0][0][1][0][1].attrib)
            except IndexError:
                print('Error')
                continue
            #print(child[0][0][1][0][0].tag, child[0][0][1][0][0].attrib)
            #print(child[0][0][1][0][1].tag, child[0][0][1][0][1].attrib)

            if child[0][0][1][0][1][1].text == '00':
                gdf.at[index, 'ryuui'] = '00'
            elif child[0][0][1][0][1][1].text == '24':
                gdf.at[index, 'ryuui'] = '24'
            elif child[0][0][1][0][1][1].text == '34':
                gdf.at[index, 'ryuui'] = '34'
            elif child[0][0][1][0][1][1].text == '44':
                gdf.at[index, 'ryuui'] = '44'
            elif child[0][0][1][0][1][1].text == '52':
                gdf.at[index, 'ryuui'] = '52'
            else:
                gdf.at[index, 'ryuui'] = ''
            print(gdf.at[index, 'ryuui'])
            '''

print(gdf.loc[18])

gdf.plot(column="ryuui", legend=True, figsize=[30,10], cmap="Oranges")
#gdf.plot("ryuui", legend=True)
plt.show()


