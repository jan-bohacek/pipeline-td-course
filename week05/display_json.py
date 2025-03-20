import streamlit as st
import pandas as pd
import json
import time

with open("week05/json/dummy_data.json", "r") as json_file:
    data = json.load(json_file)

placeholder = st.empty()

for d in data.items():
    # df = pd.DataFrame(d)
    # df

    with placeholder.container():
        st.write("Printifsfasf")
        st.dataframe(d)

    time.sleep(3)
    st.rerun()

