# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import streamlit as st
from summarizer import Summarizer

# %%
st.title("Abstract Generator")
introduction = st.text_area('Introduction:') 
ratio1 = st.slider('How much would you like to take from the introduction (%)?', 0, 100, 25)
methodology = st.text_area('methodology:') 
ratio2 = st.slider('How much would you like to take from the methodology (%)?', 0, 100, 25)
results = st.text_area('results:')
ratio3 = st.slider('How much would you like to take from the results (%)?', 0, 100, 25)
conclusion = st.text_area('conclusion:') 
ratio4 = st.slider('How much would you like to take from the conclusion (%)?', 0, 100, 25)

# %%
if st.button('Generate'):
    writer=st.write(Summarizer.getSummary(Summarizer,introduction,methodology,results,conclusion))


# %%