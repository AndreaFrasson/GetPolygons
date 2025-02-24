import os
import leafmap 
from samgeo import SamGeo, tms_to_geotiff, get_basemaps
import fiona
from shapely import Polygon
from shapely import wkb
import matplotlib.pyplot as plt
from shapely.plotting import plot_polygon
import folium
import streamlit as st

st.set_page_config(layout="wide")

markdown = """
A Streamlit map template
<https://github.com/opengeos/streamlit-map-template>
"""

st.sidebar.title("About")
st.sidebar.info(markdown)
logo = "https://i.imgur.com/UbOXYAU.png"
st.sidebar.image(logo)

st.title("Split-panel Map")

with st.expander("See source code"):
    with st.echo():
        m = leafmap.Map(center=[44.53831 , 11.40759], zoom=15)
        m.add_basemap("SATELLITE")

m.to_streamlit(height=700)

