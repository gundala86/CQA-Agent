
import streamlit as st
import pandas as pd

st.set_page_config(page_title="CMC KnowledgeBase Viewer", page_icon="📊", layout="wide")
st.title("📊 Current CMC KnowledgeBase")

kb_path = "output/CQA_KnowledgeBase_Master.csv"

try:
    df = pd.read_csv(kb_path)
    st.success(f"✅ KnowledgeBase loaded successfully. Total records: {len(df)}")
    st.dataframe(df, use_container_width=True)
    
    if st.checkbox("Download full KnowledgeBase as CSV"):
        st.download_button("Download CSV", df.to_csv(index=False), file_name="CQA_KnowledgeBase_Master.csv")
        
except Exception as e:
    st.error(f"Error loading knowledgebase: {str(e)}")
