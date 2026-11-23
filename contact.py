from urllib.parse import quote

import streamlit as st

from data import EMAIL, GITHUB, LINKEDIN, LOCATION
from ui import card, heading, pdf_bytes

heading("Contact", "I am available immediately for full-time roles and internships, remote or hybrid")

left, right = st.columns([1, 1.2], gap="large")

with left:
    card("Get in touch", LOCATION, f"<b>{EMAIL}</b><br>Immediate joiner · Open to relocation")
    a, b = st.columns(2)
    a.link_button("LinkedIn", LINKEDIN, use_container_width=True)
    b.link_button("GitHub", GITHUB, use_container_width=True)
    st.markdown("**Resume and CV**")
    c, d = st.columns(2)
    c.download_button("Resume", pdf_bytes("Aswin_Vinu_Resume.pdf"), "Aswin_Vinu_Resume.pdf",
                      "application/pdf", icon=":material/download:", use_container_width=True)
    d.download_button("CV", pdf_bytes("Aswin_Vinu_CV.pdf"), "Aswin_Vinu_CV.pdf",
                      "application/pdf", icon=":material/download:", use_container_width=True)

with right:
    st.subheader("Send me a message")
    name = st.text_input("Your name")
    subject = st.text_input("Subject", value="Opportunity for Aswin")
    message = st.text_area("Message", height=140)
    body = f"{message}\n\n{name}"
    link = f"mailto:{EMAIL}?subject={quote(subject)}&body={quote(body)}"
    st.link_button("Open in my email app", link, type="primary", icon=":material/send:")
    st.caption("This opens your email app with the message already filled in.")
