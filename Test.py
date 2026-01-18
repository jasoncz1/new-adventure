import streamlit as st
import pandas as pd

st.title("CSV Explorer & Formatter")

#1.Fileuploader Widget
uploaded_file=st.file_uploader("Choose a CSV file", type = "csv")

if uploaded_file is not None:
    #2. Load the data using Pandas
    df = pd.read_csv(uploaded_file)

    st.subheader("Data Preview")

    #3. Tweaking the format (The "Styler" API)
    #we use .style to modify how the data looks without changing the data itself
    styled_df = df.style.highlight_max(axis=0, color='lightgreen') \
    .highlight_min(axis=0,color='pink') \
    .format(precision=2)
    
    #4. Display the interactive table
    st.dataframe(styled_df, use_container_width = True)

    #5. Add some quick stats in the sidebar
    st.sidebar.header("File Statistics")
    st.sidebar.write(f"**Rows:** {df.shape[0]}")
    st.sidebar.write(f"**Columns:** {df.shape[1]}")
else:
    st.info("Please uplaod a csv file to get started.")
