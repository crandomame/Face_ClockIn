import streamlit as st
import pandas as pd
from database import execute_sql


def history(key):
    st.title("打卡记录")
    result = execute_sql("SELECT * FROM history;")

    data = pd.DataFrame(result, columns=['打卡时间', '员工编号', '员工姓名', '相似度', '是否打卡成功'])

    data.columns = ['打卡时间', '员工编号', '员工姓名', '相似度', '是否打卡成功']

    data['相似度'] = data['相似度'].apply(lambda x: format(x, '.2f'))

    st.dataframe(
        data=data.style.set_properties(**{'background-color': '#8bd2ff', 'color': 'black', 'border-color': 'black'}),
        hide_index=True,
        use_container_width=True,
    )

    st.markdown(
        "<div style='text-align: center; color: gray; position: fixed; bottom: 0; width: 50%;'>powered by streamlit</div>",
        unsafe_allow_html=True)
