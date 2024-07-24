import streamlit as st
import random

st.header('주사위 게임', divider='rainbow')
isClicked = st.button('주사위던지기', type='primary')

if isClicked :
    n = random.randint(1, 6)
    st.image(f'img/{n}.png')