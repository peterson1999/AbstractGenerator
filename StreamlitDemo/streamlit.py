# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import streamlit as st
from summarizer import Summarizer

# %%
st.title("Abstract Generator")
introduction = st.text_area('Introduction:') 
ratio1 = st.slider('How much would you like to take from the Introduction (%)?', 0, 100, 25)
methodology = st.text_area('Methodology:') 
ratio2 = st.slider('How much would you like to take from the Methodology (%)?', 0, 100, 25)
results = st.text_area('Results:')
ratio3 = st.slider('How much would you like to take from the Results (%)?', 0, 100, 25)
conclusion = st.text_area('Conclusion:') 
ratio4 = st.slider('How much would you like to take from the Conclusion (%)?', 0, 100, 25)

# %%
if st.button('Generate'):
    writer=st.write(Summarizer.getSummary(Summarizer,introduction,ratio1,methodology,ratio2,results,ratio3,conclusion,ratio4))


# %%