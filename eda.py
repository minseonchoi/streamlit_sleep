import streamlit as st
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder

from PIL import Image

import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False
if platform.system() == 'Linux':
    plt.rcParams["font.family"] = 'NanumGothic'
    rc('font', family='NanumGothic')


def run_eda() :

    st.subheader('라이프 스타일과 수면의 연관성 분석')
    st.text('')

    st.write('##### 실생활에 따른 수면 데이터 확인하기')
    
    df = pd.read_csv('./data/k_df.csv', index_col='Person ID')
    print(df.head())

    radio_menu = ['데이터 표','데이터를 요약한 수치 데이터']
    
    choice_radio = st.radio('항목을 선택하세요.', radio_menu)

    if choice_radio == radio_menu[0]:
        st.dataframe(df.head())
        st.write('374개의 데이터 중 5개만 보입니다.')
    elif choice_radio == radio_menu[1]:
        st.dataframe(df.describe())

    st.write(' ')
    st.write(' ')
    st.write(' ')
    
    st.write('##### 현대인의 수면장애 비율 _ 파이 차트')

    col1, col2 = st.columns(2)

    with col2:
        # 파이 차트 그리기
        st.write("""> 수면 장애의 대표적인 두가지인, 
                 불면증과 무호흡증의 비율을 
                 파이 차트를 통해 확인 할 수 있습니다.""")
        
        df2 = df['수면 장애'].value_counts()

        fig1 = plt.figure()
        plt.pie(df2, labels= df2.index, autopct= '%.1f%%', startangle=90, wedgeprops={'width':0.7}) 
        plt.title('현대인의 수면 건강')
        plt.legend() 
        st.pyplot(fig1)

    with col1:
        img2 = Image.open('./image/sleep.png')
        st.image(img2, width=250)

    st.write(' ')
    st.write(' ')
    st.write(' ')

    # 선택하여 그래프 볼 수 있게 하기
    st.write('##### 수면 상태와 생활의 관계')
    st.write('박스플롯 차트(캔들 차트)로 일상생활의 건강 데이터와 수면 장애의 관련성을 눈으로 확인 할 수 있습니다.')
    st.write('''> 박스플롯 차트 보는 법 : 사분 범위(네모난 상자)를 중점으로 확인하며,
            사분범위는 중앙값(Median)을 기준으로 데이터들의 흩어진 정도 입니다.
            박스플롯 차트는 분포되는 데이터에서 이상치를 찾는데 효과적입니다.''')
    column_list = ['성별',
                    '나이',
                    '수면 시간',
                    '수면의 질(등급:1-10)',
                    '신체 활동수준(분/일)',
                    '스트레스 수준',
                    '심박수(BPM)',
                    '일일 걸음 수',
                    '혈압(수축기)',
                    '혈압(이완기)']
    
    # 문자열로 되어있는 데이터 레이블 인코딩하기
    encoder = LabelEncoder()
    df['성별'] = encoder.fit_transform(df['성별'])
    df['수면 장애'] = encoder.fit_transform(df['수면 장애'])
    
    # 표 그리기
    st.write('')
    st.write('')

    choice_column = st.selectbox('보고싶은 열을 선택하세요. 숫자 데이터만 확인 가능합니다.', column_list)
        
    print(choice_column)

    df_0 = df.loc[df['수면 장애'] == 0, ]
    df_1 = df.loc[df['수면 장애'] == 1, ]
    df_2 = df.loc[df['수면 장애'] == 2, ]

    fig2 = plt.figure(figsize=(12,8))

    plt.subplot(1, 3, 1) #(행, 열 , 순서 번째)
    bplot1 = plt.boxplot(df_0[choice_column], notch=True, patch_artist=True)
    plt.xticks(np.arange(1, 2), ['무호흡'])
    plt.ylabel(choice_column)

    plt.subplot(1, 3, 2)
    bplot2 = plt.boxplot(df_1[choice_column], notch=True, patch_artist=True)
    plt.xticks(np.arange(1, 2), ['불면증'])
    plt.ylabel(choice_column)

    plt.subplot(1, 3, 3) #(행, 열 , 순서 번째)
    bplot3 = plt.boxplot(df_2[choice_column], notch=True, patch_artist=True)
    plt.xticks(np.arange(1, 2), ['정상'])
    plt.ylabel(choice_column)

    colors = ['lightblue']
    for bplot in (bplot1, bplot2, bplot3):
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)
    st.pyplot(fig2)
        







