import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pypdf import PdfReader
from researcher import ResearchAgent

# --- CONFIGURATION ---
GROQ_API_KEY = st.secrets["GROQ_API_KEY"]

st.set_page_config(page_title="FIN-AI COMMAND", layout="wide")

# --- INITIALIZE SESSION STATE ---
if "messages" not in st.session_state: st.session_state.messages = []
if "report_context" not in st.session_state: st.session_state.report_context = ""
if "actuals_df" not in st.session_state: st.session_state.actuals_df = None
if "adj_pct" not in st.session_state: st.session_state.adj_pct = 0

# --- HELPERS ---
def extract_pdf_text(uploaded_file):
    reader = PdfReader(uploaded_file)
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

def detect_anomalies(df, column):
    data = df[column]
    if len(data) < 2: return pd.DataFrame()
    mean, std = np.mean(data), np.std(data)
    if std == 0: return pd.DataFrame()
    z_scores = [(y - mean) / std for y in data]
    return df[np.abs(z_scores) > 2]

# --- MAIN LAYOUT ---
# We split the screen: 70% for Dashboard, 30% for the Right-Side Advisor
col_main, col_advisor = st.columns([0.7, 0.3], gap="large")

# --- LEFT COLUMN: DASHBOARD & CONTROLS ---
with col_main:
    st.title("🏛️ Banking Command Center")
    
    # Ingestion Controls
    with st.expander("📁 Data Ingestion & Settings", expanded=True):
        c1, c2 = st.columns(2)
        with c1:
            uploaded_file = st.file_uploader("Upload Ledger/Memos", type=["csv", "xlsx", "pdf", "txt"])
        with c2:
            st.session_state.adj_pct = st.slider("Budget Stress Test (%)", -50, 50, st.session_state.adj_pct)

    if uploaded_file:
        if uploaded_file.name.endswith(('.txt', '.pdf')):
            content = extract_pdf_text(uploaded_file) if uploaded_file.name.endswith('.pdf') else uploaded_file.read().decode("utf-8")
            st.session_state.report_context = content
        elif st.session_state.actuals_df is None:
            df_raw = pd.read_excel(uploaded_file) if uploaded_file.name.endswith('.xlsx') else pd.read_csv(uploaded_file)
            st.session_state.actuals_df = df_raw 

    if st.session_state.actuals_df is not None:
        df = st.session_state.actuals_df
        anoms = detect_anomalies(df, 'actual_amount')
        
        # KPI Bar
        k1, k2, k3 = st.columns(3)
        k1.metric("Total Spend", f"${df['actual_amount'].sum():,.0f}")
        k2.metric("Anomalies", len(anoms))
        k3.metric("Risk Level", "HIGH" if len(anoms) > 0 else "NORMAL")

        tab1, tab2 = st.tabs(["📊 Analytics", "🚨 Forensic Watch"])
        with tab1:
            df['sim'] = df['budget_amount'] * (1 + st.session_state.adj_pct/100)
            st.plotly_chart(px.bar(df, x="category", y=["actual_amount", "budget_amount", "sim"], 
                                   barmode="group", template="plotly_white"), use_container_width=True)
            st.dataframe(df, use_container_width=True, hide_index=True)
        with tab2:
            if not anoms.empty:
                st.error("🚨 POTENTIAL FRAUDULENT ACTIVITY")
                st.table(anoms)
            else:
                st.success("✅ Statistical integrity confirmed.")
    else:
        st.info("💡 Upload data to begin analysis.")

# --- RIGHT COLUMN: FLOATING ADVISOR WINDOW ---
with col_advisor:
    st.subheader("💬 AI Strategy Advisor")
    st.markdown("---")
    
    # Create a scrollable container for the chat history
    chat_box = st.container(height=550)
    
    with chat_box:
        for m in st.session_state.messages:
            with st.chat_message(m["role"]): st.markdown(m["content"])
    
    # Chat input placed directly below the history box
    if p := st.chat_input("Ask the Advisor..."):
        st.session_state.messages.append({"role": "user", "content": p})
        with chat_box.chat_message("user"): st.markdown(p)
        
        # AI Logic
        researcher = ResearchAgent(api_key=GROQ_API_KEY)
        context = f"Data: {st.session_state.actuals_df.to_string() if st.session_state.actuals_df is not None else 'No data'}\nDocs: {st.session_state.report_context}"
        res = researcher.llm.invoke(f"Context: {context}\n\nQ: {p}").content
        
        st.session_state.messages.append({"role": "assistant", "content": res})
        with chat_box.chat_message("assistant"): st.markdown(res)

    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()