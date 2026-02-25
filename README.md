# 🏛️ FIN-AI: Strategic Banking Auditor & Risk Engine

**FIN-AI** is a high-performance financial intelligence suite built to automate the role of a Junior Forensic Accountant. It bridges the gap between structured ledger data (Excel/CSV) and unstructured policy documentation (PDF/TXT) using a Retrieval-Augmented Generation (RAG) architecture.



## 🌟 Core Value Proposition
In traditional banking, auditors spend 70% of their time finding errors and only 30% analyzing them. **FIN-AI flips this ratio.** It uses statistical anomaly detection to find "The Needle in the Haystack" instantly, allowing human experts to focus on strategy.

---

## 🛠️ Key Capabilities

### 1. Statistical Fraud Detection (The "Forensic" Engine)
Uses **Z-Score analysis** to scan thousands of transactions. It identifies outliers that deviate from the mean by more than 2 standard deviations—flagging potential embezzlement, double-billing, or clerical errors.

### 2. Multi-Modal Contextual Analysis (RAG)
Unlike a standard chatbot, this system "reads" your internal policy memos (PDFs/TXT). When it finds a financial anomaly, it checks the documentation to see if that spend was pre-authorized.

### 3. Scenario "Stress Testing"
Includes a real-time **What-If Simulator**. Decision-makers can adjust global budget parameters via a slider and see the instant impact on the organization's **Risk Score (0-100)**.

### 4. Right-Side Strategic Co-pilot
A persistent AI window that maintains context of the current session, allowing for deep-dive "Forensic Conversations" without losing sight of the data visualizations.

---

## 🏗️ Technical Architecture

The system is built on a three-tier logic stack:
1. **Data Layer:** Pandas & NumPy for deterministic math.
2. **Inference Layer:** Groq (Llama 3.3-70B) for high-speed reasoning.
3. **UX Layer:** Streamlit with custom CSS for a premium FinTech experience.



---

## 🚦 Getting Started

### Prerequisites
- Python 3.9+
- A Groq API Key ([Get one here](https://console.groq.com/))

### Installation
1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/fin-ai-auditor.git](https://github.com/YOUR_USERNAME/fin-ai-auditor.git)
   cd fin-ai-auditor