# -*- coding: utf-8 -*-
"""
Created on Sun May 28 14:52:38 2023

@author: Prayag V K
"""

import streamlit as st
import pickle
import pandas as pd

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)


similarity=pickle.load(open('similarity.pkl','rb'))


def recommend(movie):
    movie_index=movies[movies['title']==movie].index[0]
    distances=similarity[movie_index]
    movie_list=sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    
    recommended_movies=[]
    
    for i in movie_list:
        movie_id=i[0]
        
        # Fetch poster.
        recommended_movies.append(movies.iloc[i[0]].title)
    
    return recommended_movies

st.title("Movie Recommendation System 📽️")

option=st.selectbox('Select movies for recommendation', movies['title'].values)

if st.button('Recommend'):
    recommendations =recommend(option)
    for i in recommendations:
        st.write(i)