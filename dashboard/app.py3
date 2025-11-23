import streamlit as st
st.set_page_config(page_title="AngelHavenOS", layout="centered")
st.title("🕊️ AngelHavenOS — Live")
st.write("**100 % of every donation goes straight to verified shelters. No fees. Forever.**")

donations = [
    {"usd":500, "shelter":"Destiny Rescue Thailand"},
    {"usd":111, "shelter":"Love146 Philippines"},
    {"usd":250, "shelter":"A21 Safe House"}
]

for d in donations:
    st.write(f"**${d['usd']}** → {d['shelter']}")

st.write(f"### Total today: **${sum(d['usd'] for d in donations)}**")
st.balloons()
