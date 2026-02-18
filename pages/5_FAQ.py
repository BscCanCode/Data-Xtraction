import streamlit as st
st.set_page_config(page_title="Frequently asked questions", layout="wide")
st.title("FAQ")


st.title("❓ Frequently Asked Questions")

# ---------- CSS ----------
st.markdown("""
<style>

.faq-tile {
    background-color: #151A22;
    padding: 20px;
    border-radius: 18px;
    border: 1px solid #2A2F3A;
    color: #EAEAEA;
    margin-bottom: 20px;
}

.faq-tile:hover {
    border: 1px solid #4DB6FF;
    transition: 0.3s;
}

.question {
    font-weight: 600;
    font-size: 18px;
    margin-bottom: 8px;
}

</style>
""", unsafe_allow_html=True)

# ---------- FAQ ITEMS ----------

st.markdown("""
<div class="faq-tile">
    <div class="question">1️⃣ What file formats are supported?</div>
    <p>The system currently supports CSV (.csv) and Excel (.xlsx) files.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="faq-tile">
    <div class="question">2️⃣ Does the system modify my original dataset?</div>
    <p>No. The original file is not permanently modified. All operations are performed within the application session.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="faq-tile">
    <div class="question">3️⃣ Do I need programming knowledge to use this system?</div>
    <p>No. The system is designed with a user-friendly interface so that even non-technical users can analyze data.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="faq-tile">
    <div class="question">4️⃣ Can this system replace advanced BI tools?</div>
    <p>No. This system provides basic data cleaning, summaries, and visualization. It is intended for academic and small business use, not enterprise-level analytics.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="faq-tile">
    <div class="question">5️⃣ Who can benefit from this system?</div>
    <p>Students, researchers, and small businesses looking for structured insights without using complex data analysis software.</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<hr>
<div style="text-align:center; color:gray;">
© 2026 Data Xtraction & Analysis System | TYBSc Computer Science Project
</div>
""", unsafe_allow_html=True)
