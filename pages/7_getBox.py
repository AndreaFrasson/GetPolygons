import streamlit as st
import leafmap.foliumap as leafmap

st.set_page_config(layout="wide")

if "data" not in st.session_state:
    st.session_state["data"] = {'bbox': None}

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

if not bbox:
    st.text("Draw field")
    tmp_button = st.button("Add value to database", key=f"missing_{st.session_state["data"]['bbox']}")
    if tmp_button:
        st.session_state["data"]['bbox'] = m.user_roi_bounds()
    else:
        st.stop()
    

st.write(bbox)