import streamlit as st
import pandas as pd
import numpy as np
import psutil
import subprocess

df = pd.DataFrame({
    "column 1": [5,3,1,5],
    "column 2": [9,5,8,2],
    "column 3": [9,1,2,5]
})

st.sidebar.header("User Sidebar")
st.sidebar.markdown("""
    Who knows what this is...
                    
    Maybe the users will know...
    
    Test another feature of this, maybe that will help
                    """)
st.sidebar.text("---------------")
st.sidebar.selectbox("Select", ("me", "you", "him"))
st.sidebar.slider("Gayness", 0, 100, 30)
st.sidebar.text_input("Name:")

# df
st.pyplot(df.plot.bar(stacked=True).figure)

# if __name__ == "__main__":
#     proc = subprocess.Popen(["streamlit", "run", "week05/streamlit_test.py"])