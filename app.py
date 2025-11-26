import streamlit as st
import pathlib

st.set_page_config(page_title="MegaServe - Trading Algorithms", layout="wide")

# Remove default Streamlit padding
st.markdown("""
<style>
.block-container {
    padding: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# Load HTML
html_file = pathlib.Path("C:\\Users\\admin\\Downloads\\page\\TEMP_BROKER.html").read_text(encoding="utf-8")

# Render
st.components.v1.html(html_file, height=1000, scrolling=False)
