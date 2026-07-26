import streamlit as st

st.set_page_config(page_title="Personal KB Agent", page_icon="🧠")
st.title("Personal KB Agent")

prompt = st.text_area("Ask a question about your documents")
if st.button("Send"):
    st.write(f"You asked: {prompt}")
