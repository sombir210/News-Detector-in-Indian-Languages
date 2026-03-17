import streamlit as st
from logic import verify_news_with_gemini

st.set_page_config(page_title="News Checker", page_icon="🕵️")

st.title("News Checker")
st.caption("Fake News Detector for indian languages")

news_input = st.text_area("Paste news here:", height=150)

if st.button("Check Veracity", type="primary"):
    if not news_input:
        st.warning("Please paste some text first.")
    else:
        with st.spinner("Searching the web & verifying..."):
            
            verdict, sources = verify_news_with_gemini(news_input)
            
            st.success("Analysis Complete")
            st.markdown(verdict)
            
            with st.expander("View Raw Search Sources"):
                if sources:
                    for s in sources:
                        st.text(s)
                else:
                    st.write("No web sources found.")