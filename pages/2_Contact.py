import streamlit as st

st.set_page_config(page_title="📞 Contact", layout="wide")
st.title("📞 Contact")

# ---------- CSS for Tiles ----------
st.markdown("""
<style>

.tile {
    background-color: #151A22;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #2A2F3A;
    color: #EAEAEA;
}

.tile:hover {
    border: 1px solid #4DB6FF;
    transition: 0.3s;
}

</style>
""", unsafe_allow_html=True)

st.markdown("## Project Information")

col1, col2 = st.columns(2)

# ---------- Developer Tile ----------
with col1:
    st.markdown("""
    <div class="tile">
        <h3>👤 Developer</h3>
        <p><b>Name:</b> Siddhesh Tambe</p>
        <p><b>Course:</b> TYBSc Computer Science</p>
        <p><b>Project:</b> Data Xtraction – Interpretation & Analysis</p>
    </div>
    """, unsafe_allow_html=True)

# ---------- Institution Tile ----------
with col2:
    st.markdown("""
    <div class="tile">
        <h3>Additional-Information</h3>
        <p> TYBsc Project_Work-2 </p>
        <p><b>Academic Year:</b> 2025 – 2026</p>
        <p><b>Email:</b> xabc31101@gmail.com</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.info("For academic queries or project-related discussions, please contact using the details above.")
