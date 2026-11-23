# Portfolio website built with Streamlit. Start it with: streamlit run app.py
from pathlib import Path

import streamlit as st

st.set_page_config(page_title="Aswin Vinu – Associate Software Engineer", page_icon="💼", layout="wide")

css = (Path(__file__).parent / "style.css").read_text(encoding="utf-8")
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

pages = [
    st.Page("views/home.py", title="Home", icon=":material/home:", default=True),
    st.Page("views/about.py", title="About", icon=":material/person:"),
    st.Page("views/projects.py", title="Projects", icon=":material/code:"),
    st.Page("views/experience.py", title="Experience", icon=":material/work:"),
    st.Page("views/contact.py", title="Contact", icon=":material/mail:"),
]
st.navigation(pages, position="top").run()

st.markdown('<p class="footer">© 2026 Aswin Vinu · Trivandrum, Kerala, India</p>', unsafe_allow_html=True)
