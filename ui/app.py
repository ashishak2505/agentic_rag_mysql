import streamlit as st
import requests

st.title("Federal Register RAG Agent")

query = st.text_input("Ask about federal documents")

if query:
    try:
        res = requests.post(
            "http://127.0.0.1:8000/chat",
            json={"query": query},
            timeout=30
        )

        # ✅ Always show status
        st.caption(f"HTTP {res.status_code}")

        # ✅ Check content type FIRST
        content_type = res.headers.get("content-type", "")

        if "application/json" in content_type:
            data = res.json()
            st.success(data.get("response", "No response field"))
        else:
            st.error("Backend did not return JSON")
            st.code(res.text)

    except requests.exceptions.RequestException as e:
        st.error(f"Request failed: {e}")
