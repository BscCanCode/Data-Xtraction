import streamlit as st

st.set_page_config(
    page_title="Data Xtraction: Home",
    page_icon="📊",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

/* Overall Background */
body {
    background-color: #0E1117;
}

/* Sidebar Styling for multipage */
section[data-testid="stSidebarNav"] ul {
    margin-top: 20px;
}

section[data-testid="stSidebarNav"] li {
    margin-bottom: 10px;
}

section[data-testid="stSidebarNav"] a {
    font-size: 17px !important;
    padding: 10px 15px !important;
    border-radius: 25px !important;
    transition: 0.3s;
}

section[data-testid="stSidebarNav"] a:hover {
    background-color: #4DB6FF !important;
    color: black !important;
}

/* Hero Section */
.hero-title {
    font-size: 56px;
    font-weight: 800;
    text-align: center;
    color: #4DB6FF;
    margin-top: 70px;
}

.hero-sub {
    font-size: 20px;
    text-align: center;
    color: #CFCFCF;
    margin-bottom: 40px;
}

/* Section Titles */
.section-title {
    font-size: 32px;
    font-weight: 700;
    text-align: center;
    margin-top: 80px;
    margin-bottom: 40px;
    color: white;
}

/* Center Description Box */
.description-box {
    background-color: #151A22;
    padding: 28px;
    border-radius: 22px;
    border: 1px solid #2A2F3A;
    text-align: center;
    font-size: 18px;
    color: #EAEAEA;
}

/* Cards */
.card {
    background-color: #151A22;
    padding: 30px;
    border-radius: 20px;
    border: 1px solid #2A2F3A;
    text-align: center;
    color: #EAEAEA;
    transition: 0.3s;
    min-height: 190px;
}

.card:hover {
    transform: translateY(-6px);
    border: 1px solid #4DB6FF;
}

/* Footer */
.footer {
    text-align: center;
    padding: 40px;
    color: #777;
    margin-top: 90px;
    border-top: 1px solid #2A2F3A;
}

/* Bottom Note */
.bottom-note {
    text-align: center;
    margin-top: 70px;
    font-size: 16px;
    color: #4DB6FF;
    text-decoration: underline;
}

</style>
""", unsafe_allow_html=True)

# ================= HOME PAGE =================

# Hero
st.markdown('<div class="hero-title">📊 Data Xtraction & Analysis System</div>', unsafe_allow_html=True)
st.markdown('<div class="hero-sub">Smart Data Cleaning • Statistical Analysis • Data Visualization</div>', unsafe_allow_html=True)

# What This System Does
st.markdown('<div class="section-title">What This System Does</div>', unsafe_allow_html=True)

center = st.columns([1,2,1])
with center[1]:
    st.markdown("""
    <div class="description-box">
    This system enables users to upload structured datasets and perform 
    intelligent data cleaning, statistical analysis, and meaningful data visualization — 
    all within a clean, modern, and user-friendly interface.
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# Feature Cards
col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown("""
    <div class="card">
        <h3>📂 Upload Data</h3>
        <p style="color:#CCCCCC;">
        Upload CSV or Excel files for structured data analysis.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🧹 Clean Data</h3>
        <p style="color:#CCCCCC;">
        Handle missing values using smart and flexible cleaning strategies.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>📊 Analyze & Visualize</h3>
        <p style="color:#CCCCCC;">
        Generate summary statistics and create meaningful data visualizations.
        </p>
    </div>
    """, unsafe_allow_html=True)

# Why Choose Section
st.markdown('<div class="section-title">Why Choose This System?</div>', unsafe_allow_html=True)

col4, col5, col6 = st.columns(3, gap="large")

with col4:
    st.markdown("""
    <div class="card">
        <h4>Beginner Friendly</h4>
        Simple interface designed for ease of use.
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="card">
        <h4>Smart Data Handling</h4>
        Intelligent cleaning and accurate statistical outputs.
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="card">
        <h4>Modern & Structured</h4>
        Built for academic projects and small business needs.
    </div>
    """, unsafe_allow_html=True)

# Bottom Note
st.markdown('<div class="bottom-note">⚠ To explore more features, please use the sidebar navigation menu.</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
© 2026 Data Xtraction & Analysis System | TYBSc Computer Science Project
</div>
""", unsafe_allow_html=True)
