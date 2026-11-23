# Small helpers shared by every page.
import base64
from pathlib import Path

import streamlit as st

ASSETS = Path(__file__).parent / "assets"


@st.cache_resource
def photo_uri():
    data = (ASSETS / "dp.webp").read_bytes()
    return "data:image/webp;base64," + base64.b64encode(data).decode()


@st.cache_resource
def pdf_bytes(name):
    return (ASSETS / name).read_bytes()


def heading(title, subtitle=""):
    html = f'<div class="page-head"><h1>{title}</h1>'
    if subtitle:
        html += f"<p>{subtitle}</p>"
    st.markdown(html + "</div>", unsafe_allow_html=True)


def section(title):
    st.markdown(f'<h2 class="section">{title}</h2>', unsafe_allow_html=True)


def card(title, meta="", body="", bullets=(), tags=(), accent=False):
    html = f'<div class="card{" accent" if accent else ""}"><h3>{title}</h3>'
    if meta:
        html += f'<p class="meta">{meta}</p>'
    if body:
        html += f"<p>{body}</p>"
    if bullets:
        html += "<ul>" + "".join(f"<li>{b}</li>" for b in bullets) + "</ul>"
    html += "".join(f'<span class="tag">{t}</span>' for t in tags) + "</div>"
    st.markdown(html, unsafe_allow_html=True)


@st.dialog("Aswin Vinu")
def show_photo():
    st.markdown(f'<div class="dp-wrap big"><img src="{photo_uri()}" alt="Aswin Vinu"></div>', unsafe_allow_html=True)


def project_card(p, accent=False):
    html = f'<div class="card{" accent" if accent else ""}"><h3>{p["title"]}</h3><p class="meta">{p["meta"]}</p>'
    html += f'<p class="label">Overview</p><p>{p["overview"]}</p>'
    html += '<p class="label">How it works</p><ol>' + "".join(f"<li>{s}</li>" for s in p["how"]) + "</ol>"
    html += '<p class="label">What I did</p><ul>' + "".join(f"<li>{s}</li>" for s in p["built"]) + "</ul>"
    html += '<p class="label">Tools</p>' + "".join(f'<span class="tag">{t}</span>' for t in p["tags"]) + "</div>"
    st.markdown(html, unsafe_allow_html=True)
