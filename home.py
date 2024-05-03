import streamlit as st
from PIL import Image

def run_home() :
    st.subheader('현대인의 수면상태를 분석하고 나의 수면 상태를 예측합니다.')

    st.write(' ')

    st.link_button('데이터 출처', url='https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset')
    st.write("""데이터는 캐글에 있는 
             Sleep_health_and_lifestyle_dataset.csv 파일을 사용했습니다.""")


    img1 = Image.open('./image/pillows-820149_1280.jpg')
    st.image(img1, use_column_width=True)

    st.write("""
             #### 수면 장애란?
             수면의 양적, 질적인 장애를 의미합니다.\n
             수면 장애의 종류는 80여 가지 이상으로 매우 다양하며, 
             두 가지 이상의 수면 장애가 함께 나타나는 경우도 빈번합니다.
             그 대표적인 예로 잠을 이루지 못하는 불면증과 코골이와 수면 무호흡증을 비롯한 
             수면 호흡장애가 있습니다.\n
             국민건강보험공단에 따르면 
             지난 2020년 국내에서 수면 장애로 진료를 받은 환자는 약 67만 명입니다.
             지난 2016년 기준 수면 장애 환자 수는 50만명에 못미쳤지만, 
             이후 5년간 12만명 가량 늘어난 현재 추세로 보면 
             미래에는 70만명을 넘어설 것으로 예상됩니다.
             """)