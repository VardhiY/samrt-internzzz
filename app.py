# frontend/SmartSDLC.py

import streamlit as st
import requests

st.set_page_config(page_title="SmartSDLC", layout="wide")
st.title("🤖 SmartSDLC: AI-Powered Software Assistant")

menu = ["Requirement Extractor", "Code Generator", "Bug Fixer", "Test Generator", "Code Summarizer"]
option = st.sidebar.selectbox("Choose Feature", menu)

BASE_URL = "http://localhost:8000"

# ---------- 1. Requirement Extractor ----------
if option == "Requirement Extractor":
    st.subheader("📄 Upload Project PDF")
    uploaded_file = st.file_uploader("Upload your project document (PDF)", type=["pdf"])

    if uploaded_file is not None:
        files = {"file": uploaded_file.getvalue()}
        res = requests.post(f"{BASE_URL}/upload-pdf/", files={"file": (uploaded_file.name, uploaded_file, "application/pdf")})
        if res.status_code == 200:
            st.text_area("📋 Extracted Requirements", res.json()["extracted_text"], height=300)
        else:
            st.error("❌ Failed to extract requirements.")

# ---------- 2. Code Generator ----------
elif option == "Code Generator":
    st.subheader("🧠 AI Code Generator")
    prompt = st.text_area("Enter your prompt to generate code:")

    if st.button("Generate Code"):
        if prompt.strip():
            res = requests.post(f"{BASE_URL}/generate-code/", json={"prompt": prompt})
            if res.status_code == 200:
                st.code(res.json()["generated_code"], language="python")
            else:
                st.error("❌ Failed to generate code.")
        else:
            st.warning("Please enter a prompt.")

# ---------- 3. Bug Fixer ----------
elif option == "Bug Fixer":
    st.subheader("🔧 Bug Fixer")
    user_code = st.text_area("Paste buggy Python code here:")

    if st.button("Fix Bugs"):
        if user_code.strip():
            res = requests.post(f"{BASE_URL}/fix-bugs/", json={"prompt": user_code})
            if res.status_code == 200:
                st.code(res.json()["fixed_code"], language="python")
            else:
                st.error("❌ Failed to fix bugs.")
        else:
            st.warning("Please enter some code.")

# ---------- 4. Test Generator ----------
elif option == "Test Generator":
    st.subheader("🧪 Test Case Generator")
    input_code = st.text_area("Paste the code you want test cases for:")

    if st.button("Generate Tests"):
        if input_code.strip():
            res = requests.post(f"{BASE_URL}/generate-tests/", json={"prompt": input_code})
            if res.status_code == 200:
                st.code(res.json()["test_cases"], language="python")
            else:
                st.error("❌ Failed to generate test cases.")
        else:
            st.warning("Please enter your code.")

# ---------- 5. Code Summarizer ----------
elif option == "Code Summarizer":
    st.subheader("📄 Code Summarizer")
    summary_code = st.text_area("Paste code to get a summary:")

    if st.button("Summarize Code"):
        if summary_code.strip():
            res = requests.post(f"{BASE_URL}/summarize-code/", json={"prompt": summary_code})
            if res.status_code == 200:
                st.success(res.json()["summary"])
            else:
                st.error("❌ Failed to summarize code.")
        else:
            st.warning("Please enter code to summarize.")
