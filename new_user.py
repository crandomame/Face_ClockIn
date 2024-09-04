import streamlit as st
import os
import cv2
import numpy as np
from database import execute_sql


def new_user(key):
    col1, col2 = st.columns(2)
    with col1:
        st.write("员工编号")
        st.write("员工姓名")

        st.markdown('<br>', unsafe_allow_html=True)
        picture = st.camera_input(
            "录入人像",
            label_visibility='collapsed',
        )

    with col2:
        employeeid = st.text_input(
            "新建员工编号", value=None,
            placeholder="请输入您的员工编号",
            label_visibility='collapsed',
        )

        name = st.text_input(
            "员工姓名", value=None,
            placeholder="请输入您的姓名",
            label_visibility='collapsed')

        if picture:
            st.image(picture)
            bytes_data = picture.getvalue()
            cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
            if st.button("确认提交", type="primary"):
                save_path = os.path.join("face", "employee_{}.jpg".format(employeeid))
                cv2.imwrite(save_path, cv2_img)
                execute_sql(
                    f"INSERT INTO employee (id, name, imagepath) VALUES ('{employeeid}', '{name}', '{save_path}');")

    st.markdown(
        "<div style='text-align: center; color: gray; position: fixed; bottom: 0; width: 50%;'>powered by streamlit</div>",
        unsafe_allow_html=True)
