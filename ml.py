import streamlit as st
import joblib
import numpy as np
import pandas as pd
from PIL import Image


def run_ml() :
    st.subheader('일상생활에 따른 수면 상태 예측')

    # 1. 예측하기 위해서 유저한테 입력 받는다
    # '성별','나이','수면 시간','수면의 질(등급:1-10)','신체 활동수준(분/일)','스트레스 수준',
    # 'BMI 범주','심박수(BPM)','일일 걸음 수','혈압(수축기)','혈압(이완기)'

    st.write('#### 나의 정보를 통해 수면 상태 예측을 할 수 있습니다.')

    st.write('###### 정보 입력하기')
    
    # 성별
    st.write('- 성별을 선택하세요.')
    gender = st.radio('성별 선택', ['남자', '여자'])
    st.info('성별은 ' + gender + ' 입니다.')
    if gender == '남자':
        gender = 0
    elif gender == '여자':
        gender = 1
    print(gender)
    
    st.write('  ')

    # 나이
    st.write('- 나이를 입력하세요.')
    age = st.number_input( '나이 입력', min_value=1, max_value=100, value=30)
    st.info('나이는 ' + str(age) + '살 입니다.')
    print(age)

    st.write('  ')

    # 총 수면 시간
    st.write('- 수면 시간을 입력하세요.')
    sleep_time = st.number_input( '수면 시간 입력. (시간 단위로 입력)',  min_value=0, max_value=24, value=6, step=1)
    st.info('총 잠자는 시간은 ' + str(sleep_time)+'시간 입니다.')
    print(sleep_time)

    st.write('  ')

    # 수면의 질(등급:1-10)
    st.write('- 수면의 질을 평가해주세요.')
    num_sleep = st.slider('수면의 질 등급 1 ~ 10 (나쁨 ~ 좋음)', 1, 10, step=1 )
    st.info('수면의 질 등급은 ' + str(num_sleep)+' 입니다.')
    print(num_sleep)

    st.write('  ')

    # 신체 활동수준(분/일)
    st.write('- 하루에 운동하는 시간을 입력하세요.')
    activity = st.number_input( '활동 시간 입력. (분 단위로 입력)',  min_value=0, max_value=1440, value=30, step=10)
    st.info('하루에 운동하는 시간은 ' + str(activity)+'분 입니다.')
    print(activity)

    st.write('  ')

    # 스트레스 수준
    st.write('- 스트레스의 정도를 평가해주세요.')
    stress = st.slider('스트레스 정도 등급 1 ~ 10 (좋음 ~ 나쁨)', 1, 10, step=1 )
    st.info('스트레스 등급은 ' + str(stress)+' 입니다.')
    print(stress)

    st.write('  ')

    # BMI 범주
    st.write('- 체중과 키를 적어 BMI 를 구합니다.')
    wegit = st.text_input('체중을 입력하세요(kg)', value=1.0)
    tall = st.text_input('키를 입력하세요(cm)', value=1.0)
    wegit = float(wegit)
    tall = float(tall)
    tall = tall/100
    bmi_sum = round( wegit / ( tall ** 2 ), 2 )
    bmi = ''
    if  bmi_sum >= 25.00 :
        bmi = '비만'
    elif bmi_sum >= 23.00 :
        bmi = '과체중'
    elif bmi_sum >= 18.50 :
        bmi = '정상'
    else :
        bmi = '저체중'
    
    st.write('> 체질량 지수 표 ')
    img = Image.open('./image/bmi.png')
    st.image(img, use_column_width=True)

    st.info('BMI 계산 결과는 ' + str(bmi_sum) + ' 로 ' + str(bmi) + ' 입니다.')
    print(bmi)

    st.write('  ')

    # 심박수(BPM)
    st.write('- 평균 심박수(BPM)를 입력 해주세요.')
    bpm = st.number_input( '평균 심박수 입력',  min_value=0, max_value=2000, value=70, step=10)
    st.info('평균 심박수는 ' + str(bpm)+' BPM 입니다.')  
    print(bpm)

    st.write('  ')

    # 일일 걸음 수 
    st.write('- 일일 걸음 수를 입력해주세요.')
    steps = st.number_input( '일일 걸음 수 입력',  min_value=0, max_value=100000, value=7000, step=100)
    st.info('일일 걸음 수는 ' + str(steps)+' 입니다.')  
    print(steps)

    st.write('  ')

    # 혈압(수축기)
    st.write('- 혈압의 수축기 숫자를 입력해주세요.')
    systolic = st.number_input( '혈압(수축기) 수 입력',  min_value=0, max_value=250, value=125, step=10)
    st.info('혈압(수축기) 수는 ' + str(systolic)+' 입니다.') 
    print(systolic)

    st.write('  ')

    # 혈압(이완기)
    st.write('- 협압의 이완기 숫자를 입력해주세요.')
    diastolic = st.number_input( '혈압(이완기) 수 입력',  min_value=0, max_value=150, value=85, step=10)
    st.info('혈압(이완기) 수는 ' + str(diastolic)+' 입니다.') 
    print(diastolic)

    st.write('  ')
    st.write('  ')
    st.write('  ')

    # 버튼 만들기
    st.write('##### 버튼을 누르면 입력하신 데이터를 통해 예상 수면상태를 예측합니다.')


    if st.button('나의 수면 상태 예측하기') :
        # 예측하기
        # 모델 데려오기
        model = joblib.load('./model/model_ovr.pkl')
        ct = joblib.load('./model/ct.pkl')

        # 입력 데이터 , 모델이 예측할 수 있는 데이터로 가공하기
        new_data2 = pd.DataFrame({'성별':[gender],
                                  '나이':[age],
                                  '수면 시간':[sleep_time],
                                  '수면의 질(등급:1-10)':[num_sleep],
                                  '신체 활동수준(분/일)':[activity],
                                  '스트레스 수준': [stress],
                                  'BMI 범주':[bmi],
                                  '심박수(BPM)':[bpm],
                                  '일일 걸음 수':[steps],
                                  '혈압(수축기)':[systolic],
                                  '혈압(이완기)':[diastolic]})
        print(new_data2)
        
        new_data2 = ct.transform(new_data2)
        data_pred = model.predict(new_data2)

        print(data_pred)

        # 리스트에서 꺼내고 한글로 변환하기
        data_pred = data_pred[0]

        if data_pred == 0 :
            st.write('###### 예상 수면 상태는 무호흡증 입니다. 나의 수면 상태를 확인하고 신경 써 주세요.')
        elif data_pred == 1 :
            st.write('###### 예상 수면 상태는 불면증 입니다. 나의 수면 상태를 확인하고 신경 써 주세요.')
        elif data_pred == 2 :
            st.write('###### 예상 수면 상태는 정상 입니다. 좋은 수면 상태를 가지고 계시나요?')
   



    
