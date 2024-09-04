import streamlit as st
from streamlit_option_menu import option_menu
import os
from main_mean import main_menu
from new_user import new_user
from clock_in import clock_in
from history import history

if "is_init" not in st.session_state:
    st.session_state.is_init = True

if __name__ == "__main__":

    # 侧栏
    with st.sidebar:
        st.image(
            os.path.join("image", "logo.png"),
            use_column_width=True
        )
        st.caption(
            f"""<p align="right">当前版本：v0.1.0</p>""",
            unsafe_allow_html=True,
        )

        # 添加空行作为间距
        st.markdown('<br>', unsafe_allow_html=True)

        pages = {
            "新建用户": {
                "icon": "person",
                "func": new_user,
            },
            "考勤打卡": {
                "icon": "person-workspace",
                "func": clock_in,
            },
            "打卡记录": {
                "icon": "clock-history",
                "func": history,
            },
        }

        options = list(pages)
        icons = [x["icon"] for x in pages.values()]

        default_index = 0

        selected_page = option_menu(
            menu_title="",
            # menu_icon="cast",
            options=options,
            icons=icons,
            default_index=-1,
            styles={
                # "icon": {"color": "blue"},
                "nav-link-selected": {"background-color": "blue"},
            },
        )

    if (selected_page in pages) and st.session_state.is_init is False:
        pages[selected_page]["func"](default_index)

    if st.session_state.is_init:
        main_menu(0)
        st.session_state.is_init = False
