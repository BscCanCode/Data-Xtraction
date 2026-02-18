import pandas as pd
import streamlit as st

st.set_page_config(page_title="Data Xtraction", layout="wide")

st.title("📊 Data Xtraction")
st.subheader("Interpretation and Analysis of Data")

file = st.file_uploader("Upload File", type=["csv", "xlsx"])

if file is not None:

    # =========================
    # Read File
    # =========================
    if file.name.endswith(".csv"):
        df = pd.read_csv(file)
    else:
        df = pd.read_excel(file)

    st.success("File uploaded successfully!")

    # =========================
    # Dataset Preview
    # =========================
    st.subheader("Dataset Preview")
    st.dataframe(df)

    # =========================
    # Missing Value Report
    # =========================
    st.subheader("Missing Value Report")

    missing_values = df.isnull().sum()
    total_missing = missing_values.sum()

    st.write("Total Missing Values:", total_missing)
    st.dataframe(missing_values[missing_values > 0])

    cleaned_df = None  # 🔹 To track cleaned data

    # =========================
    # Missing Value Handling
    # =========================
    if total_missing > 0:

        st.subheader("Missing Value Handling")

        method = st.selectbox(
            "Select method to fill missing values:",
            [
                "Median (Numeric) + Mode (Categorical)",
                "Mean (Numeric) + Mode (Categorical)",
                "Fill with 0",
                "Manual Value"
            ]
        )

        manual_value = None
        if method == "Manual Value":
            manual_value = st.text_input("Enter value to fill missing data:")

        if st.button("Apply Cleaning"):

            numeric_cols = df.select_dtypes(include=["number"]).columns
            categorical_cols = df.select_dtypes(exclude=["number"]).columns

            filled_info = {}

            if method == "Median (Numeric) + Mode (Categorical)":

                for col in numeric_cols:
                    if df[col].isnull().sum() > 0:
                        fill_val = df[col].median()
                        df[col] = df[col].fillna(fill_val)
                        filled_info[col] = fill_val

                for col in categorical_cols:
                    if df[col].isnull().sum() > 0:
                        fill_val = df[col].mode()[0]
                        df[col] = df[col].fillna(fill_val)
                        filled_info[col] = fill_val

            elif method == "Mean (Numeric) + Mode (Categorical)":

                for col in numeric_cols:
                    if df[col].isnull().sum() > 0:
                        fill_val = df[col].mean()
                        df[col] = df[col].fillna(fill_val)
                        filled_info[col] = fill_val

                for col in categorical_cols:
                    if df[col].isnull().sum() > 0:
                        fill_val = df[col].mode()[0]
                        df[col] = df[col].fillna(fill_val)
                        filled_info[col] = fill_val

            elif method == "Fill with 0":
                cols_with_missing = df.columns[df.isnull().any()]
                for col in cols_with_missing:
                    df[col] = df[col].fillna(0)
                    filled_info[col] = 0

            elif method == "Manual Value" and manual_value:
                cols_with_missing = df.columns[df.isnull().any()]
                for col in cols_with_missing:
                    df[col] = df[col].fillna(manual_value)
                    filled_info[col] = manual_value

            if filled_info:
                st.success("Missing values cleaned successfully!")
                st.subheader("Cleaned Dataset Preview")
                st.dataframe(df)
                st.write("Remaining Missing Values:", df.isnull().sum().sum())

                cleaned_df = df.copy()  # 🔹 Save cleaned version

            else:
                st.warning("No columns required cleaning.")

    else:
        st.success("No missing values found in dataset.")
        cleaned_df = df.copy()  # 🔹 Already clean

    # =========================
    # Download Cleaned Dataset
    # =========================
    if cleaned_df is not None:
        csv_data = cleaned_df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇ Download Cleaned Dataset",
            data=csv_data,
            file_name="cleaned_dataset.csv",
            mime="text/csv"
        )

    # =========================
    # Summary Statistics
    # =========================
    st.subheader("Summary Statistics (Based on Original Uploaded Dataset)")
    st.caption("Note: These statistics are calculated from the original dataset before any missing value handling.")

    numeric_df = df.select_dtypes(include=["number"])
    categorical_df = df.select_dtypes(exclude=["number"])

    if not numeric_df.empty:
        st.markdown("### Numeric Columns Summary")
        st.dataframe(numeric_df.describe())

    if not categorical_df.empty:
        st.markdown("### Categorical Columns Summary")

        cat_summary = pd.DataFrame({
            "Unique Values": categorical_df.nunique(),
            "Most Frequent": categorical_df.mode().iloc[0],
            "Frequency": categorical_df.apply(lambda x: x.value_counts().iloc[0])
        })

        st.dataframe(cat_summary)

    # =========================
    # Basic Data Overview
    # =========================
    st.subheader("Basic Data Overview")

    rows, cols = df.shape
    total_missing = df.isnull().sum().sum()

    st.write(f"The dataset contains {rows} rows and {cols} columns.")

    if total_missing == 0:
        st.write("There are no missing values in the dataset.")
    else:
        st.write(f"The dataset contains {total_missing} missing values.")

    st.write("The above statistics provide a basic understanding of the dataset structure and data quality.")

else:
    st.info("Please upload a file to continue.")

st.markdown("""
<hr>
<div style="text-align:center; color:gray;">
© 2026 Data Xtraction & Analysis System | TYBSc Computer Science Project
</div>
""", unsafe_allow_html=True)
