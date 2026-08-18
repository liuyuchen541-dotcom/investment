import streamlit as st


pages = [
    st.Page("pages/1_总览.py", title="总览"),
    st.Page("pages/2_基金观察.py", title="基金观察"),
    st.Page("pages/3_股票指数观察.py", title="股票指数观察"),
    st.Page("pages/4_持仓页.py", title="持仓页"),
    st.Page("pages/5_更新日志.py", title="更新日志"),
]

navigation = st.navigation(pages)
navigation.run()
