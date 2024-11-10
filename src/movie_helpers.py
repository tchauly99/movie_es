import streamlit as st
import pandas as pd
from elasticsearch import Elasticsearch
from streamlit_folium import folium_static
import folium
from datetime import datetime

# Connect to Elasticsearch
# es = Elasticsearch("http://localhost:9200")


@st.cache_data
def query_data(df, key_str, value):
    ret_df = df[df[key_str]==int(value)]
    # Move the column with the key string to first
    first_column = ret_df.pop(key_str) 
    ret_df.insert(0, key_str, first_column)
    # Eliminate the index column
    ret_df.pop('index')
    return ret_df

@st.cache_data
def release_year_search(df, release_year):
    key_str = 'Release Year'
    return query_data(df, key_str, release_year)

@st.cache_data
def free_text_search(free_text):
    return "This is output from Free Text search of " + free_text

@st.cache_data
def title_search(title):
    return "This is output from Title search of " + title

@st.cache_data
def origin_search(origin):
    return "This is output from Origin search of " + origin

@st.cache_data
def director_search(director):
    return "This is output from Director search of " + director

@st.cache_data
def cast_search(cast):
    return "This is output from Cast search of " + cast

@st.cache_data
def genre_search(genre):
    return "This is output from Genre search of " + genre

@st.cache_data
def plot_search(plot):
    return "This is output from Plot search of " + plot

#Release Year,Title,Origin/Ethnicity,Director,Cast,Genre,Wiki Page,Plot


