import streamlit as st

def run_ml() :
    st.subheader('일상생활에 따른 수면 상태 예측')

    # 1. 예측하기 위해서 유저한테 입력 받는다
    # '성별','나이','수면 시간','수면의 질(등급:1-10)','신체 활동수준(분/일)','스트레스 수준',
    # 'BMI 범주','심박수(BPM)','일일 걸음 수','혈압(수축기)','혈압(이완기)'

    st.write('#### 나의 정보를 통해 수면 상태 예측을 할 수 있습니다.')

    st.write('###### 정보 입력하기')
    # Gender
    st.write('- 성별을 선택하세요.')
    gender = st.radio('성별 선택', ['남자', '여자'])
    st.info('성별은 ' + gender + ' 입니다.')
    if gender == '남자':
        gender = 0
    elif gender == '여자':
        gender = 1
    
    
    st.write('  ')

    # 나이
    st.write('- 나이를 입력하세요.')
    age = st.number_input( '나이 입력', min_value=1, max_value=100, value=30)
    st.info('나이는 ' + str(age) + '살 입니다.')

    st.write('  ')

    # 총 수면 시간
    st.write('- 수면 시간을 입력하세요.')
    sleep_time = st.number_input( '수면 시간 입력. (시간 단위로 입력)',  min_value=0, max_value=24, value=0, step=1)
    st.info('총 잠자는 시간은 ' + str(sleep_time)+'시간 입니다.')

    st.write('  ')

    # 수면의 질(등급:1-10)
    st.write('- 수면의 질을 평가해주세요.')
    num_sleep = st.slider('수면의 질 등급 1 ~ 10 (나쁨 ~ 좋음)', 1, 10, step=1 )
    st.info('수면의 질 등급은 ' + str(num_sleep)+' 입니다.')

    st.write('  ')

    # 신체 활동수준(분/일)
    st.write('- 하루에 운동하는 시간을 입력하세요.')
    activity = st.number_input( '활동 시간 입력. (분 단위로 입력)',  min_value=0, max_value=1440, value=5, step=10)
    st.info('하루에 운동하는 시간은 ' + str(activity)+'분 입니다.')

    st.write('  ')

    # 스트레스 수준
    st.write('- 스트레스의 정도를 평가해주세요.')
    stress = st.slider('스트레스 정도 등급 1 ~ 10 (좋음 ~ 나쁨)', 1, 10, step=3 )
    st.info('스트레스 등급은 ' + str(stress)+' 입니다.')

    st.write('  ')

    # BMI 범주
    st.write('- 체중의 정도를 선택해주세요.')
    BMI = ['정상','과체중','비만','저체중']
    sel_bmi = st.selectbox('BMI 범주로 나눈 체중의 정도', BMI , index=None )
    st.info('BMI 정보는 ' + str(sel_bmi)+' 입니다.')

    # 심박수(BPM)
    st.write('- 평균 심박수(BPM)를 입력 해주세요.')
    bpm = st.number_input( '평균 심박수 입력',  min_value=0, max_value=2000, value=70, step=1)
    st.info('평균 심박수는 ' + str(bpm)+' BPM 입니다.')  

    # 일일 걸음 수 
    st.write('- 일일 걸음 수를 입력해주세요.')
    steps = st.number_input( '일일 걸음 수 입력',  min_value=0, max_value=100000, value=7000, step=100)
    st.info('일일 걸음 수는 ' + str(steps)+' 입니다.')  

    # 혈압(수축기)
    st.write('- 혈압의 수축기 숫자를 입력해주세요.')
    systolic = st.number_input( '혈압(수축기) 수 입력',  min_value=0, max_value=250, value=125, step=10)
    st.info('혈압(수축기) 수는 ' + str(systolic)+' 입니다.') 

    # 혈압(이완기)
    st.write('- 협압의 이완기 숫자를 입력해주세요.')
    diastolic = st.number_input( '혈압(이완기) 수 입력',  min_value=0, max_value=150, value=85, step=10)
    st.info('혈압(이완기) 수는 ' + str(diastolic)+' 입니다.') 

    
