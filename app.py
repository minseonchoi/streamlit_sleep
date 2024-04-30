import streamlit as st
from home import run_home
from eda import run_eda
from ml import run_ml



def main():
    st.title('현대인의 수면 건강')

    menu = ['HOME','생활과 수면','수면 건강 확인하기']
    choice = st.sidebar.selectbox('메뉴', menu)
   
    if choice == menu[0] :
        run_home()
    elif choice == menu[1] :
        run_eda()
    elif choice == menu[2] :
        run_ml()



if __name__ == '__main__' :
    main()
