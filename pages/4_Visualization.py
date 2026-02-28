import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io

if not st.session_state.get("authenticated"):
    st.warning("Please login to access this page.")
    st.stop()

st.set_page_config(page_title="📈 Visualization", layout="wide")

st.title("📈 Data Visualization")

# ---------------- Initialize Dashboard Storage ----------------
if "dashboard_plots" not in st.session_state:
    st.session_state.dashboard_plots = []

# ---------------- Upload File ----------------
file = st.file_uploader("Upload Cleaned File (CSV or Excel)", type=["csv", "xlsx"])

if file is not None:

    if file.name.endswith(".csv"):
        df = pd.read_csv(file, na_values=["", "NA", "NaN", "None","N/A", "null", "NULL", "?"])

    else:
        df = pd.read_excel(file, na_values=["", "NA", "NaN", "None","N/A", "null", "NULL", "?"])

    st.success("File uploaded successfully!")
    st.dataframe(df.head())

    # ---------------- Missing Check ----------------
    total_missing = df.isnull().sum().sum()

    if total_missing > 0:
        st.warning(f"Dataset contains {total_missing} missing values.")
        proceed = st.checkbox("Proceed anyway?")
        if not proceed:
            st.stop()

    # ---------------- Chart Builder ----------------
    st.subheader("Create Plot")

    chart_type = st.selectbox(
        "Select Chart Type",
        ["Line Chart", "Bar Chart", "Histogram", "Pie Chart", "Scatter Plot"]
    )

    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()
    categorical_columns = df.select_dtypes(exclude=["number"]).columns.tolist()

    fig = None

    # ---------------- Histogram ----------------
    if chart_type == "Histogram":

        if not numeric_columns:
            st.error("No numeric columns available for histogram.")
            st.stop()

        column = st.selectbox("Select Column", numeric_columns)

        fig, ax = plt.subplots()
        ax.hist(df[column], bins=20)
        ax.set_title(f"Histogram of {column}")
        ax.set_xlabel(column)
        ax.set_ylabel("Frequency")



    # ---------------- Pie Chart ----------------
    elif chart_type == "Pie Chart":

        if not categorical_columns:
            st.error("No categorical columns available for pie chart.")
            st.stop()

        column = st.selectbox("Select Column", categorical_columns)

        value_counts = df[column].value_counts()

        fig, ax = plt.subplots()
        ax.pie(value_counts, labels=value_counts.index, autopct="%1.1f%%")
        ax.set_title(f"Pie Chart of {column}")

    # ---------------- Line / Bar ----------------
    else:

        if not numeric_columns:
            st.error("No numeric columns available for plotting.")
            st.stop()

        fig, ax = plt.subplots()

        if chart_type == "Line Chart":
            x_column = st.selectbox("Select X-axis Column", df.columns)
            y_column = st.selectbox("Select Y-axis Column", numeric_columns)
            ax.plot(df[x_column], df[y_column])

        elif chart_type == "Bar Chart":
            x_column = st.selectbox("Select X-axis Column", df.columns)
            y_column = st.selectbox("Select Y-axis Column", numeric_columns)
            ax.bar(df[x_column], df[y_column])

        elif chart_type == "Scatter Plot":
            x_column = st.selectbox("Select X-axis Column", numeric_columns)
            y_column = st.selectbox("Select Y-axis Column", numeric_columns)
            ax.scatter(df[x_column], df[y_column])

            corr = df[x_column].corr(df[y_column])
            st.info(f"Correlation between {x_column} and {y_column}: {corr:.2f}")

        ax.set_title(f"{chart_type} of {y_column}")
        ax.set_xlabel(x_column)
        ax.set_ylabel(y_column)
        plt.xticks(rotation=45)

    # ---------------- Display & Save Plot ----------------
    if fig:
        st.pyplot(fig)

        buf = io.BytesIO()
        fig.savefig(buf, format="png")
        buf.seek(0)

        st.download_button(
            label="⬇ Download This Plot",
            data=buf,
            file_name="plot.png",
            mime="image/png"
        )

        if st.button("➕ Add to Dashboard"):
            st.session_state.dashboard_plots.append(buf.getvalue())
            st.success("Plot added to dashboard!")

# ---------------- Dashboard Section ----------------
st.markdown("---")
st.subheader("📊 Dashboard")

if st.session_state.dashboard_plots:

    cols = st.columns(2)

    for i, plot_img in enumerate(st.session_state.dashboard_plots):

        with cols[i % 2]:
            st.image(plot_img)

            if st.button(f"Remove Plot {i+1}", key=f"remove_{i}"):
                st.session_state.dashboard_plots.pop(i)
                st.rerun()
                break

    if st.button("⬇ Download Full Dashboard"):

        dashboard_fig, axs = plt.subplots(
            len(st.session_state.dashboard_plots),
            1,
            figsize=(6, 4 * len(st.session_state.dashboard_plots))
        )

        if len(st.session_state.dashboard_plots) == 1:
            axs = [axs]

        for ax, img in zip(axs, st.session_state.dashboard_plots):
            image = plt.imread(io.BytesIO(img))
            ax.imshow(image)
            ax.axis("off")

        dashboard_buf = io.BytesIO()
        dashboard_fig.savefig(dashboard_buf, format="png")
        dashboard_buf.seek(0)

        st.download_button(
            label="Download Dashboard Image",
            data=dashboard_buf,
            file_name="dashboard.png",
            mime="image/png"
        )

else:
    st.info("No plots added to dashboard yet.")

# ---------------- Footer ----------------
st.markdown("""
<hr>
<div style="text-align:center; color:gray;">
© 2026 Data Xtraction & Analysis System | TYBSc Computer Science Project
</div>
""", unsafe_allow_html=True)
