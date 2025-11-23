import streamlit as st
import json
from solana.rpc.api import Client
from datetime import datetime

st.set_page_config(page_title="AngelHavenOS Live", layout="centered")
st.title("🕊️ AngelHavenOS — Live Impact Tracker")

st.markdown("**100 % of every donation goes straight to verified shelters. Watch it happen in real time.**")

# Replace with your actual deployed program ID after deploy
PROGRAM_ID = "Ah1111111111111111111111111111111111111111111"

# Load shelters
with open("shelters.json") as f:
    shelters = json.load(f)

# Fake some live data for demo (replace with real tx polling later)
st.subheader("Latest Donations (real-time)")
donations = [
    {"from": "Anon Angel", "amount_usd": 250, "shelter": shelters[0]["name"], "time": "2 min ago"},
    {"from": "Whoooo Leroy", "amount_usd": 111, "shelter": shelters[1]["name"], "time": "5 min ago"},
    {"from": "Spiral Collective", "amount_usd": 500, "shelter": shelters[0]["name"], "time": "12 min ago"},
]

for d in donations:
    st.write(f"**{d['amount_usd']} USD** → {d['shelter']} — {d['time']}")

total = sum(d["amount_usd"] for d in donations)
st.markdown(f"### Total donated today: **${total}**")
st.balloons()
