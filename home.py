import streamlit as st

from data import CERTS, EDUCATION, PROJECTS, STATS, TICKER
from ui import card, pdf_bytes, photo_uri, section, show_photo

left, right = st.columns([1.25, 1], vertical_alignment="center", gap="large")

with left:
    st.markdown(
        '<span class="pill"><i class="dot"></i>Available for new roles</span>'
        '<h1 class="hero-name">Aswin <span>Vinu</span></h1>'
        '<div class="roles"><span>Associate Software Engineer</span><span>AI and ML builder</span>'
        "<span>Python developer</span><span>Team player who loves teaching</span></div>"
        '<p class="lead">M.Sc Computer Science graduate building practical AI tools with Python, from '
        "fine-tuned language models to simple apps people can use. Open to remote and hybrid roles.</p>",
        unsafe_allow_html=True,
    )
    b1, b2, b3 = st.columns(3)
    with b1:
        st.page_link("views/projects.py", label="View my work", icon=":material/arrow_outward:")
    with b2:
        st.download_button("Resume", pdf_bytes("Aswin_Vinu_Resume.pdf"), "Aswin_Vinu_Resume.pdf",
                           "application/pdf", icon=":material/download:", type="primary", use_container_width=True)
    with b3:
        st.page_link("views/contact.py", label="Contact me", icon=":material/mail:")

with right:
    st.markdown(f'<div class="dp-wrap"><img src="{photo_uri()}" alt="Aswin Vinu"></div>', unsafe_allow_html=True)
    _, middle, _ = st.columns([1, 2, 1])
    if middle.button("Tap photo to view", use_container_width=True):
        show_photo()

st.markdown(
    '<div class="marq"><div class="track">' + "".join(f"<span>{t}</span>" for t in TICKER * 2) + "</div></div>",
    unsafe_allow_html=True,
)

section("What I do")
c1, c2, c3 = st.columns(3)
with c1:
    card("AI and LLM", body="Fine-tuning and prompting language models to build helpful chatbots and study tools.")
with c2:
    card("Web Development", body="Building web apps and APIs with Python, Streamlit, Gradio, FastAPI and Django.")
with c3:
    card("Communication", body="I explain things patiently and enjoy helping teammates and clients get unstuck.")

section("Featured Project")
project = PROJECTS[0]
card(project["title"], project["meta"], project["summary"], tags=project["tags"], accent=True)
st.page_link("views/projects.py", label="See all projects", icon=":material/arrow_forward:")

section("Education")
columns = st.columns(2)
for column, (degree, college, grade) in zip(columns, EDUCATION):
    with column:
        card(degree, college, grade)

section("Certifications")
columns = st.columns(2)
for i, (name, issuer, extra) in enumerate(CERTS):
    with columns[i % 2]:
        card(name, issuer, extra)

st.markdown(
    '<div class="stats">'
    + "".join(f'<div class="stat"><b>{n}</b><span>{label}</span></div>' for n, label in STATS)
    + "</div>",
    unsafe_allow_html=True,
)
