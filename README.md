<img src="https://capsule-render.vercel.app/api?type=waving&color=85C8F8&height=150&section=header" />

# streamlit_sleep 

#### 수면장애 발생 여부를 예측하는 인공지능

#### 성별, 나이, 수면시간, 수면의 질, 신체 활동 수준, 스트레스 수준, BMI 범주, 혈압, 심박수, 일일 걸음 수가 수면에 미치는 영향을 보여주는 앱입니다.


[수면장애 발생 여부 예측 앱 URL : http://ec2-43-203-246-183.ap-northeast-2.compute.amazonaws.com:8501/](http://ec2-43-203-246-183.ap-northeast-2.compute.amazonaws.com:8501/)



✏️ 작업순서
-

데이터 주제 선정 ➡︎ 데이터 가공(주피터노트북) 
➡︎ Streamlit 프레임워크 웹 대시보드 개발 ➡︎ AWS EC2 배포




✏️ 데이터 가공
-

데이터 셋 : [Sleep Health and Lifestyle Dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)

수면 건강 및 라이프스타일 데이터세트는 수면 및 일상 습관과 관련된 변수를 다루는 400개의 행과 13개의 열로 구성되어 있습니다.

jupyter notebook 에서 데이터 한글 변환 및 정리했습니다.

1. 영어 데이터 한글로 변환 (한국인을 위한 앱이므로 데이터를 한국어로 변환합니다.)
   - 컬럼명 변환 
   - Nan 정리 : Sleep Disorder 컬럼에서 이상 없음을 'None' 이라고 적어둬서 '건강'으로 바꾸면서 영어로 되어 있는 밸류 유니크 값 3종류를 '불면증', '무호흡증'으로 변환
   - BMI Category 컬럼 밸류 유니크 값 4종류를 '저체중', '정상', '과체중', '비만'으로 변환
   - Gender 컬럼 밸류 유니크 값 2종류를 '남자', '여자'로 변환
   - Occupation(직업) 컬럼은 유니크 값이 너무 방대하여 한글로 변환하지 않았습니다.

2. 데이터 info() 확인하고 Object 컬럼 가공
   - Blood Pressure 컬럼은 숫자이지만 이완기랑 수축기 혈압이 같이 적혀있어 오브젝트로 되어 있음을 확인하였고, str.split()으로 나눠 이완기와 수축기 컬럼으로 저장하고 원래 컬럼은 drop() 했습니다.

3. 가공된 데이터 csv 형태로 data 폴더에 저장했습니다.(Visual Studio Code에서 가공한 데이터를 사용해서 웹 대시보드 개발했습니다.)





✏️ Streamlit 웹 대시보드 개발
-

파일명으로 정리했습니다.

✉︎ APP.PY
- 사이드바를 통해서 나의 웹 대시보드의 목록을 보여줍니다.
- 사이드바를 streamlit_option_menu 를 이용해서 업그레이드했습니다.

✉︎ HOME.PY
- 사용한 데이터 출처 표시했습니다.
- 데이터 출처 : [Sleep Health and Lifestyle Dataset](https://www.kaggle.com/datasets/uom190346a/sleep-health-and-lifestyle-dataset)
- 해당 앱과 관련되는 사진과 글을 넣어 웹 대시보드 메인 화면 만들었습니다.

✉︎ EDA.PY
- EC2 리눅스 컴퓨터에 한글 폰트를 설치하여 그래프에 글이 한글로 출력될 수 있도록 설정했습니다.
- 해당 데이터의 데이터프레임과 통계치를 확인할 수 있습니다.
- 수면장애를 예측하는 앱이므로 수면장애 비율을 파이 차트로 볼 수 있게 했습니다.
- 수면상태와 생활의 관계를 눈으로 보기 위해서 박스 플롯 차트를 이용했습니다. 수면장애 컬럼을 X로 지정하기 위해 레이블 인코딩을 하여 밸류 값을 0, 1, 2로 변경해줬습니다.

✉︎ ML.PY
- 주피터 노트북에서 교육한 인공지능 model_ovr.pkl와 데이터를 원핫인코딩해주는 교육된 ct.pkl을 joblib으로 로드했습니다.
- 인공지능 model_ovr.pkl : LogisticRegression로 학습 (결과 값이 3개이므로 multi_class='ovr' 사용했습니다.), ct.pkl : OneHotEncoder()로 학습
- streamlit의 사전을 이용해서 필요한 데이터 정보를 입력받았습니다.
- BMI 범주의 경우 키와 몸무게를 입력해서 BMI를 구할 수 있도록 개발했습니다.
- 새로운 데이터를 데이터프레임으로 만들고 ct.pkl를 이용해서 변환한 뒤 인공지능 model_ovr.pkl로 예측하여 사용자에게 예측 내용을 보여줍니다.



✏️ 배포
-

AWS EC2에 리눅스 프리 티어를 사용해서 배포했습니다.
- Git 설치 과정과 AWS 배포 과정 블로그 정리했습니다.
- [minseonchoi의 블로그 AWS 카테고리](https://msdev-st.tistory.com/category/AWS)
  
github Actions로 EC2 리눅스에 git pull 자동화했습니다.

현재 사용하고 있는 사용자도 새로운 버전의 화면을 볼 수 있도록 서버 실행 명령어에 --server.runOnSave true를 추가했습니다.




✏️ 사용한 프로그램
-

<a href="https://jupyter.org/"><img src="https://img.shields.io/badge/jupyter-F37626?style=flat-square&logo=jupyter&logoColor=white"/></a>
<a href="https://streamlit.io/"><img src="https://img.shields.io/badge/streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white"/></a>
<a href="https://code.visualstudio.com/"><img src="https://img.shields.io/badge/visualstudiocode-007ACC?style=flat-square&logo=visualstudiocode&logoColor=white"/></a>
<a href="https://aws.amazon.com/ko/console/"><img src="https://img.shields.io/badge/amazonec2-FF9900?style=flat-square&logo=amazonec2&logoColor=000000"/></a>




✏️ 사용한 언어
-

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=minseonchoi&langs_count=8)](https://github.com/minseonchoi/github-readme-stats)


<img src="https://capsule-render.vercel.app/api?type=waving&color=85C8F8&height=150&section=footer" />
