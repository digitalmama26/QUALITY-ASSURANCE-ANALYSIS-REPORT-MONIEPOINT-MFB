import streamlit as st
import pandas as pd
import plotly.express as px

# Professional Page Config
st.set_page_config(page_title="Moniepoint QA Audit", page_icon="🛡️", layout="wide")

# Sidebar for Navigation
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Globe_icon.svg/2048px-Globe_icon.svg.png", width=50)
st.sidebar.title("QA Intelligence Hub")
page = st.sidebar.radio("Navigate", ["Executive Summary", "Defect Explorer", "Technical Roadmap"])

# Load your data
df = pd.read_csv("defects.csv")

if page == "Executive Summary":
    st.title("🛡️ Software Quality Assurance Report: Moniepoint MFB")
    st.markdown("### Pillar: Financial Inclusion")
    
    # Big Metrics (from your slides)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Overall Pass Rate", "4%", "-96%")
    col2.metric("Critical Defects", "9", delta_color="inverse")
    col3.metric("Test Cases", "26")
    col4.metric("Risk Level", "UNACCEPTABLE", delta_color="normal")

    # Interactive Chart
    st.write("### Defect Severity Distribution")
    fig = px.pie(df, names='Severity', color='Severity', 
                 color_discrete_map={'Critical':'red', 'High':'orange', 'Medium':'yellow'})
    st.plotly_chart(fig)

elif page == "Defect Explorer":
    st.title("🐞 Interactive Defect Log")
    st.write("Filter through the 13 identified defects to understand architectural risks.")
    
    severity_filter = st.multiselect("Filter by Severity", options=["Critical", "High", "Medium"], default=["Critical", "High"])
    filtered_df = df[df['Severity'].isin(severity_filter)]
    st.table(filtered_df)

elif page == "Technical Roadmap":
    st.title("🚀 Engineering Recovery Roadmap")
    st.info("Strategy: Fix architectural bottlenecks to restore customer trust.")
    
    st.markdown("""
    - **Week 1 (Immediate):** SMS OTP Fallback & Offline Crash Fixes.
    - **Weeks 2-4 (P0):** Deploy Idempotency Engine & Reversal Logic.
    - **Weeks 5-12 (P1/P2):** Migrate to Saga Pattern & Kafka Event Bus.
    """)
    st.progress(4) # Shows only 4% complete
