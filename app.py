import streamlit as st
from auth import register_user, login_user

st.set_page_config(page_title="Data Xtraction", layout="wide")

# Initialize session
if "authenticated" not in st.session_state:
    st.session_state.authenticated = False

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 54px;
    font-weight: 800;
    margin-top: 60px;
    color: #4DB6FF;
}
.sub-title {
    text-align: center;
    font-size: 20px;
    color: #CFCFCF;
    margin-bottom: 50px;
}
.tile {
    background-color: #151A22;
    padding: 30px;
    border-radius: 18px;
    border: 1px solid #2A2F3A;
    text-align: center;
    transition: 0.3s;
    min-height: 160px;
}
.tile:hover {
    border: 1px solid #4DB6FF;
    transform: translateY(-4px);
}
section[data-testid="stRadio"] {
    display: flex;
    justify-content: center;
}
.footer {
    text-align: center;
    color: gray;
    margin-top: 80px;
    padding: 20px;
    border-top: 1px solid #2A2F3A;
}
</style>
""", unsafe_allow_html=True)

# ================= LANDING PAGE =================
if not st.session_state.authenticated:

    st.markdown('<div class="main-title">📊 Data Xtraction</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Smart Data Cleaning • Statistical Analysis • Visualization</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="tile">
        <h4>Upload & Clean</h4>
        Handle missing values and structure datasets properly.
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="tile">
        <h4>Analyze</h4>
        Generate summary statistics for quick insights.
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="tile">
        <h4>Visualize</h4>
        Create charts and build a custom dashboard.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align:center; margin-top:40px; font-size:18px; color:#CFCFCF;'>
    To explore advanced features, generate insights, and build dashboards,<br>
    <span style='color:#4DB6FF; font-weight:600;'>
    please login or register to access the full system.
    </span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    center = st.columns([1,2,1])

    with center[1]:

        option = st.radio("", ["Login", "Register"], horizontal=True)

        st.markdown("<br>", unsafe_allow_html=True)

        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        # ---------------- REGISTER ----------------
        if option == "Register":
            if st.button("Create Account", use_container_width=True):

                success, message = register_user(email, password)

                if success:
                    st.success(message + " Please login.")
                else:
                    st.error(message)

        # ---------------- LOGIN ----------------
        if option == "Login":
            if st.button("Login to Continue", use_container_width=True):

                success, message = login_user(email, password)

                if success:
                    st.session_state.authenticated = True
                    st.success(message)
                    st.rerun()
                else:
                    st.error(message)

# ================= AFTER LOGIN =================
else:
    st.success("Logged in successfully!")
    st.write("Use the sidebar to access the system.")

    if st.button("Logout"):
        st.session_state.authenticated = False
        st.rerun()

# ================= FOOTER =================
st.markdown("""
<div class="footer">
© 2026 Data Xtraction & Analysis System | TYBSc Computer Science Project
</div>
""", unsafe_allow_html=True)