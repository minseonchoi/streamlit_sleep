import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from PIL import Image


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
        st.text('374개의 데이터 중 5개만 보입니다.')
    elif choice_radio == radio_menu[1]:
        st.dataframe(df.describe())

    st.write(' ')
    st.write(' ')
    st.write(' ')
    
    st.write('##### 현대인의 수면장애 비율 _ 파이 차트')

    col1, col2 = st.columns(2)

    with col2:
        # 파이 차트 그리기
        st.text('수면 장애의 종류는 80여 가지 이상으로 매우 다양하다.')
        st.text('비율을 구하기 위해서 대표적인 예인 불면증과 무호흡증으로 알아보았다.')
        
        df2 = df['수면 장애'].value_counts()
        import platform

        from matplotlib import font_manager, rc
        plt.rcParams['axes.unicode_minus'] = False

        if platform.system() == 'Darwin':
            rc('font', family='AppleGothic')
        elif platform.system() == 'Windows':
            path = "c:/Windows/Fonts/malgun.ttf"
            font_name = font_manager.FontProperties(fname=path).get_name()
            rc('font', family=font_name)
        else:
            print('Unknown system... sorry~~~~')

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
    st.text('일상생활과 건강의 데이터와 수면 장애의 관련성을 눈으로 확인할 수 있습니다.')
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
    choice_column = st.selectbox('보고싶은 열을 선택하세요. 숫자 데이터만 확인 가능합니다.', column_list)
    
    print(choice_column)
    
    fig2 = plt.figure()
    plt.hist2d(data=df, x='수면 장애', y= str(choice_column), cmin= 0.5, cmap = 'viridis_r', bins= 20)
    plt.xticks([0, 1, 2])
    plt.colorbar()
    plt.title(f'수면 상태와 {str(choice_column)} 의 관계')
    plt.xlabel('0 = 무호흡,   1 = 불면증,   2 = 정상')
    plt.ylabel(f'{str(choice_column)}')
    st.pyplot(fig2)
        







