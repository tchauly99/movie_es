import streamlit as st
import src.movie_helpers as helpers

import pandas as pd

df = (
    pd.read_csv("data/wiki_movie_plots_deduped.csv")
    .dropna()
    .sample(5000, random_state=42)
    .reset_index()
)

# Ensure the entire page is loaded
st.set_page_config(layout="wide")

# Add Header and title to the sidebar
st.header("The :red[Wiki Movie search] :green[with] :violet[ElasticSearch] :orange[by our team] :earth_americas:")
st.sidebar.title(":blue[Search by: ] ")
my_separator = "---"
st.sidebar.markdown(my_separator, unsafe_allow_html=False)

""":violet[Search by Free Text]"""
############################################
text = st.sidebar.text_input(":orange[Free text search]")
############################################
if text:
    ret_str = helpers.free_text_search(text)
    st.text(ret_str)

""":violet[Search by Release Year]"""
############################################
search_id = st.sidebar.text_input(":orange[Release Year]")

if search_id:
    ret_df = helpers.release_year_search(df, search_id)
    ret_table = st.dataframe(data=ret_df.style.hide(axis="index"), width=1200, hide_index=True)

""":violet[Search by Title]"""
############################################
search_id = st.sidebar.text_input(":orange[Title]")

if search_id:
    ret_str = helpers.title_search(search_id)
    st.text(ret_str)

""":violet[Search by Origin]"""
############################################
search_id = st.sidebar.text_input(":orange[Origin]")

if search_id:
    ret_str = helpers.origin_search(search_id)
    st.text(ret_str)

""":violet[Search by Director]"""
############################################
search_id = st.sidebar.text_input(":orange[Director]")

if search_id:
    ret_str = helpers.director_search(search_id)
    st.text(ret_str)

""":violet[Search by Cast]"""
############################################
search_id = st.sidebar.text_input(":orange[Cast]")

if search_id:
    ret_str = helpers.cast_search(search_id)
    st.text(ret_str)

""":violet[Search by Genre]"""
############################################
search_id = st.sidebar.text_input(":orange[Genre]")

if search_id:
    ret_str = helpers.genre_search(search_id)
    st.text(ret_str)

""":violet[Search by Plot]"""
############################################
search_id = st.sidebar.text_input(":orange[Plot]")

if search_id:
    ret_str = helpers.plot_search(search_id)
    st.text(ret_str)
#Release Year,Title,Origin/Ethnicity,Director,Cast,Genre,Wiki Page,Plot