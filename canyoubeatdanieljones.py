
import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import time
from datetime import datetime, timedelta, date
import altair as alt
import requests
import matplotlib
import io
import warnings
from PIL import Image

warnings.filterwarnings('ignore')

st.sidebar.write('https://github.com/kanerhee')
st.sidebar.title('Shouts out to: ')
st.sidebar.text('@SimonKurtisRhee')
st.sidebar.text('@JordnCPierce_')
st.sidebar.text('@Tiefkowski')
st.sidebar.text('@Ikewafeena')
st.sidebar.text('@JoeyLieberman9')
st.sidebar.text('@EvanColesLewis')
st.sidebar.text('@Hayashi69')

def app():

    st.title('Can You Beat Daniel Jones in a Fight?')
    st.write('by Kane Rhee')

    st.subheader('Basic Info: ')

    danieljonespoints = 6
    totalpoints = 0
    # Slider For Age:
    yourage = st.slider('What is your age?',
        0, 100, (0)
    )
    if yourage < 40:
        if yourage > 18:
            totalpoints = totalpoints + 2

    # Slider for Weight:
    yourheight = st.slider('What is your height?',
        0.0, 8.0, (0.0)
    )
    if yourheight < 8.0:
        if yourheight > 5.5:
            totalpoints = totalpoints + 2

    # Slider for Weight:
    yourweight = st.slider('What is your weight?',
        0.0, 300.0, (0.0)
    )
    if yourweight < 290:
        if yourweight > 140:
            totalpoints = totalpoints + 2

    # Slider for 40 time:
    your40 = st.slider(
        'How fast can you run the 40 yard dash?',
        0.0, 10.0, (0.0)
    )
    if your40 < 4.9:
        totalpoints = totalpoints + 1

    if your40:
        haveyoufell = ['Yes', 'No']
        fellresults = st.multiselect('Have you ever stumbled and fell while running the 40?', haveyoufell)

        if haveyoufell:
            if haveyoufell == 'Yes':
                totalpoints = totalpoints - 3
            elif haveyoufell == 'No':
                totalpoints = totalpoints + 1

    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")

    if your40:
        if yourweight:
            if yourheight:
                if yourage:
                    st.header('Calculating odds against Daniel Jones...')
                    time.sleep(4)
                    st.write('Done!')
                    st.text("")
                    st.text("")
                    time.sleep(2)

                    col1, col2 = st.beta_columns(2)

                    if danieljonespoints >= totalpoints:

                        with col1:
                            image = Image.open('/Users/kanerhee/Desktop/github/canyoubeatdanieljones/danhappy.png')
                            st.image(image, use_column_width=True)
                        with col2:
                            st.subheader('No!')
                            st.write('Run for your life. You never know where Daniel Jones is hiding.')

                    elif totalpoints > danieljonespoints:

                        with col1:
                            image = Image.open('/Users/kanerhee/Desktop/github/canyoubeatdanieljones/dansad.png')
                            st.image(image, use_column_width=True)
                        with col2:
                            st.subheader('Yes!')
                            st.write('Rest assured, should you ever cross paths with Daniel Jones, you should easily be able to beat him in fight.')

    st.text("")
    st.text("")
    st.text("")
    st.write(totalpoints)





app()
