import streamlit as st
import pandas as pd
import json
import time

with open("week05/json/dummy_data.json", "r") as json_file:
    data = json.load(json_file)

if "index" not in st.session_state:
    st.session_state.index = 0

keys = list(data.keys())

cur_key = keys[st.session_state.index]
cur_value = data[cur_key]

st.subheader(f"Current key : {cur_key}")
st.write(cur_value)

st.session_state.index = (st.session_state.index + 1) % len(keys)
print(st.session_state.index)

time.sleep(1)
st.rerun()

# for d in data.items():
#     # df = pd.DataFrame(d)
#     # df

#     st.write("Printifsfasf")
#     st.dataframe(d)

#     time.sleep(3)
#     st.rerun()

