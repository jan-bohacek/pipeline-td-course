import streamlit as st
import pandas as pd
import json
import time

with open("week05/json/employees.json", "r") as file:
    data = json.load(file)

if "index" not in st.session_state:
    st.session_state.index = 0

keys = list(data.keys())

current_key = keys[st.session_state.index]
current_value = data[current_key]

st.title("Employees Info")
st.text(f"Name : {current_value["name"]}")
st.text(f"Title : {current_value["title"]}")
st.text(f"Age : {current_value["age"]}")

shows_df = pd.DataFrame({"Projects": current_value["shows"]})
st.dataframe(shows_df.style.hide(axis="index"), use_container_width=True)

st.session_state.index = (st.session_state.index + 1) % len(keys)
print(st.session_state.index)

time.sleep(1)
st.rerun()