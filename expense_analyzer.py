# Cost Structure Pie Chart Analyzer
# Function: Allows for manual editing of costs, supports uploading of Excel files, and enables export of reports
# Relevant course knowledge: Variables, dictionaries, for loops, conditional judgments, pandas DataFrame, file reading and writing

import streamlit as st
import pandas as pd
import plotly.express as px
from io import BytesIO

# ----------------------------- page setup ---------------------------------
st.set_page_config(page_title="Cost Structure Analyzer", layout="wide")
st.title("Department Expense Structure Pie Chart Analyzer")
st.markdown("This tool enables accountants to visually analyze the proportion of various expenses. You can upload your own Excel file, or use the preset data provided below.")

# ----------------------------- 1. Define default expense data (dictionary) -----------------
default_expenses = {
    "labor cost": 50000,
    "material cost": 30000,
    "rent": 20000,
    "marketing costs": 15000,
    "others": 5000
}

# ----------------------------- 2. Initialize session_state (to store user modifications)----
if "expenses" not in st.session_state:
    st.session_state.expenses = default_expenses.copy()
if "data_source" not in st.session_state:
    st.session_state.data_source = "default"

# ----------------------------- 3. File upload area  ------------------
st.subheader("Upload cost data (optional)")
uploaded_file = st.file_uploader("Upload the Excel file（.xlsx 或 .xls）", type=["xlsx", "xls"])

if uploaded_file is not None:
    try:
        # Use pandas to read Excel
        df_upload = pd.read_excel(uploaded_file)
        # Suppose Excel has two columns: the first column represents the expense category, and the second column shows the amount.
        if df_upload.shape[1] >= 2:
            # Convert the first two columns into a list, and then convert it into a dictionary
            expense_names = df_upload.iloc[:, 0].astype(str).tolist()
            expense_amounts = df_upload.iloc[:, 1].astype(float).tolist()
            uploaded_expenses = dict(zip(expense_names, expense_amounts))
            st.session_state.expenses = uploaded_expenses
            st.session_state.data_source = "upload"
            st.success(f"Successfully uploaded {len(uploaded_expenses)} expense items")
        else:
            st.error("The Excel file must have at least two columns: expense category and amount.")
    except Exception as e:
        st.error(f"Error occurred while reading the file: {e}")
else:
    if st.session_state.data_source != "upload":
        st.session_state.expenses = default_expenses.copy()
        st.session_state.data_source = "default"
    st.info("No file has been uploaded. Using default cost data. You can upload your own Excel file (with two columns: category, amount)")

# ----------------------------- 4. Editorial cost amount (using for loop) -----------
st.subheader("Edit Expense Amounts (double-click to modify)")
cols = st.columns(2)  # Display in two columns
expense_names = list(st.session_state.expenses.keys())

# Refer to Week 3 for the loop：for p in prices:
for i, name in enumerate(expense_names):
    with cols[i % 2]:
        st.session_state.expenses[name] = st.number_input(
            f"{name} (yuan)",
            value=float(st.session_state.expenses[name]),
            step=1000.0,
            key=f"input_{name}"
        )

# ----------------------------- 5. Convert to DataFrame and calculate the proportion ------------
# Reference Week 3: Convert Dictionary to DataFrame
df_expenses = pd.DataFrame({
    "Expense Category": list(st.session_state.expenses.keys()),
    "Amount (Yuan)": list(st.session_state.expenses.values())
})

total = df_expenses["Amount (Yuan)"].sum()
df_expenses["Proportion(%)"] = (df_expenses["Amount (Yuan)"] / total) * 100

# ----------------------------- 6. Display pie chart (plotly) ---------------------
st.subheader("Pie chart of cost structure")
fig = px.pie(df_expenses, values="Amount (Yuan)", names="Expense Category", title="Proportion of various expenses")
st.plotly_chart(fig, use_container_width=True)

# ----------------------------- 7. Display the detailed cost list (with formatting) --------------
st.subheader("statement of expenses")
styled_df = df_expenses.style.format({
    "Amount (Yuan)": "{:,.0f}",
    "Proportion(%)": "{:.1f}%"
})
st.dataframe(styled_df)
st.metric("Total cost", f"{total:,.0f} yuan")

# ----------------------------- 8. Export Excel report ---------------
# Refer to Week5 data.to_excel("aapl_sales.xlsx", index=False)
st.subheader("Export Report")
export_df = df_expenses.copy()
export_df["remark"] = ""

output = BytesIO()
with pd.ExcelWriter(output, engine='openpyxl') as writer:
    export_df.to_excel(writer, sheet_name="Expense Report", index=False)
    # Add an additional metadata worksheet
    meta_data = pd.DataFrame({
        "Project": ["Generation Time", "Total Cost"],
        "value": [pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S"), f"{total:,.0f}"]
    })
    meta_data.to_excel(writer, sheet_name="metadata", index=False)
output.seek(0)

st.download_button(
    label="Download Excel report",
    data=output,
    file_name="Cost Structure Report.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)

# ----------------------------- 9. Display information on data source explanation -----------------------
st.caption(f"Current data source: {'User uploaded' if st.session_state.data_source == 'upload' else 'Default preset'}")