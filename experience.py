import streamlit as st

from data import EXPERIENCE, ROLES, WORK_STYLE
from ui import card, heading, section

heading("Experience", "My work experience and the roles I am looking for")

for job in EXPERIENCE:
    card(job["title"], job["meta"], bullets=job["bullets"], accent=True)

section("Roles I am looking for")
columns = st.columns(3)
for column, (title, text, roles) in zip(columns, ROLES):
    with column:
        card(title, body=text, tags=roles)

card("How I want to work", body=WORK_STYLE, accent=True)
