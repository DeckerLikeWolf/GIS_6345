from arcgis.gis import GIS

import arcpy

import pandas as pd

import matplotlib.pyplot as plt

arcpy.env.workspace = r"C:\GIS\6345\Data"

df = pd.DataFrame.spatial.from_featureclass("oprhp18")

df.head()

df['County'].value_counts().head()

sedf = pd.DataFrame.spatial.from_featureclass("oprhp18")

sedf = pd.DataFrame.spatial.from_featureclass("oprhp18")

plt.bar(sedf.County, sedf.Tot_acre)


plt.xticks(rotation=90)

plt.show()


