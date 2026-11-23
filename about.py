import streamlit as st

from data import ACTIVITIES, INTERESTS, SKILLS
from ui import card, heading, section

heading("About me", "Who I am and what I work with")

c1, c2 = st.columns(2, gap="large")
with c1:
    st.write(
        "I recently completed my M.Sc in Computer Science and spent my final year building an AI sports "
        "nutrition chatbot from the dataset up: preparing the data, fine-tuning a language model, designing "
        "the prompts, and testing the answers."
    )
    st.write("Before that, I interned in AI and machine learning and built a Streamlit study assistant on top of an LLM API.")
with c2:
    st.write(
        "I communicate clearly, explain things patiently, and enjoy helping teammates get unstuck. Those habits "
        "make me comfortable in client-facing work as well as in engineering teams."
    )
    st.write("Languages: English (professional), Malayalam (native), Hindi (professional), Tamil (basic).")

section("Skills")
st.caption("Tap any skill to see what it is and where I used it.")
for group, items in SKILLS.items():
    st.markdown(f'<h4 class="group">{group}</h4>', unsafe_allow_html=True)
    pick = st.pills(group, list(items), key=f"skill_{group}", label_visibility="collapsed")
    if pick:
        description, used = items[pick]
        extra = f'<p class="used">Where I used it: {used}</p>' if used else ""
        st.markdown(f'<div class="info"><b>{pick}</b><p>{description}</p>{extra}</div>', unsafe_allow_html=True)

section("Interests")
card("What I love learning about", tags=INTERESTS)

section("Extra-curricular activities")
card("Sports I play", tags=ACTIVITIES)
