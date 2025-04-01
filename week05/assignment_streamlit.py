import streamlit as st
import json
import time

with open("week05/json/posts.json", "r") as file:
    data = json.load(file)

if "index" not in st.session_state:
    st.session_state.index = 0
    repeat = False

st.sidebar.header("Settings")
num = st.sidebar.slider("Items to List", 1, len(data), 5)
delay = st.sidebar.slider("Display Time", 1, 10, 5)

st.title("JSON Data Display:")

idx = st.session_state.index
for key in data[idx].keys():
    col1, col2 = st.columns([1,3])
    with col1:
        st.markdown(f"<p style='color: orange; font-weight: bold'>{key}</style>", unsafe_allow_html=True)
    with col2:
        st.text(data[idx][key])

placeholder = st.empty()
if st.session_state.index + 1 == num:
    placeholder.markdown(f"<p style='color: grey'><i>Limit reached, starting from the beginning...</i></style>", unsafe_allow_html=True)
else:
    placeholder.empty()

st.session_state.index = (st.session_state.index + 1) % num

time.sleep(delay)
st.rerun()