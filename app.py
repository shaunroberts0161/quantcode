import streamlit as st
import pandas as pd

st.title("QuantCode™")
st.write("**Rank energy quants by model accuracy + GitHub impact**")

# Hardcoded data (will auto-update later)
data = [
    {"Quant": "Dr. Elena Kim", "Score": 94, "LMP Error": "3.8%", "Stars": 1200, "Company": "VoltPeak"},
    {"Quant": "Alex Chen", "Score": 89, "LMP Error": "4.1%", "Stars": 890, "Company": "Calpine"},
    {"Quant": "Priya Patel", "Score": 87, "LMP Error": "4.5%", "Stars": 720, "Company": "Aurora Grid"},
]
df = pd.DataFrame(data)
st.dataframe(df)

# Download buttons
csv = df.to_csv(index=False)
st.download_button("Download Leaderboard", csv, "quantcode_leaderboard.csv", "text/csv")

pdf_text = """QuantCode™ Scorecard
────────────────────
Name: Dr. Elena Kim
Score: 94/100
LMP Error: 3.8%
GitHub Stars: 1,200
Company: VoltPeak
Desk: Battery ML
"""
st.download_button("Download Sample Scorecard", pdf_text, "quantcard_elena_kim.pdf", "text/plain")
