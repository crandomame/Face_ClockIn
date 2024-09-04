import streamlit as st


def main_menu(key):
    st.markdown("<h1 style='text-align: center;'>欢迎使用Face Clock In</h1>", unsafe_allow_html=True)

    for i in range(3):
        st.markdown('<br>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("高精度识别", divider=True)
        st.write("利用讯飞星火API实现精准识别，结果更可靠")

    with col2:
        st.subheader("便捷式操作", divider=True)
        st.write("通过Streamlit的WebUI操作，用户体验流畅")

    with col3:
        st.subheader("数据安全防护", divider=True)
        st.write("使用OpenGauss存储，确保数据安全")

    st.markdown(
        "<div style='text-align: center; color: gray; position: fixed; bottom: 0; width: 50%;'>powered by streamlit</div>",
        unsafe_allow_html=True)
