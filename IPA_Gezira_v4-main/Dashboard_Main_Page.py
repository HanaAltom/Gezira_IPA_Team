import streamlit as st
import matplotlib.cm as cm
from streamlit_folium import st_folium
from shapely.geometry import Point
from arabic_support import support_arabic_text
from util.gezira_info_txt import arabic_txt, english_txt

from util import common2 as cm


cm.set_page_container_style(
        max_width = 1100, max_width_100_percent = True,
        padding_top = 0, padding_right = 0, padding_left = 0, padding_bottom = 0
)

col1, col2 = st.columns((5, 3), gap='medium')

dfm, geo = cm.read_df_and_geo('wheats')
logo_small, logo_wide = cm.logos()
gdf = cm.get_gdf_from_json(geo)
ipa_ds_path = r"data/Gezira_ipa_results.nc"
shapefile_path = r"data/Gezira_IR.json"

# Sidebar
with st.sidebar:

    st.logo(logo_wide, size="large", link='https://www.un-ihe.org/', icon_image=logo_small)
    if st.button("العربية"):
        st.session_state.language = "Arabic"
    if st.button("English"):
        st.session_state.language = "English"



# Dashboard Main Panel

# Initialize session state


season_list = list(dfm.season.unique())[::-1]
ll = list(dfm.columns.unique())[3:][::-1]
indicator_lst = [' '.join(l.split('_')[1:]) for l in ll]
indicator_lst = list(set(indicator_lst))


with col1:
	    
	 st.header("Dashboard Overview")

	 st.write('This dashboard provides an assessment of the irrigation performance of Gezira Scheme over the years ',season_list[-1][:4], ' - ', season_list[0][5:])
	 st.markdown(
	 """
	 Main cultivated crops are ,🌾 Sorghum, 🌿 Wheat and 🌼 Cotton.
	 """,
    	 unsafe_allow_html=True
	 )

 
	 st.write('Different indicators are used considering the sections and divisions of Gezira Scheme which are:')
	 st.write(indicator_lst)
	 st.markdown(f"All the data used for the analysis is obtained from [FAO WaPOR](https://data.apps.fao.org/wapor/?lang=en).")

st.write('Read more about Gezira Irrigation Scheme below in English or Arabic')




if st.session_state.get("language", "Arabic") == "English":
    	  support_arabic_text(all=False)
    	  text = english_txt
else:
    	  support_arabic_text(all=True)
    	  text = arabic_txt

st.markdown(text, unsafe_allow_html=True)


with col2:
	
	st.write ('')
	st.write('')
	st.write('')
	Gezira_scheme_image = "https://github.com/HanaAltom/Gezira_IPA_Team/blob/main/data/Gezira_Scheme.png"
	response = requests.get(Gezira_scheme_image)

	if response.status_code == 200:
    img = Image.open(BytesIO(response.content))
    st.image(img, caption="Image from URL", use_container_width=True)
	else:
    st.error("Could not fetch image")	
	st.image(Gezira_scheme_image, caption="Gezira Scheme Divisions", width=400)





