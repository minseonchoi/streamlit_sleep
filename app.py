import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image

from home import run_home
from eda import run_eda
from ml import run_ml



def main():
    st.title('현대인의 수면 건강')

    menu = ['메인화면','생활과 수면의 관계','나의 수면 건강 확인하기']
    img_side = Image.open('./image/그림1.png')
    with st.sidebar :
        st.write('# 💤 수면 건강 예측하기 💤')
        st.image(img_side, use_column_width=True)
        choice = option_menu(' ', menu,
                             icons=['house','bi bi-clipboard2-data','bi bi-chat-heart'],
                             menu_icon='bi bi-list', default_index=0,
                             styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#fff"},
        "nav-link-selected": {"background-color": "#7588AF"}})
    
   
    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_eda()
    elif choice == menu[2] :
        run_ml()



if __name__ == '__main__' :
    main()
