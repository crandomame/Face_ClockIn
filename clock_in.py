import streamlit as st
import os
import cv2
import numpy as np
from face_compare import run
from datetime import datetime
from database import execute_sql
from setting import SparkApi_config


def clock_in(key):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    col1, col2 = st.columns(2)

    with col1:
        st.write("员工编号")
        st.markdown('<br>', unsafe_allow_html=True)
        picture = st.camera_input(
            "拍照打卡",
            label_visibility='collapsed',
        )

    with col2:
        employeeid = st.text_input(
            "打卡员工编号", value=None,
            placeholder="请输入您的员工编号",
            label_visibility='collapsed',
        )

    if picture:
        with col2:
            st.image(picture)
        bytes_data = picture.getvalue()
        cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

        if st.button("确认打卡", type="primary"):
            save_path = os.path.join("temp", f"clockin_{employeeid}.jpg")
            cv2.imwrite(save_path, cv2_img)

            name = execute_sql(f"SELECT name FROM employee WHERE id = {employeeid};")
            print(name[0][0])

            if not name:
                st.write("没有查询到此ID，请检查后重新打卡！")
                return

            ret = -1

            ret, score = run(
                appid=SparkApi_config['appid'],
                apisecret=SparkApi_config['apisecret'],
                apikey=SparkApi_config['apikey'],
                img1_path=os.path.join("face", "employee_{}.jpg".format(employeeid)),
                img2_path=save_path,
            )

            if os.path.exists(save_path):
                os.remove(save_path)

            issuccessful = (True if ret == 0 and score > 0.67 else False)

            if issuccessful:
                st.write("恭喜您，打卡成功！")
            else:
                st.write("很遗憾，打卡失败！")

            execute_sql("INSERT INTO history "
                        "(time, id, similarity, name, issuccessful) "
                        f"VALUES ('{current_time}', '{employeeid}', {score}, '{name[0][0]}', {issuccessful});")

    st.write(f"当前时间： {current_time}")

    st.markdown(
        "<div style='text-align: center; color: gray; position: fixed; bottom: 0; width: 50%;'>powered by streamlit</div>",
        unsafe_allow_html=True)
