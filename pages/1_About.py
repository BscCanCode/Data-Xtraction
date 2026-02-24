import streamlit as st

if not st.session_state.get("authenticated"):
    st.warning("Please login to access this page.")
    st.stop()

st.set_page_config(page_title="About", layout="wide")


st.title(" About This Project")

# ---------- CSS for Tiles ----------
st.markdown("""
<style>

.tile {
    background-color: #151A22;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #2A2F3A;
    color: #EAEAEA;
    margin-bottom: 25px;
}

.tile:hover {
    border: 1px solid #4DB6FF;
    transition: 0.3s;
}

.section-title {
    font-size: 28px;
    font-weight: 600;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)

# ---------- What the System Does ----------
st.markdown("""
<div class="tile">
    <div class="section-title">📊 What This System Does</div>
    <p>
    The Data Xtraction & Analysis System allows users to upload structured 
    CSV or Excel datasets and perform basic data cleaning, statistical analysis, 
    and data visualization.
    </p>
    <p>
    It focuses on providing clear summaries and structured insights from raw data 
    without requiring advanced technical knowledge.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------- How It Works ----------
st.markdown("""
<div class="tile">
    <div class="section-title">⚙ How It Works</div>
    <p>
    Users upload a dataset, after which the system:
    </p>
    <ul>
        <li>Identifies and handles missing values</li>
        <li>Generates statistical summaries</li>
        <li>Provides structured overview of the dataset</li>
        <li>Creates visual representations for easier understanding</li>
    </ul>
    <p>
    The goal is to simplify raw data into understandable information.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------- Who Can Use It ----------
st.markdown("""
<div class="tile">
    <div class="section-title">👥 Who Can Use It</div>
    <p>
    This system is designed for:
    </p>
    <ul>
        <li>Students working on academic data projects</li>
        <li>Small businesses seeking basic data insights</li>
        <li>Individuals who want structured summaries without complex tools</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# ---------- Purpose & Vision ----------
st.markdown("""
<div class="tile">
    <div class="section-title">🎯 Purpose of the Project</div>
    <p>
    The purpose of this project is not to replace advanced Business Intelligence 
    tools, but to provide a simple and accessible platform for understanding data 
    at a fundamental level.
    </p>
    <p>
    It aims to make data interpretation easier for users who need meaningful insights 
    without relying on complex enterprise software.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<hr>
<div style="text-align:center; color:gray;">
© 2026 Data Xtraction & Analysis System | TYBSc Computer Science Project
</div>
""", unsafe_allow_html=True)